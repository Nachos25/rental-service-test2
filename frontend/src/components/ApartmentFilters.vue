<script setup>
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['filter']);

const filters = ref({
  price_min: '',
  price_max: '',
  rooms: '',
  available: null,
  search: ''
});

const roomOptions = [1, 2, 3, 4, 5];

const applyFilters = () => {
  // Убираем пустые значения
  const validFilters = {};
  Object.entries(filters.value).forEach(([key, value]) => {
    if (value !== '' && value !== null) {
      validFilters[key] = value;
    }
  });
  
  emit('filter', validFilters);
};

const resetFilters = () => {
  filters.value = {
    price_min: '',
    price_max: '',
    rooms: '',
    available: null,
    search: ''
  };
  
  emit('filter', {});
};
</script>

<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-6">
    <h2 class="text-lg font-bold text-gray-800 mb-4">Фильтры</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
      <!-- Поиск -->
      <div class="col-span-1 md:col-span-2 lg:col-span-3">
        <label class="block text-sm font-medium text-gray-700 mb-1">Поиск</label>
        <input 
          v-model="filters.search"
          type="text" 
          placeholder="Введите название или описание" 
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
        >
      </div>
      
      <!-- Цена от -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Цена от</label>
        <input 
          v-model="filters.price_min"
          type="number" 
          min="0"
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
        >
      </div>
      
      <!-- Цена до -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Цена до</label>
        <input 
          v-model="filters.price_max"
          type="number" 
          min="0"
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
        >
      </div>
      
      <!-- Комнаты -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Комнаты</label>
        <select 
          v-model="filters.rooms"
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
        >
          <option value="">Все</option>
          <option v-for="room in roomOptions" :key="room" :value="room">
            {{ room }}
          </option>
        </select>
      </div>
      
      <!-- Доступность -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Доступность</label>
        <select 
          v-model="filters.available"
          class="w-full p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
        >
          <option :value="null">Все</option>
          <option :value="true">Доступно</option>
          <option :value="false">Недоступно</option>
        </select>
      </div>
    </div>
    
    <div class="flex justify-end space-x-4">
      <button 
        @click="resetFilters"
        class="px-4 py-2 border border-gray-300 rounded-md text-sm text-gray-700 hover:bg-gray-50"
      >
        Сбросить
      </button>
      <button 
        @click="applyFilters"
        class="px-4 py-2 bg-indigo-600 rounded-md text-sm text-white hover:bg-indigo-700"
      >
        Применить
      </button>
    </div>
  </div>
</template> 