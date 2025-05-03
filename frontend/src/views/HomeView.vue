<template>
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">Добро пожаловать в Rental Service</h1>
      <p class="text-lg text-gray-600 max-w-2xl mx-auto">
        Найдите идеальную квартиру для аренды с нашим удобным сервисом поиска.
      </p>
      <router-link 
        to="/apartments" 
        class="mt-8 inline-block px-6 py-3 rounded-md text-white bg-indigo-600 hover:bg-indigo-700 font-medium text-lg"
      >
        Начать поиск
      </router-link>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
      <div class="bg-white p-6 rounded-lg shadow-md">
        <div class="text-3xl text-indigo-600 mb-4">
          <i class="fas fa-search"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-800 mb-2">Удобный поиск</h3>
        <p class="text-gray-600">Используйте продвинутые фильтры, чтобы найти квартиру, соответствующую всем вашим требованиям.</p>
      </div>
      
      <div class="bg-white p-6 rounded-lg shadow-md">
        <div class="text-3xl text-indigo-600 mb-4">
          <i class="fas fa-building"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-800 mb-2">Большой выбор</h3>
        <p class="text-gray-600">В нашей базе данных множество вариантов для аренды - от студий до многокомнатных квартир.</p>
      </div>
      
      <div class="bg-white p-6 rounded-lg shadow-md">
        <div class="text-3xl text-indigo-600 mb-4">
          <i class="fas fa-heart"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-800 mb-2">Проверенные варианты</h3>
        <p class="text-gray-600">Мы тщательно проверяем все предложения, чтобы обеспечить вам безопасную и комфортную аренду.</p>
      </div>
    </div>
  </div>
</template> 