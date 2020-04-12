<template>
  <div class="project">
    <md-dialog :md-active.sync="moreActive">
      <md-dialog-title>{{projects[moreIndex].title}}</md-dialog-title>
      <md-field>
        <label>需求</label>
        <md-textarea v-model="projects[moreIndex].requirements"></md-textarea>
      </md-field>
    </md-dialog>

    <md-table v-model="projects" md-card>
      <md-table-toolbar>
        <h1 class="md-title">定制任务</h1>
      </md-table-toolbar>
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="姓名">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="项目">{{ item.title }}</md-table-cell>
        <md-table-cell md-label="需求">
          {{ item.summary }}
          <md-button class="md-icon-button" v-on:click="onMoreClicked(item.id)">
            <md-icon>more_horiz</md-icon>
          </md-button>
        </md-table-cell>
        <md-table-cell md-label="开发周期">
          <md-tooltip md-direction="left">2019-12-01</md-tooltip>
          <md-progress-bar md-mode="determinate" :md-value="69"></md-progress-bar>
          <md-tooltip md-direction="right">2019-12-30</md-tooltip>
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
  export default {
    name: 'Project',
    data: () => ({
      moreActive: false,
      moreIndex: 0,
      projects: [
        {
          id: 0,
          name: 'jack',
          title: '拥有微信、QQ 两大平台，腾讯为何还要推出全新“朋友”',
          summary: '社交领域一直是互联网公司竞争的一个重头戏',
          requirements: '社交领域一直是互联网公司竞争的一个重头戏，牢牢稳坐第一把交椅的是拥有微信、QQ两大平台的腾讯。',
          date: '2020-01-01'
        },
        {
          id: 1,
          name: 'jack',
          title: 'a project',
          summary: 'summary',
          requirements: 'requirements',
          date: '2020-01-01'
        },
        {
          id: 2,
          name: 'jack',
          title: 'a project',
          summary: 'summary',
          requirements: 'requirements',
          date: '2020-01-01'
        },
        {
          id: 3,
          name: 'jack',
          title: 'a project',
          summary: 'summary',
          requirements: 'requirements',
          date: '2020-01-01'
        },
        {
          id: 4,
          name: 'jack',
          title: 'a project',
          summary: 'summary',
          requirements: 'requirements',
          date: '2020-01-01'
        }
      ]
    }),
    methods: {
      onMoreClicked(i) {
        this.moreActive = true;
        this.moreIndex = i;
      }
    },
  }
</script>

<style lang="scss" scoped>
.project {
    margin: 0 100px;
    padding: 20px 20px;
}

.md-dialog {
  min-width: 1000px;
  padding: 20px 20px;
}

.md-progress-bar {
  min-width: 300px;
}
</style>