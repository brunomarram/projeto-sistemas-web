<template>
  <div id="receitas">
      <h1 v-if="search">Suas buscas pelo termo {{search}} retornaram os seguintes resultados: </h1>
      <section>
            <md-card v-for="recipe in recipes" v-bind:key="recipe._id">
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
                        <md-button v-if="isLogged()" class="md-icon-button">
                            <md-icon>favorite</md-icon>
                        </md-button>
                    </div>
                </md-card-actions>
            </md-card>
      </section>
  </div>
</template>

<script>
import router from "../router";

export default {
  name: 'Receitas',
  data() {
    return {
      search: this.$route.params?.search || false,
      recipes: [
        {
            "_id": "5744eff20ca2b5c745a48",
            "nome": "Brownie de Chocolate com Gengibre",
            "secao": [
                {
                "nome": " Ingredientes",
                "conteudo": [
                    "50 g farinha de milho fina",
                    "10 g de cacau em pó",
                    "250 g de chocolate meio amargo",
                    "200 g de manteiga sem sal cortada em cubos",
                    "20 ml de suco de gengibre",
                    "5 ovos",
                    "200 g de açúcar",
                    "1 colher (chá) de fermento em pó",
                    "100 g de nozes picadas grosseiramente",
                    " "
                ]
                },
                {
                "nome": " Modo de Preparo",
                "conteudo": [
                    "1 - Coloque numa tigela a farinha de milho fina e o cacau em pó.",
                    "2 - Misture e reserve.",
                    "3 - Numa panela, em banho-maria, derreta o chocolate meio amargo picado com a manteiga sem sal cortada em cubos.",
                    "4 - Retire do fogo.",
                    "5 - Adicione o suco de gengibre e misture.",
                    "6 - Acrescente a mistura de farinha com cacau em pó (reservada acima). Misture bem e reserve.",
                    "7 - Numa batedeira, coloque os ovos e o açúcar. Bata bem até dobrar de volume.",
                    "8 - Com a batedeira ainda ligada, adicione o fermento em pó e bata até misturar.",
                    "9 - Desligue a batedeira. Acrescente a mistura de chocolate (reservada acima) e as nozes picadas. Misture.",
                    "10 - Transfira a massa para uma assadeira retangular (18 cm X 30 cm) untada e forrada com papel manteiga.",
                    "11 - Leve para assar em forno médio pré-aquecido a 180°C por +/- 40 minutos.",
                    "12 - Retire do forno.",
                    "13 - Cubra o brownie com papel manteiga.",
                    "14 - Coloque outra assadeira do mesmo tamanho pressionando levemente o brownie para que fique mais compacto e úmido",
                    "15 - Deixe por +/- 4 horas na geladeira.",
                    "16 - Retire a assadeira de cima do brownie, desenforme, corte em quadrados e sirva em seguida.",
                    " "
                ]
                },
                {
                "nome": " Outras informações",
                "conteudo": [
                    "Rendimento: 20 porções "
                ]
                }
            ]
        }, {
            "_id": "5744eff20ca7832b5c745a48",
            "nome": "Brownie de Chocolate com Gengibre",
            "secao": [
                {
                "nome": " Ingredientes",
                "conteudo": [
                    "50 g farinha de milho fina",
                    "10 g de cacau em pó",
                    "250 g de chocolate meio amargo",
                    "200 g de manteiga sem sal cortada em cubos",
                    "20 ml de suco de gengibre",
                    "5 ovos",
                    "200 g de açúcar",
                    "1 colher (chá) de fermento em pó",
                    "100 g de nozes picadas grosseiramente",
                    " "
                ]
                },
                {
                "nome": " Modo de Preparo",
                "conteudo": [
                    "1 - Coloque numa tigela a farinha de milho fina e o cacau em pó.",
                    "2 - Misture e reserve.",
                    "3 - Numa panela, em banho-maria, derreta o chocolate meio amargo picado com a manteiga sem sal cortada em cubos.",
                    "4 - Retire do fogo.",
                    "5 - Adicione o suco de gengibre e misture.",
                    "6 - Acrescente a mistura de farinha com cacau em pó (reservada acima). Misture bem e reserve.",
                    "7 - Numa batedeira, coloque os ovos e o açúcar. Bata bem até dobrar de volume.",
                    "8 - Com a batedeira ainda ligada, adicione o fermento em pó e bata até misturar.",
                    "9 - Desligue a batedeira. Acrescente a mistura de chocolate (reservada acima) e as nozes picadas. Misture.",
                    "10 - Transfira a massa para uma assadeira retangular (18 cm X 30 cm) untada e forrada com papel manteiga.",
                    "11 - Leve para assar em forno médio pré-aquecido a 180°C por +/- 40 minutos.",
                    "12 - Retire do forno.",
                    "13 - Cubra o brownie com papel manteiga.",
                    "14 - Coloque outra assadeira do mesmo tamanho pressionando levemente o brownie para que fique mais compacto e úmido",
                    "15 - Deixe por +/- 4 horas na geladeira.",
                    "16 - Retire a assadeira de cima do brownie, desenforme, corte em quadrados e sirva em seguida.",
                    " "
                ]
                },
                {
                "nome": " Outras informações",
                "conteudo": [
                    "Rendimento: 20 porções "
                ]
                }
            ]
        }
      ]
    }
  },
  methods: {
    seeRecipe: function(recipe) {
      router.push({ path: "receita/"+recipe._id, name: "Receita", params: recipe })
    },
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

#receitas img {
  margin-top: 4vh;
  height: 20%;
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
