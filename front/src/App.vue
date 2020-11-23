<template>
  <Header />
  <Home />
</template>

<script>
import Home from "./components/Home.vue";
import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {
    Home,
    Header,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10vh;
}

body {
  margin: 0;
  background: #edf1f1;
}

input {
  border: 1px solid #072047;
  padding: 20px;
  border-radius: 20px;
}

input:focus {
  border: 1px solid #072047;
  padding: 20px;
  border-radius: 20px;
}

button.primary {
  background: #072047;
  color: #fff;
  border: 0;
  padding: 20px;
  border-radius: 30px;
  cursor: pointer;
}

button.secondary {
  background: #440a2d;
  color: #fff;
  border: 0;
  padding: 20px;
  border-radius: 30px;
  cursor: pointer;
}

button.primary.raised {
  background: #fff;
  color: #072047;
  border: 2px solid #072047;
}

/* total width */
*::-webkit-scrollbar {
  background-color: #fff;
  border-radius: 16px;
  width: 16px;
}

/* background of the scrollbar except button or resizer */
*::-webkit-scrollbar-track {
  /* background-color: #fff; */
}

/* scrollbar itself */
*::-webkit-scrollbar-thumb {
  background-color: #babac0;
  border-radius: 16px;
  border: 4px solid #fff;
}

/* set button(top and bottom of the scrollbar) */
*::-webkit-scrollbar-button {
  display: none;
}
</style>
