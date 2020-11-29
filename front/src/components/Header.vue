<template>
  <header>
    <div class="search">
      <img v-on:click="send('/')" alt="logo" src="../assets/logo.png">
      <input type="search" placeholder="Busque por uma receita..."/>
      <button class="primary">Buscar</button>
    </div>
    <div v-if="user" class="user">
      <md-icon>account_circle</md-icon>
      <h3>{{getUsername()}}</h3>
      <md-button class="md-icon-button" v-on:click="logout">
        <md-icon>exit_to_app</md-icon>
      </md-button>
    </div>
    <div v-else>
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
  data() {
    return {
      user: window.localStorage.userId
    }
  },
  methods: {
    send: function(component) {
      router.push(component)
    },
    getUsername: function() {
      return window.localStorage.getItem("username");
    },
    logout: function() {
      window.localStorage.clear();
      window.location.href = "/";
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

header .user {
  display: flex;
  align-items: center;
}

header .user h3 {
  margin-left: 1vw;
}

header input {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  border: 0;
  padding: 20px;
  border-radius: 20px;
}

@media only screen and (max-width: 720px) {
  header .search input {
    width: 100%;
  }
  
  header div:last-child {
    display: none;
  }
}
</style>
