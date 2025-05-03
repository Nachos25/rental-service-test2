<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isAuthenticated = ref(false);

onMounted(() => {
  isAuthenticated.value = !!localStorage.getItem('token');
});

const logout = () => {
  localStorage.removeItem('token');
  isAuthenticated.value = false;
  router.push('/');
};
</script>

<template>
  <nav class="bg-white shadow-md">
    <div class="container mx-auto px-4">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex-shrink-0 flex items-center">
            <span class="text-2xl font-bold text-indigo-600">Rental Service</span>
          </router-link>
          <div class="ml-10 flex items-center space-x-4">
            <router-link 
              to="/apartments" 
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-indigo-600"
            >
              Квартиры
            </router-link>
          </div>
        </div>
        <div class="flex items-center">
          <template v-if="isAuthenticated">
            <button 
              @click="logout"
              class="ml-4 px-4 py-2 rounded-md text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700"
            >
              Выйти
            </button>
          </template>
          <template v-else>
            <router-link 
              to="/login" 
              class="px-4 py-2 rounded-md text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700"
            >
              Войти
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template> 