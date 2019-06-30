<template>
  <div class="books">
    <ul>
      <li v-for="book in books" :key="book.id">
        <router-link :to="'/bookdetail/' + book.id">
          <img class="bookImg" :src="book.imgUrl" alt="book picture">
          <div>
            <p class="bookTitle" >{{book.title}}</p>
            <span class="money">￥{{book.price}}</span>
            <p class="brief">{{book.intro}}...</p>
          </div>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'books',
  computed: {
    books () {
      return this.$store.state.bookItems
    }
  }
}
</script>

<style scoped>
  .books{
    width: 100%;
    box-sizing: border-box;
  }
  a{
    text-decoration: none;
    color:#222;
  }
  ul{
    display: flex;
    flex-wrap:wrap;
    padding: 0;
    list-style: none;
    text-align: center;
  }
  li{
    flex-grow: 1;
    flex-basis:200px;
    padding: 2px;
    margin: 10px 0px;
    cursor: pointer;

  }
  li:hover{
    background-color: #eee;
  }
  li:hover .bookImg{
    transform: scale(1.2);
  }
  .bookImg{
    width: 120px;
    height: 180px;
    transition:transform 0.8s;
  }
  .books .bookTitle{
    font-weight: bold;
    padding: 0;
    margin: 0;
  }
  .books .money{
    font-size: 14px;
    color:crimson;
  }
  .books .brief{
    font-size: 13px;
    color:#424242;
  }
</style>
