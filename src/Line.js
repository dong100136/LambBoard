/*
 * @Author: jiandong.ye
 * @email: yejiandong@bytedance.com
 * @Date: 2020-12-23 23:22:54
 * @description: 
 */

import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  mounted() {
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [40, 39, 10, 40, 39, 80, 40]
        },
        {
          label: 'Data Two',
          backgroundColor: '#f8f979',
          data: [10, 30, 12, 28, 29, 70, 30]
        }
      ]
    }, { responsive: true, maintainAspectRatio: false })
  }
}