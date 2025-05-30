<script setup>
import { ref } from "vue";
import axios from "axios";

const props = defineProps({
  selectedFlights: Array,
  required: true,
});

let totalCost = 0;

const ticketBookings = ref([]); // store individual tickets in array
const hasBooked = ref(false);
const bookingRefs = ref([]);

for (const flight of props.selectedFlights) {
  for (let i = 0; i < flight.tickets; i++) {
    ticketBookings.value.push({
      price: flight.price,
      departTime: flight.departTime,
      arriveTime: flight.arriveTime,
      code: flight.code,
      startLocation: flight.startLocation,
      destination: flight.destination,
      name: "", // filled out in form
    });
    totalCost += flight.price;
  }
}

const bookFlights = async () => {
  for (const ticket of ticketBookings.value) {
    // call API to book ticket
    try {
      const response = await axios.get("http://127.0.0.1:9000/bookflight/", {
        params: {
          code: ticket.code,
          name: ticket.name,
        },
      });
      bookingRefs.value.push(response.data);
      console.log(
        "Booked ticket for: " +
          bookingRefs.value.name +
          " on flight " +
          ticket.code,
        response.data
      );
      hasBooked.value = true;
    } catch (error) {
      console.error("Error booking flight: ", error);
    }
  }
};

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
</script>

<template>
  <div v-if="!hasBooked" class="booking-container">
    <h2 class="title">Selected Flights</h2>
    <h3>Verify your order before you confirm the booking</h3>
    <table>
      <thead>
        <tr>
          <th>Price</th>
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
          <td>${{ ticket.price }}</td>
          <td>{{ formatTime(ticket.departTime, ticket.startLocation) }}</td>
          <td>{{ formatTime(ticket.arriveTime, ticket.destination) }}</td>
          <td>{{ ticket.code }}</td>
          <td>{{ ticket.startLocation }}</td>
          <td>{{ ticket.destination }}</td>
          <td>
            <input
              class="location-input input"
              type="text"
              placeholder="Enter Name"
              v-model="ticket.name"
            />
          </td>
        </tr>
        <td class="price">Total</td>
        <td class="price">$ {{ totalCost }}</td>
      </tbody>
    </table>

    <button @click="bookFlights" class="button">Confirm Booking</button>
  </div>

  <div v-if="hasBooked" class="success-container">
    <h3 class="success-text">Success</h3>
    <p>Your tickets have been booked.</p>
    <p>Review your details.</p>

    <table>
      <thead>
        <td>Name</td>
        <td>Flight Code</td>
        <td>Reference</td>
      </thead>
      <tbody>
        <tr v-for="booking in bookingRefs" class="summary">
          <td>{{ booking.name }}</td>
          <td>{{ booking.flightCode }}</td>
          <td>{{ booking.bookingref }}</td>
        </tr>
      </tbody>
    </table>
    <img src="../assets/tick.webp" class="success-img" />
  </div>
</template>

<style scoped>
h2 {
  margin: 2rem 0;
}

h3 {
  margin: 1rem 0;
}

.success-text {
  color: #3fd43f;
  font-size: 30px;
  text-align: center;
  margin: 1rem;
}

.book-flights {
  padding: 2rem 1rem;
}

.price {
  font-size: 18px;
  font-weight: 600;
  margin: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.315);
}

.summary {
}

tr {
  border: 1px solid rgba(255, 255, 255, 0.13);
}

.button {
  background-color: rgb(33, 165, 72);
  transition: ease-in-out 0.2s;
  color: var(--color-white);
}
.button:hover {
  background-color: rgb(59, 173, 93);
}

.input {
  padding: 1rem;
  color: var(--color-white);
}
.input::placeholder {
  color: rgba(255, 255, 255, 0.288);
}
</style>
