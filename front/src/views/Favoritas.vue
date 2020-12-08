<template>
  <div id="receitas">
      <h1>Minhas receitas favoritas: </h1>
      <section>
            <md-card v-for="recipe in recipes" v-bind:key="recipe._id.$oid">
                <md-card-area>
                    <md-card-header>
                    <div class="md-title">{{recipe.nome}}</div>
                    <div class="md-subhead">{{recipe.secao[0].conteudo.length}} Ingredientes</div>
                    </md-card-header>

                    <md-card-content>
                        <ul>
                            <li v-for="ingredient in recipe.secao[0].conteudo" v-bind:key="ingredient">
                                {{ingredient}}
                            </li>
                        </ul>
                    </md-card-content>
                </md-card-area>

                <md-card-actions>
                    <md-button class="md-primary md-raised" v-on:click="seeRecipe(recipe)">
                        Ver receita completa
                    </md-button>
                </md-card-actions>
            </md-card>
      </section>
  </div>
</template>

<script>
import router from "../router";
import recipes from "../mock/recipes.json";

export default {
  name: 'Receitas',
  data() {
    const favorites = window.localStorage.getItem("favorites");
    const ids = favorites.split(",");
    return { recipes: recipes.filter((recipe) => ids.indexOf(recipe._id.$oid) > -1) }
  },
  methods: {
    seeRecipe: function(recipe) {
      router.push({ path: "receita/"+recipe._id, name: "Receita", params: recipe })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

#receitas img {
  margin-top: 4vh;
  height: 20%;
}

#receitas .md-title {
  height: 100px;
}

#receitas .md-card-content {
  height: 200px;
  overflow: auto;
}

#receitas {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: auto;
  min-height: 80vh;
}

#receitas section {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
}

#receitas section .md-card:nth-child(n) {
    width: 20%;
    margin: 2.5%;
    animation: fadeIn 1s;
}

#receitas section .md-card li {
    text-align: left;
}

#receitas .md-card-actions {
    justify-content: space-between;
}


@media only screen and (max-width: 720px) {
  #receitas {
    height: auto;
  }

  #receitas img {
    width: 30%;
  }

  #receitas div {
    width: 90%;
  }
}
</style>
