<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  apartment: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <router-link 
    :to="{ name: 'apartment-detail', params: { slug: apartment.slug }}" 
    class="block transition-all duration-300"
    :class="{ 'opacity-60 hover:opacity-70': !apartment.availability, 'hover:shadow-lg': apartment.availability }"
  >
    <div class="bg-white rounded-lg shadow-md overflow-hidden">
      <div class="p-6">
        <div class="flex justify-between items-start">
          <h3 class="text-xl font-bold text-gray-800 mb-2">{{ apartment.name }}</h3>
          <span class="px-2 py-1 text-xs rounded-full" 
            :class="apartment.availability ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
            {{ apartment.availability ? 'Доступно' : 'Недоступно' }}
          </span>
        </div>
        
        <div class="text-gray-700 mb-4 line-clamp-2">{{ apartment.description }}</div>
        
        <div class="flex justify-between items-end">
          <div class="text-2xl font-bold text-indigo-600">₴{{ apartment.price }}</div>
          <div class="text-sm text-gray-600">
            <div>{{ apartment.number_of_rooms }} комн. · {{ apartment.square }} м²</div>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template> 