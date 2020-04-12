/*jshint esversion: 6 */
import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/views/Index';
import Help from '@/views/Help';
import Article from '@/views/Article';
import Editor from '@/views/Editor';
import Project from '@/views/Project';
import Tools from '@/views/Tools';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
    },
    {
      path: '/help',
      name: 'Help',
      component: Help,
    },
    {
      path: '/article',
      name: 'Article',
      component: Article,
    },
    {
      path: '/editor',
      name: 'Editor',
      component: Editor,
    },
    {
      path: '/project',
      name: 'Project',
      component: Project,
    },
    {
      path: '/tools',
      name: 'Tools',
      component: Tools,
    },
  ]
});

