<template>
  <div id="home">
    <img alt="logo" src="../assets/logo.png">
    <h1>As melhores receitas você encontra aqui</h1>
    <div class="fieldset">
      <div class="field" v-for="(ingredient, key) in ingredients" v-bind:key="ingredient">
        <input :placeholder="placeholder(key)" type="text" />
        <button v-if="key !== 0" class="secondary">Remover</button>
        <button class="primary">Adicionar</button>
      </div>
    </div>
    <button class="primary receitar">Receitar!!</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {},
  data: function() {
    return {
      ingredients: [
        { text: 'teset' },
        { text: 'teset' },
        { text: 'teset' },
        { text: 'teset' },
        { text: 'teset' }
      ]
    }
  },
  methods: {
    placeholder: (key) => {
      return "Ingrediente " + (key + 1);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@keyframes fadeIn {
    from { opacity: 0; height: 0; }
    to { opacity: 1; height: auto; }
}

#home {
  animation: fadeIn 2s linear;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#home button {
  margin-left: 10px;
}

#home .receitar {
  margin-top:20px; 
  width: 20%;
  font-size: 18px;
}

#home .field {
  margin-top: 15px;
  display: flex;
  justify-content: space-between;
}

#home .fieldset {
  max-height: 20vh;
  overflow: auto;
  width: 25%;
}
</style>
