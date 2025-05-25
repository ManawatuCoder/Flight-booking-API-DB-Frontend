<script setup>
import { ref } from "vue";
import axios from "axios";
import FlightResultsTimeTable from "./FlightResultsTimeTable.vue";

const props = defineProps({
  selectedFlights: Array,
  required: true,
});

const ticketBookings = ref([]); // store individual tickets in array
const hasBooked = ref(false);

for (const flight of props.selectedFlights) {
  for (let i = 0; i < flight.tickets; i++) {
    ticketBookings.value.push({
      departTime: flight.departTime,
      arriveTime: flight.arriveTime,
      code: flight.code,
      startLocation: flight.startLocation,
      destination: flight.destination,
      name: "", // filled out in form
    });
  }
}

const bookFlights = async () => {
  for (const ticket of ticketBookings.value) {
    // call API to book ticket
    try {
      const response = await axios.get("http://127.0.0.1:8000/bookflight/", {
        params: {
          code: ticket.code,
          name: ticket.name,
        },
      });
      console.log(
        "Booked ticket for: " + ticket.name + " on flight " + ticket.code,
        response
      );
      hasBooked.value = true;
    } catch (error) {
      console.error("Error booking flight: ", error);
    }
  }
};
</script>

<template>
  <div v-if="!hasBooked" class="booking-container">
    <h2 class="title">Selected Flights</h2>
    <table>
      <thead>
        <tr>
          <th>Departs at</th>
          <th>Arrives at</th>
          <th>Flight Code</th>
          <th>Departs From</th>
          <th>Destination</th>
          <th>Passenger Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(ticket, index) in ticketBookings" :key="index">
          <td>{{ ticket.departTime }}</td>
          <td>{{ ticket.arriveTime }}</td>
          <td>{{ ticket.code }}</td>
          <td>{{ ticket.startLocation }}</td>
          <td>{{ ticket.destination }}</td>
          <td>
            <input type="text" placeholder="Enter Name" v-model="ticket.name" />
          </td>
        </tr>
      </tbody>
    </table>

    <button @click="bookFlights" class="button">Book Flights</button>
  </div>

  <div v-if="hasBooked" class="success-container">
    <h3 class="success-text">Success</h3>
    <p>Your tickets have been booked.</p>
    <img src="../assets/tick.webp" class="success-img" />
  </div>
</template>

<style scoped>
h2 {
  margin: 2rem 0;
}

.success-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  border-radius: 25px;
  border: 1px solid #44444427;
  box-shadow: 2px 6px 24px #44444431;
}

.success-text {
  color: #5cb85c;
  font-size: 26px;
  text-align: center;
  margin: 1rem;
}

.book-flights {
  padding: 2rem 1rem;
}

.success-img {
  height: 100px;
  width: 100px;
  margin: 2rem;
}
</style>
