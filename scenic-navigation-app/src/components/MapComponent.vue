<template>
  <div class="map">
    <h3>Map</h3>
    <p>This is where the interactive map will be displayed.</p>
  </div>
</template>

<script>
export default {
  name: 'MapComponent',
  data() {
    return {
      map: null,
      directionsRenderer: null,
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      fetch('/api/key')
        .then(response => response.text())
        .then(apiKey => {
          const mapOptions = {
            zoom: 8,
            center: { lat: 39.9607, lng: -75.6055 }, // Default center
          };
          this.map = new google.maps.Map(document.getElementById('map'), mapOptions);
          this.directionsRenderer = new google.maps.DirectionsRenderer();
          this.directionsRenderer.setMap(this.map);
        })
        .catch(error => console.error('Error fetching API key:', error));
    },
    renderDirections(directions) {
      this.directionsRenderer.setDirections(directions);
    },
  },
};
</script>

<style>
.placeholder {
  border: 2px solid #ccc;
  margin: 10px;
  padding: 20px;
  text-align: center;
}
</style>
