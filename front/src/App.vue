<template>
  <div>
    <Header/>
    <div id="app">
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer
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



button.primary, a.primary {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  background: #072047;
  color: #fff;
  border: 0;
  padding: 20px;
  border-radius: 30px;
  cursor: pointer;
  text-decoration: none;
}

button.secondary, a.secondary {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  background: #440a2d;
  color: #fff;
  border: 0;
  padding: 20px;
  border-radius: 30px;
  cursor: pointer;
  text-decoration: none;
}

button.primary.raised, a.primary.raised {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
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
