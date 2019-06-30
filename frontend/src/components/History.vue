<template>
  <!--订单-->
  <div class="col-sm-12 col-md-6" >
    <div class="orderForm">
      <h2>已购商品</h2>
      <table class="table">
        <thead class="thead-default">
        <tr>
          <th>书名</th>
          <th>单价</th>
          <th>数量</th>
          <th>店铺</th>
          <th>总价</th>
          <th>评价</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="book in orders">
          <td>{{book.title}}</td>
          <td>￥{{book.price}}</td>
          <td>{{book.number}}</td>
          <td>{{book.bookStore}}</td>
          <td>￥{{book.price * book.number}}</td>
          <td><router-link :to="'/comment/'+book.id"><button class="btn btn-sm btn-danger" >评价</button></router-link></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'history'
}
</script>

<style scoped>

</style>
