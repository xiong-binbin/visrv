<template>
  <div class="xml-tools">
    <div class="md-layout md-gutter md-alignment-center">
      <div class="md-layout-item">
        <md-field>
          <label>xml格式数据</label>
          <md-textarea class="xml-input" v-model="inputData"></md-textarea>
        </md-field>
      </div>
      <div class="md-layout-item md-size-5" style="padding-right: 0px; padding-left: 0px;">
        <md-button class="md-icon-button md-raised" v-on:click="onBuildClicked()">
          <md-icon>chevron_right</md-icon>
        </md-button>
      </div>
      <div class="md-layout-item">
        <md-field>
          <label>头文件</label>
          <md-textarea class="output-code" v-model="headerCode"></md-textarea>
        </md-field>
        <md-field>
          <label>源文件</label>
          <md-textarea class="output-code" v-model="sourceCode"></md-textarea>
        </md-field>
      </div>
    </div>

    <md-snackbar :md-position="'center'" :md-duration="2000" :md-active.sync="showSnackbar" md-persistent>
      <span>{{snackbarContent}}</span>
    </md-snackbar>
  </div>
</template>

<script>
  export default {
    name: 'tools',
    data () {
      return {
        inputData: null,
        headerCode: null,
        sourceCode: null,
        showSnackbar: false,
        snackbarContent: null,
        response: [],
        postData: {
          key: '1',
          value: '',
        },
        host: 'http://127.0.0.1:5000',
      }
    },
    methods: {
      onBuildClicked() {
        if(this.inputData == null) {
          this.snackbarContent = 'xml格式数据不能为空';
          this.showSnackbar = true;
          return;
        }
        this.postData.value = this.inputData;
        this.$axios.post(this.host + '/api/tools', this.postData)
        .then((response)=>{
          var jsonObj = JSON.parse(response.data);
          if(jsonObj['status'] == 'ok') {
            this.headerCode = jsonObj['value']['header'];
            this.sourceCode = jsonObj['value']['source'];
            this.snackbarContent = '成功!';
            this.showSnackbar = true;
          }
          else {
            this.headerCode = '';
            this.sourceCode = '';
            this.snackbarContent = jsonObj['status'];
            this.showSnackbar = true;
          }
        })
        .catch((error)=>{
          console.log(error);
        });
      }
    },
  }
</script>

<style lang="scss" scoped>
$input-heigth: 600px;

.xml-tools {
  padding: 50px 100px 0px 100px;
}

.xml-input {
  height: $input-heigth;
  max-height: $input-heigth;
}

.output-code {
  height: ($input-heigth - 40px)/2;
  max-height: ($input-heigth - 40px)/2;
}
</style>