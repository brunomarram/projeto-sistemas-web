<template>
  <div>
    <div class="poster"></div>
    <div id="home">
      <img alt="logo" src="../assets/logo.png">
      <div>
        <h1>O que você quer cozinhar hoje?</h1>
        <div class="fieldset">
          <div class="field" v-for="(ingredient, key) in ingredients" v-bind:key="ingredient">
            <input :placeholder="placeholder(key)" type="text" />
            <button v-if="key !== 0" v-on:click="removeIngredient(key)" class="secondary">Remover</button>
            <button v-if="key === (ingredients.length - 1)" v-on:click="addIngredient" class="primary">Adicionar</button>
          </div>
        </div>
        <button class="primary receitar">Receitar!!</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {},
  data: function() {
    return {
      ingredients: [""]
    }
  },
  methods: {
    placeholder: function (key) {
      return "Ingrediente " + (key + 1);
    },
    addIngredient: function () {
      this.ingredients.push("")
    },
    removeIngredient: function (key) {
      this.ingredients.splice(key, 1);
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

.poster {
  height:50vh;
  background: url('/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 0.7;
}

#home {
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  animation: fadeIn 1s linear;
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 90vh;
}

#home button {
  margin-left: 10px;
}

#home .receitar {
  margin-top:20px; 
  font-size: 18px;
  width: 50%;
}

#home .field {
  margin-top: 15px;
  display: flex;
  justify-content: space-between;
}

#home .fieldset {
  height: 40vh;
  overflow: auto;
}
</style>
