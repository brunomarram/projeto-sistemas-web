<template>
  <div id="login">
    <img alt="logo" src="../assets/logo.png">
    <h1>Faça Login para continuar</h1>
    <form>
      <input type="email" placeholder="E-mail"/>
      <input type="password" placeholder="Senha"/>
      <button class="primary">Acessar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
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

#login form {
  display: flex;
  flex-direction: column;
  width: 30%;
}

#login form input {
  margin: 3vh 0
}

@media only screen and (max-width: 720px) {
  #login {
    height: auto;
  }

  #login img {
    width: 30%;
  }

  #login form {
    width: 90%;
  }
}
</style>
