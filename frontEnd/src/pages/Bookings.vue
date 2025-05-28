<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

const allBookings = ref([]);
const selectedBookings = ref([]);
const searchName = ref("");
const hasCancelled = ref(false);

const getBookingsFromName = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/searchbooking/", {
      params: {
        name: searchName.value,
      },
    });
    allBookings.value = response.data;
  } catch (error) {
    console.error("Error getting bookings", error);
  }
};

const getBookings = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/searchbooking/");
    allBookings.value = response.data;
  } catch (error) {
    console.error("Error getting bookings", error);
  }
};

const cancelBookings = async () => {
  for (const booking of selectedBookings.value) {
    try {
      await axios.get("http://127.0.0.1:8000/unbookflight/", {
        params: {
          code: booking.bookingRef,
        },
      });
      hasCancelled.value = true;
    } catch (error) {
      console.error("Error cancelling booking", error);
    }
  }
};

const toggleBookingSelection = (booking) => {
  const index = selectedBookings.value.findIndex(
    (b) => b.bookingRef === booking.bookingRef
  );
  if (index === -1) {
    selectedBookings.value.push(booking);
  } else {
    selectedBookings.value.splice(index, 1);
  }
};

onMounted(() => {
  getBookings();
});
</script>

<template>
  <h1>My Bookings</h1>
  <div v-if="!hasCancelled" class="bookings">
    <div class="search-container">
      <input
        type="text"
        v-model="searchName"
        placeholder="Enter Name"
        class="location-input input"
      />
      <button
        @click="getBookingsFromName"
        :value="searchName"
        class="search-button"
      >
        Search
      </button>
    </div>
    <table>
      <thead>
        <td>Flight Code</td>
        <td>Booking Ref</td>
        <td>Name</td>
        <td>Delete</td>
      </thead>
      <tbody>
        <tr v-for="booking in allBookings">
          <td>
            {{ booking.flightCode }}
          </td>
          <td>
            {{ booking.bookingRef }}
          </td>
          <td>
            {{ booking.passengerID }}
          </td>
          <td id="checkbox-container">
            <input
              type="checkbox"
              class="name-box"
              :value="booking.bookingRef"
              :checked="
                selectedBookings.some(
                  (b) => b.bookingRef === booking.bookingRef
                )
              "
              @change="toggleBookingSelection(booking)"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <button class="button" @click="cancelBookings">Cancel Flights</button>
  </div>

  <div v-if="hasCancelled" class="success-container">
    <h3 class="success-text">Success</h3>
    <p>Your bookings have been cancelled.</p>
    <img src="../assets/tick.webp" class="success-img" />
  </div>
</template>

<style scoped>
#checkbox-container {
  width: 60px;
  margin: 0 auto;
}

tr {
  height: 30px;
}

.name-box {
  padding: 10px;
}

.bookings {
  display: flex;
  flex-direction: column;
}

.search-container {
  display: flex;
  width: 100%;
  align-items: center;
}
.input {
  width: 100%;
  height: 50px;
  color: var(--color-white);
  padding: 0 10px;
}

.input::placeholder {
  color: var(--color-input-text);
}

.search-button {
  padding: 1rem;
  margin: 0;
  background-color: var(--color-button);
  border: none;
  color: var(--color-white);
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: ease-in-out 0.2s;
}
.search-button:hover {
  background-color: var(--color-button-hover);
}
</style>
