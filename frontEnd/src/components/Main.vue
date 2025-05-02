<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const flights = ref(null);

const getFlights = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/flightslist/");
    flights.value = response.data;
    console.log(response.data);
  } catch (error) {
    console.error(error);
    flights.value;
  }
};

getFlights();
</script>

<template>
  <header>Assignment 2 - Alex Malone, Ben Perkins</header>
  <p>{{ flights }}</p>
</template>
