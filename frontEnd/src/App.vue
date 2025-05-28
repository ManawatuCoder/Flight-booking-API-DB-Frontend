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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
