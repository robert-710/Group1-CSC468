<template>
  <header>
    <img :src="logo" alt="Scenic Navigation App Logo" class="logo">
      <h1>Scenic Navigation App</h1>
  </header>
  <main>
    <MapComponent v-if="mapLoaded" :directions-service="directionsService" @directions-calculated="handleDirectionsCalculated" />
    <div v-else-if="apiKey" class="route-calculation-components">
      <RouteSuggestionsComponent :directions-service="directionsService" @directions-calculated="handleDirectionsCalculated" />
    </div>
    <div v-else-if="!mapLoaded && !apiKey" class="api-key-form">
      <input type="text" v-model="apiKey" placeholder="Enter your Google Maps API Key" />
      <button @click="initializeMap">Submit</button>
    </div>
  </main>
</template>

<script>
/* global google */
import MapComponent from './components/MapComponent.vue';
import RouteSuggestionsComponent from './components/RouteSuggestionsComponent.vue';
export default {
  name: 'App',
  data() {
    return {
      logo: require('@/assets/logo.png'),
      apiKey: process.env.VUE_APP_GOOGLE_MAPS_API_KEY,
      mapLoaded: false,
      directionsService: null,
    };
  },
  components: {
    MapComponent,
    RouteSuggestionsComponent,
  },
  methods: {
    initializeMap() {
      if (this.apiKey) {
        const script = document.createElement('script');
        script.src = `https://maps.googleapis.com/maps/api/js?key=${this.apiKey}&libraries=places,directions`;
        script.async = true;
        script.defer = true;
        document.head.appendChild(script);

        // Trigger the custom event to signal API readiness
        script.addEventListener('load', () => {
          this.directionsService = new google.maps.DirectionsService();
          this.mapLoaded = true;
          window.dispatchEvent(new Event('googleMapsApiLoaded'));
        });
      } else {
        alert('Please enter a valid Google Maps API key.');
      }
    },
    handleDirectionsCalculated(directions) {
      this.$refs.mapComponent.renderDirections(directions);
    },
  },
  mounted() {
    // Call only after setting up the Google Maps API key in your environment
    this.initializeMap();
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

body {
  font-family: 'Fira Sans', sans-serif;
}

header, footer {
  text-align: center;
  padding: 1rem;
}

main {
  display: flex;
  justify-content: space-around;
  padding: 1rem;
}

.logo {
  max-width: 100px;
  height: auto;
  margin: 0 auto;
}

.placeholder {
  text-align: center;
}
</style>
