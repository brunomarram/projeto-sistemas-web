<template>
  <div id="register">
    <img alt="logo" src="../assets/logo.png">
    <h1>Que tal fazer seu cadastro?</h1>
    <form>
      <input type="text" placeholder="Nome"/>
      <input type="email" placeholder="E-mail"/>
      <input type="password" placeholder="Senha"/>
      <input type="password" placeholder="Confirmar senha"/>
      <button class="primary">Cadastrar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Register',
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
  height: 70vh
}

#register form {
  display: flex;
  flex-direction: column;
  width: 30%;
}

#register form input {
  margin: 2vh 0
}
</style>
