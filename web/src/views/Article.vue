<template>
  <div class="article">
    <md-toolbar md-elevation="1">
      <div class="md-toolbar-row">
        <div class="md-toolbar-section-start">
          <h3 class="md-title">Hikvision</h3>
        </div>
      </div>
    </md-toolbar>
    <div class="drawer-menu">
      <md-list :md-expand-single="expandSingle">
        <md-list-item md-expand v-for="menu in menus" :key="menu.index" v-bind:md-expanded.sync="menu.active">
          <md-icon>{{icon[menu.index]}}</md-icon>
          <span class="md-list-item-text">{{menu.name}}</span>
          <md-list slot="md-expand">
            <md-list-item class="md-inset" v-for="item in menu.items" :key="item.id" v-on:click="onMenuClicked(menu.index, item.id)" v-bind:class="{'list-item-active': item.active}">
              {{item.title}}
            </md-list-item>
          </md-list>
        </md-list-item>
      </md-list>
    </div>
    <md-speed-dial md-direction="top">
      <md-speed-dial-target class="md-primary">
        <md-icon>add</md-icon>
      </md-speed-dial-target>
      <md-speed-dial-content>
        <md-button class="md-icon-button" v-on:click="onAddClicked()">
          <md-icon>add</md-icon>
        </md-button>
        <md-button class="md-icon-button" v-on:click="onEditClicked()">
          <md-icon>edit</md-icon>
        </md-button>
        <md-button class="md-icon-button" v-on:click="onDeleteClicked()">
          <md-icon>delete</md-icon>
        </md-button>
      </md-speed-dial-content>
    </md-speed-dial>
    <div class="doc-content">
      <div v-html="content" style="height: 100%"></div> 
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Article',
    data() {
      return {
        expandSingle: false,
        icon: ['whatshot', 'layers', 'description', 'storage', 'flash_on', 'pages', 'cached', 'filter_drama'],
        menus: [],
        sIndex: null,
        sId: null,
        content: null,
        articleInfo: {
          key: '',
          value: '',          
        },
        host: 'http://127.0.0.1:5000',
      }
    },
    methods: {
      onMenuClicked(index, id) {
        if(this.sIndex != null) {
          this.menus[this.sIndex].items[this.sId].active = false;
        }
        this.menus[index].items[id].active = true;
        this.sIndex = index;
        this.sId = id;
        if(this.menus[index].items[id].link != "") {
          this.$axios.get(this.host + this.menus[index].items[id].link)
          .then((response)=>{
            this.content = response.data;
          })
          .catch((error)=>{
            console.log(error);
          });
        }
        else {
          this.content = "";
        }
      },
      onAddClicked() {
        var id = this.$route.query.id;
        window.open('/editor?action=add&id='+id, '_blank');
      },
      onEditClicked() {
        if(this.sIndex == null) {
          return;
        }
        var id = this.$route.query.id;
        var selected = this.sIndex*100 + this.sId;
        window.open('/editor?action=edit&id='+id+'&selected='+selected, '_blank');
      },
      onDeleteClicked() {
        if(this.sIndex == null) {
          return;
        }
        else if(this.sId == 0 && this.menus[this.sIndex].items.length == 1) {
          this.articleInfo.value.menus.splice(this.sIndex, 1);
        }
        else {
          this.articleInfo.value.menus[this.sIndex].items.splice(this.sId, 1);
          for(var i=0; i<this.articleInfo.value.menus[this.sIndex].items.length; i++)
          {
            this.articleInfo.value.menus[this.sIndex].items[i].id = i;
          }
          for(var i=0; i<this.articleInfo.value.menus.length; i++)
          {
            this.articleInfo.value.menus[i].active = false;
          }
        }
        this.$axios.post(this.host + '/api/article', this.articleInfo)
        .then((response)=>{
          console.log(response);
        })
        .catch((error)=>{
          console.log(error);
        });
        location.reload();
      },
    },
    created() {
      var id = this.$route.query.id;
      var selected = this.$route.query.selected;
      this.$axios.get(this.host + '/api/article?id=' + id)
      .then((response)=>{
        var jsonObj = JSON.parse(response.data);
        this.articleInfo.key = id;
        this.articleInfo.value = jsonObj;
        this.menus = jsonObj['menus'];
        if(selected != null) {
          this.sIndex = parseInt(selected/100);
          this.sId    = parseInt(selected%100);
          this.menus[this.sIndex].active = true;
          this.menus[this.sIndex].items[this.sId].active = true;
          if(this.menus[this.sIndex].items[this.sId].link != "") {
            this.$axios.get(this.host + this.menus[this.sIndex].items[this.sId].link)
            .then((response)=>{
              this.content = response.data;
            })
            .catch((error)=>{
              console.log(error);
            });
          }
        }
      })
      .catch((error)=>{
        console.log(error);
      });
    },
  }
</script>

<style lang="scss" scoped>
$drawer-width: 300px;

p{
  word-wrap: break-word;
  word-break: break-all;
  overflow: hidden;
}

.article {
  position: relative;
  width: 100%;
  height: 100%;
}

.drawer-menu {
  position: absolute;
  width: $drawer-width;
  height: auto;
}

.md-list {
  background-color: rgba(0, 0, 0, 0);
}

.doc-content {
  height: calc(100% - 80px);
  margin-left: $drawer-width;
  margin-right: 180px;
  padding: 10px 30px 0px 30px;
}

.md-speed-dial {
  position: fixed;
  bottom: 40px;
  right: 40px;
}

.list-item-active {
  background-color: #595959;
}
</style>

<style>
.md-list-item-expand {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

#pdf-frame {
  width: 100%;
  height: 100%;
}
</style>
