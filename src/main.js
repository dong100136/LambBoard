/*
 * @Author: your name
 * @Date: 2020-12-23 01:30:35
 * @LastEditTime: 2021-01-23 14:31:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/src/main.js
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'vuetify/dist/vuetify.min.css'
import vuetify from './plugins/vuetify';
import axios from 'axios'
import VueAxios from 'vue-axios'
import ECharts from 'vue-echarts'

import echarts from "echarts";
Vue.prototype.$echarts = echarts;

Vue.config.productionTip = false
Vue.use(VueAxios,axios);
Vue.component('v-chart', ECharts)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
