<script setup>
import { ref } from "vue";

const flights = ref([]);
for (let i = 0; i < 10; i++) {
  flights.value.push({
    time: i,
    arriveTime: i + 1,
    name: `Flight ${i + 1}`,
    duration: `${i * 10} min`,
  });
}
</script>
<template>
  <h1>Timetable</h1>
  <table>
    <thead>
      <tr>
        <th>Time</th>
        <th>Arrive Time</th>
        <th>Flight Name</th>
        <th>Duration</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(flight, index) in flights" :key="index">
        <td>{{ flight.time }}</td>
        <td>{{ flight.arriveTime }}</td>
        <td>{{ flight.name }}</td>
        <td>{{ flight.duration }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style>
table {
  border-collapse: collapse;
}
th,
td {
  margin: 0;
  padding: 1rem;
}

th,
td {
  border: 1px solid var(--color-border);
}
</style>
