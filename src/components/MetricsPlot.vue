<!--
 * @Author: your name
 * @Date: 2021-01-23 14:29:20
 * @LastEditTime: 2021-01-23 16:25:42
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/src/components/LineChart.vue
-->

<template>
  <v-card >
    <v-card-title>{{ title }}</v-card-title>
    <v-row align="center" justify="end">
      <v-chart
        :options="option"
        autoresize
      ></v-chart>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: ["metrics", "title"],
  computed: {
    option() {
      return {
        xAxis: {
          data: this.metrics.map((x) => x["step"]),
        },
        yAxis: { type: "value" },
        series: [
          {
            data: this.metrics.map((x) => x["value"]),
            type: "line",
            smooth: true,
          },
        ],
      };
    },
  },
  // mounted() {
  //   const that = this;
  //   window.addEventListener("resize", function () {
  //     that.echarts.resize(); //初始化的
  //   });
  // }
};
</script>
