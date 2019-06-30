<template>
  <div>
    <el-table :data="orders" border style="width: 100%">
      <el-table-column fixed prop="date" label="日期" width="150"></el-table-column>
      <el-table-column prop="id" label="书籍编号" width="100"></el-table-column>
      <el-table-column prop="bookname" label="书名" width="150"></el-table-column>
      <el-table-column prop="price" label="价格" width="100"></el-table-column>
      <el-table-column prop="sell" label="卖家" width="100"></el-table-column>
      <el-table-column prop="selltel" label="卖家电话" width="150"></el-table-column>
      <el-table-column prop="num" label="数量" width="80"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'history',
  data () {
    return {
      orders: []
    }
  },
  methods: {
    handleClick (row) {
      console.log(row)
      this.$router.push({path: '/bookdetail/' + row.id})
    }
  },
  created () {
    this.$axios.get('/', {
      params: {
        'operation': 'vieworder',
        'buy': this.currentUser.username
      }
    })
      .then((response) => {
        if (response.status === 200) {
          if (response.data.success === true) {
            this.orders = response.data.maindata
          } else {
            alert(response.data.maindata)
          }
        }
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style scoped>

</style>
