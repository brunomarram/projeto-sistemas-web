<template>
  <div id="receita">
      <h1>{{recipe.nome}}</h1>
      <div v-for="(secao, key) in recipe.secao" v-bind:key="key">
          <h2>{{secao.nome}}</h2>
          <ul>
              <li v-for="item in secao.conteudo" v-bind:key="item">{{item}}</li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Receita',
  data() {
    return {
        recipe: this.$route.params
    }
  },
  methods: {
    isLogged: function() {
        return window.localStorage.userId;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

#receita {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: auto;
  min-height: 80vh;
}

#receita div {
    display: flex;
    flex-direction: column;
    align-items: left;
    width: 100%;
    text-align: left;
    margin-left: 2vw;
}

@media only screen and (max-width: 720px) {
  #receita {
    height: auto;
  }

  #receita img {
    width: 30%;
  }

  #receita div {
    width: 90%;
  }
}
</style>
