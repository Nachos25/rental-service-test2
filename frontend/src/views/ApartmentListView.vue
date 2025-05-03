<script setup>
import { ref, onMounted } from 'vue';
import api from '@/services/api';
import ApartmentCard from '@/components/ApartmentCard.vue';
import ApartmentFilters from '@/components/ApartmentFilters.vue';
import Pagination from '@/components/Pagination.vue';

const apartments = ref([]);
const isLoading = ref(true);
const error = ref(null);
const currentPage = ref(1);
const totalPages = ref(1);
const activeFilters = ref({});

const fetchApartments = async () => {
  isLoading.value = true;
  error.value = null;
  
  try {
    const params = { ...activeFilters.value, page: currentPage.value };
    const response = await api.getApartments(params);
    
    apartments.value = response.data.results;
    
    // Вычисляем общее количество страниц
    const count = response.data.count;
    const pageSize = 10; // Размер страницы на бэкенде
    totalPages.value = Math.ceil(count / pageSize);
  } catch (err) {
    error.value = 'Не удалось загрузить список квартир';
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

const handleFilter = (filters) => {
  activeFilters.value = filters;
  currentPage.value = 1;
  fetchApartments();
};

const handlePageChange = (page) => {
  currentPage.value = page;
  fetchApartments();
};

onMounted(() => {
  fetchApartments();
});
</script>

<template>
  <div>
    <h1 class="text-3xl font-bold text-gray-900 mb-6">Поиск квартир</h1>
    
    <ApartmentFilters @filter="handleFilter" />
    
    <div v-if="isLoading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
    </div>
    
    <div v-else-if="error" class="bg-red-100 p-4 rounded-md text-red-800 mb-6">
      {{ error }}
    </div>
    
    <div v-else-if="apartments.length === 0" class="text-center py-12">
      <p class="text-gray-600 text-lg">Не найдено квартир, соответствующих вашему запросу</p>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <ApartmentCard 
        v-for="apartment in apartments" 
        :key="apartment.id" 
        :apartment="apartment" 
      />
    </div>
    
    <Pagination 
      :current-page="currentPage" 
      :total-pages="totalPages" 
      @page-change="handlePageChange"
    />
  </div>
</template> 