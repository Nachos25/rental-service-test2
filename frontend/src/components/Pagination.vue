<script setup>
import { defineProps, defineEmits, computed } from 'vue';

const props = defineProps({
  currentPage: {
    type: Number,
    required: true
  },
  totalPages: {
    type: Number,
    required: true
  }
});

const emit = defineEmits(['page-change']);

const pages = computed(() => {
  let result = [];
  
  // Всегда показываем 1 страницу
  result.push(1);
  
  // Добавляем текущую страницу и страницы вокруг неё
  for (let i = Math.max(2, props.currentPage - 1); i <= Math.min(props.totalPages - 1, props.currentPage + 1); i++) {
    result.push(i);
  }
  
  // Всегда показываем последнюю страницу если она существует
  if (props.totalPages > 1) {
    result.push(props.totalPages);
  }
  
  // Убираем дубликаты и сортируем
  return [...new Set(result)].sort((a, b) => a - b);
});

const changePage = (page) => {
  if (page !== props.currentPage && page >= 1 && page <= props.totalPages) {
    emit('page-change', page);
  }
};
</script>

<template>
  <div v-if="totalPages > 1" class="flex justify-center my-6">
    <nav class="flex items-center space-x-1">
      <!-- Кнопка "Назад" -->
      <button 
        @click="changePage(currentPage - 1)"
        :disabled="currentPage === 1"
        class="px-3 py-2 rounded-md text-sm font-medium" 
        :class="currentPage === 1 ? 'text-gray-400 cursor-not-allowed' : 'text-gray-700 hover:bg-gray-200'"
      >
        &#8592;
      </button>
      
      <!-- Номера страниц -->
      <template v-for="(page, index) in pages" :key="page">
        <!-- Добавляем многоточие, если есть разрыв между страницами -->
        <span 
          v-if="index > 0 && page > pages[index - 1] + 1" 
          class="px-3 py-2 rounded-md text-gray-500"
        >
          ...
        </span>
        
        <button 
          @click="changePage(page)"
          class="px-3 py-2 rounded-md text-sm font-medium"
          :class="page === currentPage ? 'bg-indigo-600 text-white' : 'text-gray-700 hover:bg-gray-200'"
        >
          {{ page }}
        </button>
      </template>
      
      <!-- Кнопка "Вперед" -->
      <button 
        @click="changePage(currentPage + 1)"
        :disabled="currentPage === totalPages"
        class="px-3 py-2 rounded-md text-sm font-medium" 
        :class="currentPage === totalPages ? 'text-gray-400 cursor-not-allowed' : 'text-gray-700 hover:bg-gray-200'"
      >
        &#8594;
      </button>
    </nav>
  </div>
</template> 