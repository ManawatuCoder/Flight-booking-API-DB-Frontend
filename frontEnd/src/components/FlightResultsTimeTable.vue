<script setup>
import { ref } from "vue";

const props = defineProps({
  flights: {
    // pass through array of flights
    type: Array,
    required: true,
  },
});

const seatSelections = ref({});
const maxSeats = ref(5);

const formatTime = (time) => {
  const formattedTime = new Date(time).toUTCString().replace("GMT", "");

  return formattedTime;
};

const handleBooking = () => {
  const selected = Object.entries(seatSelections.value)
    .filter(([_, tickets]) => tickets > 0)
    .map(([flightCode, tickets]) => ({
      flightCode,
      tickets,
    }));

  for (const booking of selected) {
    // book each ticket for each flight
    for (let i = 1; i < booking.tickets + 1; i++) {
      // call API to book ticket
      console.log(
        "Booking ticket: " + i + " from flight " + booking.flightCode
      );
    }
  }

  console.log("Booking these flights: ", selected);
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
              :max="maxSeats"
            />
          </td>
          <td>{{ formatTime(flight.departTime) }}</td>
          <td>{{ formatTime(flight.arriveTime) }}</td>
          <td>{{ flight.craftName }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div>
    <button @click="handleBooking">Book Flight</button>
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
