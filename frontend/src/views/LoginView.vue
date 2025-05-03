<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

const router = useRouter();
const username = ref('');
const password = ref('');
const error = ref('');
const isLoading = ref(false);

const login = async () => {
  // Валидация формы
  if (!username.value || !password.value) {
    error.value = 'Пожалуйста, заполните все поля';
    return;
  }
  
  isLoading.value = true;
  error.value = '';
  
  try {
    const response = await api.login({ username: username.value, password: password.value });
    const token = response.data.access;
    
    // Сохраняем токен
    localStorage.setItem('token', token);
    localStorage.setItem('username', username.value);
    
    // Перенаправляем на главную страницу
    router.push('/');
  } catch (err) {
    console.error(err);
    
    if (err.response && err.response.status === 401) {
      error.value = 'Неверное имя пользователя или пароль';
    } else {
      error.value = 'Произошла ошибка при входе. Пожалуйста, попробуйте позже.';
    }
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="max-w-md mx-auto bg-white p-8 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold text-gray-900 mb-6">Вход в систему</h1>
    
    <div v-if="error" class="mb-4 p-3 bg-red-100 text-red-800 rounded-md">
      {{ error }}
    </div>
    
    <form @submit.prevent="login" class="space-y-4">
      <div>
        <label for="username" class="block text-sm font-medium text-gray-700 mb-1">Имя пользователя</label>
        <input 
          id="username"
          v-model="username"
          type="text" 
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
          autocomplete="username"
        >
      </div>
      
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Пароль</label>
        <input 
          id="password"
          v-model="password"
          type="password" 
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
          autocomplete="current-password"
        >
      </div>
      
      <div>
        <button 
          type="submit"
          class="w-full px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          :disabled="isLoading"
        >
          <span v-if="isLoading">Загрузка...</span>
          <span v-else>Войти</span>
        </button>
      </div>
    </form>
  </div>
</template> 