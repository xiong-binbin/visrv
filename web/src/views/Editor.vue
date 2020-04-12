<template>
  <div>
    <md-tabs md-alignment="centered" v-on:md-changed="switchTabs">
      <md-tab id="tab-edit" md-label="编辑">
        <div ref="editor" class="wangeditor"></div>
      </md-tab>
      <md-tab id="tab-pdf" md-label="PDF">
        <div class="pdf-upload">
          <md-field>
            <label>请选择上传的PDF文档</label>
            <md-file v-on:md-change="changePDF"/>
          </md-field>
        </div>
      </md-tab>
    </md-tabs>
    
    <div class="editor-sort md-layout md-gutter">
      <div class="md-layout-item">
        <md-autocomplete v-if="action=='add'" v-model="articleSort" :md-options="articleSortList">
          <label>类别</label>
        </md-autocomplete>
      </div>
      <div class="md-layout-item">
        <md-field v-if="action=='add'">
          <label>标题</label>
          <md-input v-model="articleTitle"></md-input>
        </md-field>
      </div>
    </div>

    <div class="editor-operate md-layout md-gutter">
      <div class="md-layout-item"></div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item">
        <md-button class="md-raised md-primary" v-on:click="submitDocument">提交</md-button>
      </div>
      <div class="md-layout-item">
        <md-button class="md-raised md-primary" v-on:click="submitDocument">取消</md-button>
      </div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item"></div>
    </div>

    <md-snackbar :md-position="'center'" :md-duration="2000" :md-active.sync="showSnackbar" md-persistent>
      <span>{{snackbarContent}}</span>
    </md-snackbar>
  </div>
</template>

<script>
  import E from 'wangeditor';

  export default {
    name: 'Editor',
    data() {
      return {
        menus: [],
        action: null,
        sIndex: null,
        sId: null,
        activeTab: null,
        showSnackbar: false,
        snackbarContent: null,
        pdfName: null,
        editorContent: null,
        articleSort: null,
        articleSortList: [],
        articleTitle: null,
        documentInfo: {
          key: '',
          value: '',
        },
        articleInfo: {
          key: '',
          value: '',          
        },
        addMenu: {
          index: null, name: null, active: false, items: [
            {id: 0, title: null, link: null, active: false},
          ],
        },
        addItem: {id: null, title: null, link: null, active: false},
        host: 'http://127.0.0.1:5000',
      }
    },
    methods: { 
      switchTabs(activeTab) {
        this.activeTab = activeTab;
      },

      changePDF(e) {
        var param = new FormData();
        param.append('file', e[0]);
        this.$axios.post(this.host + '/upload/pdf', param)
        .then((response)=>{
          this.pdfName = response.data;
          this.snackbarContent = "pdf文件上传成功！";
          this.showSnackbar = true;
        })
        .catch((error)=>{
          console.log(error);
        });
      },

      submitDocument() {
        var nowDateStr = this.getNowFormatDate();
        if(this.articleSort == null || this.articleTitle == null) {
          this.snackbarContent = "类别或标题不能为空，提交失败！";
          this.showSnackbar = true;
          return;
        }
        if((this.activeTab == "tab-edit" && this.editorContent == null) || (this.activeTab == "tab-pdf" && this.pdfName == null)) {
          this.snackbarContent = "填入内容不能为空，提交失败！";
          this.showSnackbar = true;
          return;
        }
        if(this.action == "add") {
          this.documentInfo.key = nowDateStr;
          if(this.activeTab == "tab-edit") {
            this.documentInfo.value = this.editorContent;
          }
          else if(this.activeTab == "tab-pdf") {
            this.documentInfo.value = '<iframe id="pdf-frame" src="' + this.host + '/static/pdf/'+this.pdfName+'"></iframe>';
          }
          for(var i=0; i<this.menus.length; i++)
          {
            if(this.menus[i].name == this.articleSort) {
              this.addItem.id = this.menus[i].items.length;
              this.addItem.title = this.articleTitle;
              this.addItem.link = '/api/document?id='+nowDateStr;
              this.articleInfo.value.menus[i].items.push(this.addItem);
              break;
            }
          }
          if(i == this.menus.length) {
            this.addMenu.index = this.menus.length;
            this.addMenu.name = this.articleSort;
            this.addMenu.items[0].title = this.articleTitle;
            this.addMenu.items[0].link = '/api/document?id='+nowDateStr;
            this.articleInfo.value.menus.push(this.addMenu);
          }
        }
        else if(this.action == "edit") {
          if(this.menus[this.sIndex].items[this.sId].link == "") {
            this.documentInfo.key = nowDateStr;
            this.articleInfo.value.menus[this.sIndex].items[this.sId].link = '/api/document?id='+nowDateStr;
          }
          else {
            this.documentInfo.key = this.menus[this.sIndex].items[this.sId].link.split('id=')[1];
          }
          
          if(this.activeTab == "tab-edit") {
            this.documentInfo.value = this.editorContent;
          }
          else if(this.activeTab == "tab-pdf") {
            this.documentInfo.value = '<iframe id="pdf-frame" src="' + this.host + '/static/pdf/'+this.pdfName+'"></iframe>';
          }
        }

        this.$axios.post(this.host + '/api/article', this.articleInfo)
        .then((response)=>{
          console.log(response);
        })
        .catch((error)=>{
          console.log(error);
        });

        this.$axios.post(this.host + '/api/document', this.documentInfo)
        .then((response)=>{
          this.snackbarContent = "提交成功！";
          this.showSnackbar = true;
        })
        .catch((error)=>{
          console.log(error);
        });
      },
    },
    mounted() {
      var editor = new E(this.$refs.editor);
      editor.customConfig.uploadImgShowBase64 = true;
      editor.customConfig.onchange = (html) => {
        this.editorContent = html
      };
      editor.create();

      var id       = this.$route.query.id;
      var selected = this.$route.query.selected;
      this.action  = this.$route.query.action;
      this.$axios.get(this.host + '/api/article?id='+id)
      .then((response)=>{
        var jsonObj = JSON.parse(response.data);
        this.articleInfo.key = id;
        this.articleInfo.value = jsonObj;
        this.menus = jsonObj['menus'];
        for(var i=0; i<this.menus.length; i++) 
        {
          this.articleSortList.push(this.menus[i].name);
        }

        if(this.action == "edit" && selected != null) {
          this.sIndex = parseInt(selected/100);
          this.sId    = parseInt(selected%100);
          this.articleSort = this.menus[this.sIndex].name;
          this.articleTitle = this.menus[this.sIndex].items[this.sId].title;
          if(this.menus[this.sIndex].items[this.sId].link != "") {
            this.$axios.get(this.host + this.menus[this.sIndex].items[this.sId].link)
            .then((response)=>{
              if(response.data.search("pdf-frame") == -1) {
                editor.txt.html(response.data);
                this.editorContent = response.data;
              };
            })
            .catch((error)=>{
              console.log(error);
            });
          };
        };
      })
      .catch((error)=>{
        console.log(error);
      });
    }
  }
</script>

<style lang="scss" scoped>
.md-tabs {
  margin: 0px 50px 0px 50px;
}
.editor-sort {
  margin: 50px 50px 50px 50px;
}
.editor-operate {
  margin: 180px 50px 80px 50px;
}

.pdf-upload {
  min-height: 200px;
  padding-top: 120px;
}
</style>

<style>
.w-e-text-container{
  height: 600px !important;
}

.md-content.md-theme-default {
  background-color: rgba(0, 0, 0, 0);
}

.md-tabs.md-theme-default .md-tabs-navigation {
  background-color: rgba(0, 0, 0, 0);
}
</style>

