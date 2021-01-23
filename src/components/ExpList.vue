<!--
 * @Author: your name
 * @Date: 2021-01-23 10:36:57
 * @LastEditTime: 2021-01-23 15:37:23
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/src/components/ExpList.vue
-->
<template>
  <card>
    <!-- <v-card-title>
      <v-text-field
        v-model="搜索实验"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="exps"
      :search="search"
    ></v-data-table> -->
  </card>
</template>

<script>
export default {
  name: "ExpList",
  data: () => {
    return {
      search: "",
      exps: {},
      headers: [
        {
          text: "实验名称",
          align: "start",
          filterable: 'true',
          value: "exp_name",
        },
        { text: "实验id", value: "exp_id" },
      ],
    };
  },
  mounted() {
    this.axios.get("/api/exp").then((response) => {
      console.log(response.data);
      this.exps = response.data;
    });
  },
};
</script>