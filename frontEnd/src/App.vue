<script setup>
import TopNav from "./components/nav/TopNav.vue";
</script>

<template>
  <TopNav />
  <div class="content-wrapper">
    <RouterView />
  </div>
</template>

<style scoped>
.content-wrapper {
  margin: 1rem;
}
</style>
