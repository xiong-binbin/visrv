<template>
  <div class="home">
    <div class="article">
      <h1 class="article-title">文档</h1>
      <div class="article-list md-layout md-gutter">
        <div class="md-layout-item">
          <md-list v-for="item in article.list_0" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list v-for="item in article.list_1" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list v-for="item in article.list_2" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list v-for="item in article.list_3" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list v-for="item in article.list_4" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list v-for="item in article.list_5" :key="item.id">
            <md-list-item v-bind:href="item.link" target="_blank">{{item.title}}</md-list-item>
          </md-list>
        </div>
      </div>
    </div>
    <div class="other">
      <h1 class="other-title">其它</h1>
      <div class="other-list md-layout md-gutter">
        <div class="md-layout-item">
          <md-list>
            <md-list-item href="/project" target="_blank">项目进度</md-list-item>
          </md-list>
        </div>
        <div class="md-layout-item">
          <md-list>
            <md-list-item href="/tools" target="_blank">xml组装工具</md-list-item>
          </md-list>          
        </div>
        <div class="md-layout-item"></div>
        <div class="md-layout-item"></div>
        <div class="md-layout-item"></div>
        <div class="md-layout-item"></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Index',
    data () {
      return {
        host: 'http://127.0.0.1:5000',
        article: [],
      }
    },
    created: function() {
      this.$axios.get(this.host + '/api/page?name=index')
      .then((response)=>{
        var jsonObj = JSON.parse(response.data);
        this.article = jsonObj['article'];
      })
      .catch((error)=>{
        console.log(error);
      });
    },
  }
</script>

<style lang="scss" scoped>
h1 {
  font-size: 32px;
  padding-top: 20px;
  padding-bottom: 20px;
}

.home {
  padding: 50px 100px 50px 100px;
}

.other {
  margin-top: 160px;
}

.md-list {
  background-color: rgba(0, 0, 0, 0);
}

.md-layout-item {
  padding-left: 0px !important;
  padding-right: 0px !important;
}
</style> 


