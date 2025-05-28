import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/pages/LandingPage.vue";
import SearchFlights from "@/pages/SearchFlights.vue";
import Bookings from "@/pages/Bookings.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/search", component: SearchFlights },
  { path: "/bookings", component: Bookings },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
