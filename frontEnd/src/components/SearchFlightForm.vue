<script setup>
import axios from "axios";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

import { onMounted, ref, computed, onUnmounted } from "vue";

const emit = defineEmits(["search-completed"]); // to tell parent component that search has been made

const date = ref([]);
const departureAirportName = ref("");
const departureAirportCode = ref("");
const destinationAirportName = ref("");
const destinationAirportCode = ref("");

// state for dynamic airport search results
const departRef = ref(null);
const destRef = ref(null);
const showDepartSuggestions = ref(false);
const showDestSuggestions = ref(false);

const airportsList = ref([]);

const getAirports = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:9000/airportlist/");
    airportsList.value = Object.entries(response.data).map(([key, name]) => ({
      key,
      name,
    }));
  } catch (error) {
    console.error("Failed to get airports list: ", error);
  }
};
const filteredDepartures = computed(() => {
  if (departureAirportName.value.length < 1) return;
  return airportsList.value.filter((airport) =>
    airport.name
      .toLowerCase()
      .includes(departureAirportName.value.toLowerCase())
  );
});

const filteredArrivals = computed(() => {
  if (destinationAirportName.value.length < 1) return;
  return airportsList.value.filter((airport, code) =>
    airport.name
      .toLowerCase()
      .includes(destinationAirportName.value.toLowerCase())
  );
});

function setDepartureInput(airport) {
  departureAirportName.value = airport.name;
  departureAirportCode.value = airport.key;
  showDepartSuggestions.value = false;
}

function setDestinationInput(airport) {
  destinationAirportName.value = airport.name;
  destinationAirportCode.value = airport.key;
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
    const response = await axios.get("http://127.0.0.1:9000/withinperiod/", {
      params: {
        start: departureDateTime,
        end: endDateTime,
        departure: departureAirportCode.value,
        arrival: destinationAirportCode.value,
      },
    });
    console.log("Search Params: ");
    console.log(response.data);
    emit("search-completed", response.data);
  } catch (error) {
    console.error("Failed to search for flights: ", error);
  }
};

// close dropdown when click outside of dropdonw/input
const handleClickOutsideDropdown = (event) => {
  if (departRef.value && !departRef.value.contains(event.target)) {
    showDepartSuggestions.value = false;
    showDestSuggestions.value = false;
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
      <div class="input-container">
        <div class="location-container">
          <div class="input-wrapper" ref="departRef">
            <label>Depart from</label>
            <input
              placeholder="Dairy Flats"
              type="text"
              class="location-input"
              v-model="departureAirportName"
              @input="showDepartSuggestions = true"
            />
            <ul v-if="showDepartSuggestions" class="suggestions">
              <li v-for="(airport, i) in filteredDepartures" :key="i">
                <button @click="setDepartureInput(airport)">
                  {{ airport.name }}
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
              v-model="destinationAirportName"
              @input="showDestSuggestions = true"
            />
            <ul v-if="showDestSuggestions" class="suggestions">
              <li v-for="(airport, i) in filteredArrivals" :key="i">
                <button @click="setDestinationInput(airport)">
                  {{ airport.name }}
                </button>
              </li>
            </ul>
          </div>
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
    </div>
    <button type="submit" class="button">Search</button>
  </form>
</template>

<style scoped>
.booking-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  max-width: 500px;
  background-color: var(--color-feature);
  padding: 1rem 1.5rem 1.5rem 1.5rem;
}

.location {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 1rem;
}
.location-container {
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
  width: calc(100% - 10px);
  background-color: var(--color-input-background);
  color: var(--color-white);
  border: none;
}

.location-input::placeholder {
  color: var(--color-input-text);
}

.location-input:focus {
  border: none;
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
  background-color: var(--color-input-background);
}

::v-deep(.dp__input) {
  padding-left: 35px;
  background-color: var(--color-input-background);
}
::v-deep(.dp__action_row) {
  width: 100%;
  display: flex;
  justify-content: center;
}
::v-deep(.dp__action_buttons) {
  margin: 0;
  display: flex;
  flex-direction: column;
}

::v-deep(.dp__action_select) {
  width: 300px;
  height: 50px;
  text-align: center;
  display: flex;
  justify-content: center;
}
::v-deep(.dp__action_cancel) {
  width: 300px;
  height: 30;
  margin: 5px;
  background-color: rgba(211, 211, 211, 0.308);
  text-align: center;
  display: flex;
  justify-content: center;
}

::v-deep(.dp__outer_menu_wrap) {
}
::v-deep(.dp__menu) {
  background-color: #3361af;
}

::v-deep(.dp__cell_inner),
::v-deep(.dp__pointer),
::v-deep(.dp--future) {
  color: white;
}

::v-deep(.dp__input_icon) {
  color: var(--color-input-text);
}

::v-deep(.dp__range_between) {
  background-color: rgba(255, 255, 255, 0.185);
  border: none;
}

::v-deep(.dp__calendar_header_item) {
  color: white;
}
::v-deep(.dp__month_year_select) {
  color: white;
}

::v-deep(.dp__selection_preview) {
  color: white;
}
::v-deep(.dp--past) {
  color: gray;
}

.suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid var(--color-border);
  z-index: 1000;
  margin-top: 2px;
  padding: 0;
  width: 100%;
  background-color: var(--color-input-background);
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
  border: 1px solid var(--color-border);
  border-top: none;
  background-color: #3361af;
  color: var(--color-white);
  transition: ease-in-out 0.2s;
}

li button:hover {
  background-color: #467cda;
}
</style>
