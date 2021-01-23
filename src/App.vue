<!--
 * @Author: your name
 * @Date: 2020-12-23 01:30:35
 * @LastEditTime: 2021-01-23 16:57:11
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/src/App.vue
-->
<template>
  <v-app id="inspire">
    <v-app-bar app clipped-right flat height="72">
      <h1 class="black--text">
        <v-icon @click="drawer = !drawer">menu</v-icon>
        Lamb
      </h1>
      <v-spacer></v-spacer>

      <v-responsive max-width="156">
        <v-text-field dense flat hide-details rounded solo-inverted
          >Lamb</v-text-field
        >
      </v-responsive>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app width="300">
      <v-list class="pl-14" shaped>
        <ExpList></ExpList>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer app clipped right>
      <MetricsList></MetricsList>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <v-row class="py-2">
          <v-col
            cols="4"
            class="px-2"
            v-for="(value, name) in metrics"
            :key="name"
          >
            <MetricsPlot :metrics="value" :title="name"></MetricsPlot>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import ECharts from "vue-echarts/components/ECharts";
// import "echarts/lib/chart/bar";
import ExpList from "@/components/ExpList";
import MetricsList from "@/components/MetricsList";
import MetricsPlot from "@/components/MetricsPlot";

export default {
  components: { ExpList, MetricsList, MetricsPlot },
  data: function () {
    return {
      title: "ceshfhsdifhsdifjsdfjskldf ",
      bar: {
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: "line",
            smooth: true,
          },
        ],
      },
      metrics: {},
      models: {},
    };
  },
  methods: {
    get_data() {
      this.axios.get("/api/exp/resnet").then((resp) => {
        console.log(resp.data);
        this.models["resnet"] = resp.data;
      });

      this.axios.get("/api/exp/vlbert").then((resp) => {
        console.log(resp.data);
        this.model["vlbert"] = resp.data;
      });
    },
  },
  watch: {
    model: (new_val) => {
      for ((metrics, model_name) in new_val) {
        for ((points, metric_name) in metrics) {
          this.metrics[metric_name][model_name] = points;
        }
      }
    },
  },
  mounted() {
    this.get_data();
  },
};
</script>