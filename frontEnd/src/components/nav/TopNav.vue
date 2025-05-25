<script setup></script>
<template>
  <nav>
    <router-link to="/" class="link">AirlineBooker</router-link>
    <div>
      <router-link to="/" class="link">Home</router-link>
      <router-link to="/bookings" class="link">Bookings</router-link>
      <router-link to="/timetable" class="link">Timetable</router-link>
    </div>
  </nav>
</template>
<style>
nav {
  display: flex;
  justify-content: space-between;
  background-color: var(--color-nav);
  color: var(--color-white);
  padding: 1rem;
}

.link {
  color: var(--color-white);
  text-decoration: none;
  padding: 0 5px;
  cursor: pointer;
}

.link:hover {
  text-decoration: underline;
}
</style>
