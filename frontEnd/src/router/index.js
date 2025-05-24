import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/pages/LandingPage.vue";
import Bookings from "@/pages/Bookings.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/bookings", component: Bookings },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
