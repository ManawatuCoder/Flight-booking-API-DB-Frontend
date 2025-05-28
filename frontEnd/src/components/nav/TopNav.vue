<script setup></script>
<template>
  <nav>
    <router-link to="/" class="link">AirlineBooker</router-link>
    <div>
      <router-link to="/" class="link">Home</router-link>
      <router-link to="/search" class="link">Search Flights</router-link>
      <router-link to="/bookings" class="link">Bookings</router-link>
    </div>
  </nav>
</template>
<style>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: transparent;
  color: var(--color-white);
  padding: 1rem;
  width: calc(100% - 2rem);
}

.link {
  color: rgb(235, 235, 235);
  text-decoration: none;
  padding: 8px 15px;
  cursor: pointer;
  transition: ease-in-out 0.1s;
  border-radius: 4px;
}

.link:hover {
  background-color: rgba(143, 143, 143, 0.116);
}
</style>
