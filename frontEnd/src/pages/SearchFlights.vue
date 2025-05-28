<script setup>
import SearchFlightForm from "@/components/SearchFlightForm.vue";
import FlightResultsTimeTable from "@/components/FlightResultsTimeTable.vue";
import { ref } from "vue";
import BookingModule from "@/components/BookingModule.vue";

// get search results to pass into results
const availableFlights = ref([]);
const hasSearched = ref(false);
const selectedFlights = ref([]);
const isBooking = ref(false);

// call and let results component to appear
const handleSearchFlights = (results) => {
  availableFlights.value = results;
  hasSearched.value = true;
};

const handleFlightsSelected = (flights) => {
  selectedFlights.value = flights;
  isBooking.value = true;
};
</script>

<template>
  <h1 v-if="!isBooking">Search Flights</h1>

  <div>
    <SearchFlightForm
      v-if="!hasSearched"
      @search-completed="handleSearchFlights"
    />
    <FlightResultsTimeTable
      v-if="hasSearched && !isBooking"
      :flights="availableFlights"
      @flights-selected="handleFlightsSelected"
    />
    <BookingModule v-if="isBooking" :selectedFlights="selectedFlights" />
  </div>
</template>

<style></style>
