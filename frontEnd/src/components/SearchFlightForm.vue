<script setup>
import axios from "axios";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

import { onMounted, ref, computed, onUnmounted } from "vue";

const emit = defineEmits(["search-completed"]); // to tell parent component that search has been made

const date = ref([]);
const departureAirport = ref("");
const destinationAirport = ref("");

// state for dynamic airport search results
const departRef = ref(null);
const destRef = ref(null);
const showDepartSuggestions = ref(false);
const showDestSuggestions = ref(false);

const airportsList = ref([]);

// state for displaying results
const availableFlights = ref(null);
const showAvailableFlights = ref(false);

const getAirports = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/airportlist/");
    airportsList.value = Object.values(response.data);
    console.log(response.data);
  } catch (error) {
    console.error("Failed to get airports list: ", error);
  }
};

const filteredDepartures = computed(() => {
  if (departureAirport.value.length < 1) return;
  return airportsList.value.filter((airport) =>
    airport.toLowerCase().includes(departureAirport.value.toLowerCase())
  );
});

const filteredArrivals = computed(() => {
  if (departureAirport.value.length < 1) return;
  return airportsList.value.filter((airport) =>
    airport.toLowerCase().includes(destinationAirport.value.toLowerCase())
  );
});

function setDepartureInput(airport) {
  departureAirport.value = airport;
  showDepartSuggestions.value = false;
}

function setDestinationInput(airport) {
  destinationAirport.value = airport;
  showDestSuggestions.value = false;
}

const searchFlights = async () => {
  // make json object with all fields
  if (!date.value || date.value.length < 1) {
    return;
  }

  // assign date into two variables (in format that backend expects)
  const departureDateTime = date.value[0].toISOString().slice(0, 16);
  const endDateTime = date.value[1]?.toISOString().slice(0, 16); // return date is optional

  try {
    const response = await axios.get("http://127.0.0.1:8000/withinperiod/", {
      params: {
        start: departureDateTime,
        end: endDateTime,
        departure: "NZCI",
        arrival: "NZNE",
      },
    });
    emit("search-completed", response.data);

    emit("search-completed", response.data);
  } catch (error) {
    console.error("Failed to search for flights: ", error);
  }
};

// close dropdown when click outside of dropdonw/input
const handleClickOutsideDropdown = (event) => {
  if (departRef.value && !departRef.value.contains(event.target)) {
    showDepartSuggestions.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", handleClickOutsideDropdown);
  getAirports();
});

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutsideDropdown);
});
</script>

<template>
  <form class="booking-form" @submit.prevent="searchFlights">
    <div class="location">
      <div class="input-wrapper" ref="departRef">
        <label>Depart from</label>
        <input
          placeholder="Dairy Flats"
          type="text"
          class="location-input"
          v-model="departureAirport"
          @input="showDepartSuggestions = true"
        />
        <ul v-if="showDepartSuggestions" class="suggestions">
          <li v-for="(airport, i) in filteredDepartures" :key="i">
            <button @click="setDepartureInput(airport)">
              {{ airport }}
            </button>
          </li>
        </ul>
      </div>

      <div class="input-wrapper" ref="destRef">
        <label>Arrive at</label>
        <input
          placeholder="Melbourne"
          type="text"
          class="location-input"
          v-model="destinationAirport"
          @input="showDestSuggestions = true"
        />
        <ul v-if="showDestSuggestions" class="suggestions">
          <li v-for="(airport, i) in filteredArrivals" :key="i">
            <button @click="setDestinationInput(airport)">
              {{ airport }}
            </button>
          </li>
        </ul>
      </div>
    </div>

    <div class="date-time">
      <label>Search within range (select two dates)</label>
      <VueDatePicker
        v-model="date"
        :multi-calendars="2"
        :min-date="new Date()"
        :range="{ partialRange: false }"
        class="date-picker"
      />
    </div>
    <button type="submit">Search</button>
  </form>
</template>

<style scoped>
.booking-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 500px;
  background-color: var(--color-feature);
  padding: 1rem 1.5rem 1.5rem 1.5rem;
  border-radius: 6px;
}

.location {
  display: flex;
  gap: 1rem;
}

.input-wrapper {
  display: flex;
  flex: 1;
  flex-direction: column;
  position: relative;
}

.location-input {
  width: 100%;
  width: calc(100% - 10px);
}

.date-time {
}

/* Vue Date Picker styles */
::v-deep(.dp__input),
.location-input {
  border: 1px solid var(--color-border);
  padding: 1px;
  line-height: 30px;
  border-radius: 4px;
  padding: 5px;
}

::v-deep(.dp__input) {
  padding-left: 35px;
}

.suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 200px;
  overflow-y: auto;
  background-color: white;
  border: 1px solid var(--color-border);
  z-index: 1000;
  margin-top: 2px;
  padding: 0;
}

li {
  list-style-type: none;
}

li button {
  margin: 0;
  padding: 1rem;
  border-radius: 0;
  width: 100%;
  cursor: pointer;
  background-color: white;
  border: 1px solid var(--color-border);
  border-top: none;
}

li button:hover {
  background-color: rgb(240, 240, 240);
}
</style>
