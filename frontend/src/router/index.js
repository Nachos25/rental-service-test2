import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue'),
    meta: { title: 'Главная' }
  },
  {
    path: '/apartments',
    name: 'apartments',
    component: () => import('@/views/ApartmentListView.vue'),
    meta: { title: 'Список квартир' }
  },
  {
    path: '/apartments/:slug',
    name: 'apartment-detail',
    component: () => import('@/views/ApartmentDetailView.vue'),
    meta: { title: 'Детали квартиры' }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginView.vue'),
    meta: { title: 'Вход' }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Change document title when route changes
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Rental Service';
  next();
});

export default router; 