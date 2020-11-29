<template>
  <div id="login">
    <img alt="logo" src="../assets/logo.png">
    <h1>Faça Login para continuar</h1>
    <div>
      <input v-model="email" type="email" placeholder="E-mail"/>
      <input v-model="password" type="password" placeholder="Senha"/>
      <button v-on:click="submit" class="primary">Acessar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    submit: function() {
      // Fazer login do usuário
      window.localStorage.setItem("userId", "id-fake");
      window.localStorage.setItem("username", "Usuário");
      window.location.href = "/"
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#login img {
  margin-top: 4vh;
  height: 20%;
}

#login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 70vh
}

#login div {
  display: flex;
  flex-direction: column;
  width: 30%;
}

#login div input {
  margin: 3vh 0
}

#login input {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  border: 0;
  padding: 20px;
  border-radius: 20px;
}

@media only screen and (max-width: 720px) {
  #login {
    height: auto;
  }

  #login img {
    width: 30%;
  }

  #login div {
    width: 90%;
  }
}
</style>
