<template>
  <div id="receitas">
      <h1 v-if="search">Suas buscas pelo termo {{search}} retornaram os seguintes resultados: </h1>
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
                    <div>
                        <md-button v-if="isLogged()" v-on:click="favorite(recipe._id.$oid)" class="md-icon-button">
                            <md-icon>favorite</md-icon>
                        </md-button>
                    </div>
                </md-card-actions>
            </md-card>
      </section>
      <md-snackbar md-position="left" :md-duration="2000" :md-active.sync="showSnackbar" md-persistent>
        <span>Receita adicionada as favoritas com sucesso</span>
      </md-snackbar>
  </div>
</template>

<script>
import router from "../router";
import recipes from "../mock/recipes.json";

export default {
  name: 'Receitas',
  data() {
    let tempRecipes = []

    if(this.$route.params?.search) {
      tempRecipes = recipes.filter((recipe) => {
        return recipe.nome.toLowerCase().indexOf(this.$route.params?.search) > -1;
      })
    } else {
      tempRecipes = recipes.splice(0, 20);
    }

    return {
      recipes: tempRecipes,
      showSnackbar: false,
      search: this.$route.params?.search || false
    }
  },
  methods: {
    seeRecipe: function(recipe) {
      router.push({ path: "receita/"+recipe._id, name: "Receita", params: recipe })
    },
    isLogged: function() {
        return window.localStorage.userId;
    },
    favorite: function(id) {
      this.showSnackbar = true;
      let favorites = window.localStorage.getItem("favorites");
      (!favorites) ? favorites = id : favorites += `,${id}`;
      window.localStorage.setItem("favorites", favorites);
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
