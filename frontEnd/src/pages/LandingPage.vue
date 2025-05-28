<template>
  <div class="container">
    <div>
      <h1>AirlineBooker</h1>
      <h2>You want flights? We got em</h2>
      <div class="text">
        <p>
          Operating out of Dairy Flats airport, we offer a range of flights to
          various places in Australia and New Zealand
        </p>
        <p>Check out our 'Search Flights' feature!</p>
        <br />
        <br />
        <RouterLink to="/search" class="button"
          >Search for Flights Now!</RouterLink
        >
      </div>
    </div>

    <img src="\src\assets\airplane.png" class="image" />
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;

  margin: 4rem;
  display: flex;
  width: 90%;
  align-items: flex-start;
  justify-content: space-between;
}
h2 {
  margin: 1rem;
  font-weight: 400;
}
.text {
  width: 70vw;
  max-width: 700px;
}
p {
  margin: 2rem;
}

.image {
  right: 20px;
  margin-top: 4rem;
  width: 500px;
}

@media screen and (max-width: 1300px) {
  .container {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
}
</style>
