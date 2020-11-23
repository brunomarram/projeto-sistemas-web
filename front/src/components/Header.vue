<template>
  <header>
    <img alt="logo" src="../assets/logo.png">
    <div>
        <button class="primary">Fazer Login</button>
        <button class="primary raised">Cadastrar</button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {}
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
}

header img {
    height: 100%;
}

header button {
    margin-right: 10px;
}
</style>
