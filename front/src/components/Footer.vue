<template>
  <footer>
    <div class="produced">
        <h2>Produzido pela: </h2>
        <img src="../assets/ufv.png" alt=""/>
    </div>
    <div class="students">
        <h2>Alunos: </h2>
        <ul>
            <li>Bruno Marra</li>
            <li>Maria Dalila</li>
            <li>Vinícius Gabriel</li>
        </ul>
    </div>
  </footer>
</template>

<script>
import router from "../router";

export default {
  name: 'Footer',
  props: {},
  methods: {
    send: function(component) {
      router.push(component)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

footer {
  height: 20vh;
  -webkit-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 4px 30px 0px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: space-around;
}

footer .produced img {
  height: 50%;
}

footer .produced {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

footer h2 {
    text-align: left;
}

footer ul {
    list-style-type: none;
    text-align: left;
    padding: 0;
}
</style>
