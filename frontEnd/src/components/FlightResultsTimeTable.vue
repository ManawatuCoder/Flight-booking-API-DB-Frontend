<script setup>
import { ref } from "vue";
import axios from "axios";

const props = defineProps({
  flights: {
    // pass through array of flights
    type: Array,
    required: true,
  },
});

const emits = defineEmits(["flights-selected"]);

const seatSelections = ref({});
const maxSeats = ref();

const formatTime = (time, timeZone) => {
  const newTime = new Date(time);
  let formattedTime = new Date(time);
  switch (timeZone) {
    case "YMML":
      newTime.setHours(newTime.getHours() - 2);
      formattedTime = new Date(newTime)
        .toUTCString()
        .replace(":00 GMT", " AEST")
        .replace("2025", "")
        .replace(",", "");
      break;
    case "NZCI":
      newTime.setMinutes(newTime.getMinutes() + 45);
      formattedTime = new Date(newTime)
        .toUTCString()
        .replace(":00 GMT", " CST")
        .replace("2025", "")
        .replace(",", "");
      break;
    default:
      formattedTime = new Date(newTime)
        .toUTCString()
        .replace(":00 GMT", " NZT")
        .replace("2025", "")
        .replace(",", "");
      break;
  }

  return formattedTime;
};
const sendSelectedFlights = () => {
  const ticketEntries = Object.entries(seatSelections.value);
  const validSelections = ticketEntries.filter(([_, tickets]) => tickets > 0); // only store tickets with passengers added
  const selectedFlights = validSelections
    .map(([code, tickets]) => {
      const numericCode = Number(code);
      const flight = props.flights.find((f) => f.code === numericCode);

      if (!flight) {
        console.warn("No flight found for code: ", numericCode);
        return null;
      }

      return {
        ...flight,
        tickets,
      };
    })
    .filter((flight) => flight !== null); // filter out null values

  emits("flights-selected", selectedFlights); // send selected flights to parent
};
</script>

<template>
  <div class="available-flights">
    <table>
      <thead>
        <tr>
          <th>Book Seats</th>
          <th>Price</th>
          <th>Depart Time</th>
          <th>Arrive Time</th>
          <th>Flight Name</th>
          <th>Remaining Seats</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="flight in flights" :key="flight.code">
          <td class="book-seats">
            <input
              type="number"
              v-model.number="seatSelections[flight.code]"
              placeholder="0"
              min="0"
              :max="flight.availableSeats"
            />
          </td>
          <td>${{ flight.price }}</td>
          <td>{{ formatTime(flight.departTime, flight.startLocation) }}</td>
          <td>{{ formatTime(flight.arriveTime, flight.destination) }}</td>
          <td>{{ flight.craftName }}</td>
          <td>{{ flight.availableSeats }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="button-div">
    <button @click="sendSelectedFlights" class="button">Continue</button>
  </div>
</template>
<style scoped>
li {
  list-style-type: none;
}

.available-flights {
  margin-top: 1rem;
}

.book-seats {
  max-width: 10px;
}

.book-seats input {
  max-width: 30px;
  height: 20px;
}

.button-div {
  display: flex;
  justify-content: center;
}
</style>
