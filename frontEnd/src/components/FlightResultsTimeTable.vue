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

const formatTime = (time) => {
  const formattedTime = new Date(time).toUTCString().replace("GMT", "");

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

  console.log("SELECTED FLIGHTS:", selectedFlights);
  emits("flights-selected", selectedFlights); // send selected flights to parent
};
</script>

<template>
  <div class="available-flights">
    <table>
      <thead>
        <tr>
          <th>Book Seats</th>
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
          <td>{{ formatTime(flight.departTime) }}</td>
          <td>{{ formatTime(flight.arriveTime) }}</td>
          <td>{{ flight.craftName }}</td>
          <td>{{ flight.availableSeats }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div>
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
</style>
