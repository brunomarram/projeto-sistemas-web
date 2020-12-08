<template>
  <div id="register">
    <img alt="logo" src="../assets/logo.png">
    <h1>Que tal fazer seu cadastro?</h1>
    <div class="form">
      <input type="text" placeholder="Nome"/>
      <input type="email" placeholder="E-mail"/>
      <input type="password" placeholder="Senha"/>
      <input type="password" placeholder="Confirmar senha"/>
      <button class="primary" v-on:click="submit()">Cadastrar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  methods: {
    submit: function() {
      // Fazer login do usuário
      window.localStorage.setItem("userId", "id-fake");
      window.localStorage.setItem("username", "Bruno Marra");
      window.location.href = "/"
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#register img {
  margin-top: 1vh;
  height: 20%;
}

#register {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 90vh
}

#register .form {
  display: flex;
  flex-direction: column;
  width: 30%;
}

#register .form input {
  margin: 2vh 0
}

#register input {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  border: 0;
  padding: 20px;
  border-radius: 20px;
}

@media only screen and (max-width: 720px) {
  #register {
    height: auto;
  }

  #register img {
    width: 30%;
  }

  #register .form {
    width: 90%;
  }
}
</style>
