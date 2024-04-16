<template>
  <div class="map">
    <h3>Map</h3>
    <div id="map"></div>
  </div>
</template>

<script>
/* global google */
export default {
  name: 'MapComponent',
  props: {
    directionsService: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      map: null,
      directionsRenderer: null,
    };
  },
  mounted() {
    // Ensure the Google Maps API is available
    if (window.google) {
      this.initMap();
    } else {
      window.addEventListener('googleMapsApiLoaded', this.initMap);
    }
  },
  methods: {
    initMap() {
      if (this.directionsService) {
        const mapOptions = {
            zoom: 8,
            center: { lat: 39.9607, lng: -75.6055 }, // Default center
        };
        this.map = new google.maps.Map(document.getElementById('map'), mapOptions);
        this.directionsRenderer = new google.maps.DirectionsRenderer();
        this.directionsRenderer.setMap(this.map);
      } else {
        console.warn('Google Maps API key or directionsService is missing.');
      }
    },
    renderDirections(directions) {
      this.directionsRenderer.setDirections(directions);
    },
  },
};
</script>

<style>
#map {
  border: 2px solid #ccc;
  height: 400px; /* Example height */
  width: 300px;  /* Example width */
}
</style>