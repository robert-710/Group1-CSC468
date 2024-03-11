<template>
  <div id="app">
    <header>
      <img :src="logo" alt="Scenic Navigation App Logo" class="logo">
      <h1>Scenic Navigation App</h1>
    </header>
    <main>
      <MapComponent />
      <RouteSuggestionsComponent />
    </main>
  </div>
</template>

<script>
import MapComponent from './components/MapComponent.vue'
import RouteSuggestionsComponent from './components/RouteSuggestionsComponent.vue'

export default {
  name: 'App',
  data() {
    return {
      logo: require('@/assets/logo.png')
    }
  },
  components: {
    MapComponent,
    RouteSuggestionsComponent
  }
}
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
</style>
