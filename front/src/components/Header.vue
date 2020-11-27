<template>
  <header>
    <div class="search">
      <img v-on:click="send('/')" alt="logo" src="../assets/logo.png">
      <input type="search" placeholder="Busque por uma receita..."/>
      <button class="primary">Buscar</button>
    </div>
    <div>
        <button class="primary" v-on:click="send('login')">Fazer Login</button>
        <button class="primary raised" v-on:click="send('cadastrar')">Cadastrar</button>
    </div>
  </header>
</template>

<script>
import router from "../router";

export default {
  name: 'Header',
  props: {},
  methods: {
    send: function(component) {
      router.push(component)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

header {
  height: 10vh;
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  position: fixed;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  top: 0;
  background: #FFF;
  z-index: 9;
}

header img {
  margin-left: 1vw;
  height: 100%;
  cursor: pointer;
}

header button {
  margin-right: 10px;
}

header .search {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 100%;
}

header .search input {
  height: 50%;
  width: 30vw;
  margin: 0 3vw;
}
</style>
