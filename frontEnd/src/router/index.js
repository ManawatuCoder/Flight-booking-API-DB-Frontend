import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/pages/LandingPage.vue";
import Bookings from "@/pages/Bookings.vue";
import Timetable from "@/pages/Timetable.vue";

const routes = [
  { path: "/", component: LandingPage },
  { path: "/bookings", component: Bookings },
  { path: "/timetable", component: Timetable },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
