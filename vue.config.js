/*
 * @Author: your name
 * @Date: 2020-12-23 01:36:10
 * @LastEditTime: 2021-01-23 12:15:41
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/vue.config.js
 */

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    host: 'localhost',
    port: 8080,
    proxy: {
      "/api": {
        ws: false,
        target: "http://localhost:7878",
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/api'
        }
      }
    }
  }
}
