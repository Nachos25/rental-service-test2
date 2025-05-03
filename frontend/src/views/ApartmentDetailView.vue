<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import api from '@/services/api';

const route = useRoute();
const router = useRouter();
const apartment = ref(null);
const isLoading = ref(true);
const error = ref(null);
const isAuthenticated = computed(() => !!localStorage.getItem('token'));

const fetchApartmentDetails = async () => {
  isLoading.value = true;
  error.value = null;
  
  try {
    const response = await api.getApartment(route.params.slug);
    apartment.value = response.data;
  } catch (err) {
    error.value = 'Не удалось загрузить информацию о квартире';
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

const deleteApartment = async () => {
  if (!confirm('Вы уверены, что хотите удалить эту квартиру?')) {
    return;
  }
  
  try {
    await api.deleteApartment(route.params.slug);
    router.push('/apartments');
  } catch (err) {
    alert('Произошла ошибка при удалении квартиры');
    console.error(err);
  }
};

onMounted(() => {
  fetchApartmentDetails();
});
</script>

<template>
  <div>
    <div v-if="isLoading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
    </div>
    
    <div v-else-if="error" class="bg-red-100 p-4 rounded-md text-red-800 mb-6">
      {{ error }}
    </div>
    
    <div v-else-if="apartment" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Заголовок с кнопками управления -->
      <div class="p-6 border-b">
        <div class="flex justify-between items-start mb-2">
          <h1 class="text-3xl font-bold text-gray-900">{{ apartment.name }}</h1>
          <span 
            class="px-3 py-1 text-sm rounded-full"
            :class="apartment.availability ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'"
          >
            {{ apartment.availability ? 'Доступно' : 'Недоступно' }}
          </span>
        </div>
        
        <div v-if="isAuthenticated && apartment.owner === localStorage.getItem('username')" class="flex space-x-4 mt-4">
          <button 
            @click="deleteApartment"
            class="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700"
          >
            Удалить
          </button>
        </div>
      </div>
      
      <!-- Основная информация -->
      <div class="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Левая колонка с информацией -->
        <div class="md:col-span-2">
          <div class="mb-6">
            <h2 class="text-xl font-bold text-gray-800 mb-2">Описание</h2>
            <p class="text-gray-700 whitespace-pre-line">{{ apartment.description }}</p>
          </div>
          
          <div class="mb-6">
            <h2 class="text-xl font-bold text-gray-800 mb-2">Характеристики</h2>
            <div class="grid grid-cols-2 gap-4">
              <div class="flex items-center">
                <span class="text-gray-600 mr-2">Количество комнат:</span>
                <span class="font-medium">{{ apartment.number_of_rooms }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-600 mr-2">Площадь:</span>
                <span class="font-medium">{{ apartment.square }} м²</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-600 mr-2">Владелец:</span>
                <span class="font-medium">{{ apartment.owner }}</span>
              </div>
              <div class="flex items-center">
                <span class="text-gray-600 mr-2">Последнее обновление:</span>
                <span class="font-medium">{{ new Date(apartment.updated_at).toLocaleDateString() }}</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Правая колонка с ценой -->
        <div class="bg-gray-50 p-6 rounded-lg">
          <div class="text-3xl font-bold text-indigo-600 mb-2">₴{{ apartment.price }}</div>
          <div class="text-gray-600 mb-6">за месяц</div>
          
          <div class="border-t pt-4 mt-4">
            <button 
              class="w-full px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 disabled:bg-gray-400"
              :disabled="!apartment.availability"
            >
              Связаться с владельцем
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <div v-if="apartment" class="mt-6">
      <router-link 
        to="/apartments" 
        class="text-indigo-600 hover:text-indigo-800"
      >
        &larr; Вернуться к списку квартир
      </router-link>
    </div>
  </div>
</template> 