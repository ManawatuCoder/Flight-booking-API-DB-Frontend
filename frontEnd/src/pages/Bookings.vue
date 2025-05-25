<script setup>
import SearchFlightForm from "@/components/SearchFlightForm.vue";
import FlightResultsTimeTable from "@/components/FlightResultsTimeTable.vue";
import { ref } from "vue";

// get search results to pass into results
const availableFlights = ref([]);
const hasSearched = ref(false);

// call and let results component to appear
const handleSearchFlights = (results) => {
  availableFlights.value = results;
  hasSearched.value = true;
};
</script>

<template>
  <h1>Bookings</h1>

  <SearchFlightForm @search-completed="handleSearchFlights" />
  <FlightResultsTimeTable v-if="hasSearched" :flights="availableFlights" />
</template>
