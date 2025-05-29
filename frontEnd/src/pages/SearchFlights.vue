<script setup>
import SearchFlightForm from "@/components/SearchFlightForm.vue";
import FlightResultsTimeTable from "@/components/FlightResultsTimeTable.vue";
import { ref } from "vue";
import BookingModule from "@/components/BookingModule.vue";
import { useSuccessStatusStore } from "@/stores/successStatusStore";

// get search results to pass into results
const availableFlights = ref([]);
const successStatusStore = useSuccessStatusStore();
const selectedFlights = ref([]);

// call and let results component to appear
const handleSearchFlights = (results) => {
  availableFlights.value = results;
  successStatusStore.setSuccessStatus(true);
};

const handleFlightsSelected = (flights) => {
  selectedFlights.value = flights;
  successStatusStore.setBookingRef(true);
};
</script>

<template>
  <h1 v-if="!successStatusStore.isBookingRef">Search Flights</h1>

  <div>
    <SearchFlightForm
      v-if="!successStatusStore.successStatus"
      @search-completed="handleSearchFlights"
    />
    <FlightResultsTimeTable
      v-if="successStatusStore.successStatus && !successStatusStore.isBookingRef"
      :flights="availableFlights"
      @flights-selected="handleFlightsSelected"
    />
    <BookingModule v-if="successStatusStore.isBookingRef" :selectedFlights="selectedFlights" />
  </div>
</template>

<style></style>
