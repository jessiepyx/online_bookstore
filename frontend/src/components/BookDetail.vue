<template>
  <div class="bookDetail">
    <el-dialog width="60%" title="成功加入购物车" :visible.sync="alerted">
      <el-button type="primary" @click="alerted = false">确 定</el-button>
    </el-dialog>
    <div class="container">
      <div class="row mt-5">
        <div class="col-md-4 box">
          <img :src="book.imgUrl" class="imgClass" alt="book picture">
        </div>
        <div class="col-md-8 book">
          <div class="name">{{book.title}}<span class="publisher">{{book.publisher}} {{book.publishDate}}</span></div>

          <p class="author">{{book.author}}</p>
          <p class="pands">折扣价：
            <span class="price">￥{{book.price}}</span>
            <span class="salesVolume">销量: {{book.salesVolume}}</span>
            <span class="stock">库存: {{book.stock}}</span>
          </p>
          <p class="bookstore">{{book.bookStore}}</p>
          <p class="fromAddress">发货地: {{book.fromAddress}}</p>
          <h6>简介：</h6>
          <p class="brief">{{book.intro}}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-8 button">
          <button type="button" class="btn btn-info btn-sm" style="margin-right: 20px" @click="addToCart">加入购物车</button>
          <button type="button" class="btn btn-danger btn-sm" @click="buy">立即购买</button>
        </div>
      </div>
      <hr/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'bookdetail',
  alerted: false,
  data () {
    return {
      bookId: this.$route.params.id,
      book: {}
    }
  },
  created () {
    this.$axios.get('/server', {
      params: {
        'operation': 'viewbook',
        'id': 'this.bookId'
      }
    })
      .then((response) => {
        if (response.status === 200) {
          if (response.data.success === true) {
            this.book = response.data.maindata
          } else {
            alert(response.data.maindata)
          }
        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    addToCart () {
      if (this.currentUser === null) {
        alert('请先登录')
      } else {
        this.$axios.post('/server', {
          operation: 'addtocart',
          id: this.bookId,
          buy: this.currentUser
        })
          .then((response) => {
            if (response.status === 200) {
              if (response.data.success === true) {
                this.alerted = true
              } else {
                alert(response.data.maindata)
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    buy () {
      if (this.currentUser === null) {
        alert('请先登录')
      } else {
        this.$store.commit('setCurrentBook', this.book)
        this.$router.push({name: 'buy'})
      }
    }
  },
  computed: {
    currentUser () {
      return this.$store.state.currentUser
    }
  }
}
</script>

<style scoped>
  .book .name{
    font-size: 20px;
    font-weight: bold;
  }
  .book .author{
    font-size: 14px;
    color:darkblue;
    margin-top: 5px;
    cursor: pointer;
  }
  .box .imgClass{
    width: 250px;
    height: 300px;
  }
  .book .publisher{
    font-size: 14px;
    color:#222;
    margin-left: 5px;
  }
  .book .pands{
    font-size: 14px;
    color:darkred;
    font-weight: bold;
  }
  .book .price{
    display: inline-block;
    width: 80px;
    height: 20px;
    border: 1px solid chocolate;
    border-radius: 8px;
    text-align: center;
    line-height: 20px;
    color: crimson;
    font-weight: bold;
  }
  .book .pands .stock,  .book .pands .salesVolume{
    color: #222;
    font-weight: normal;
    font-size:12px;
    margin-left: 20px;
  }
  .book .bookstore{
    font-size: 15px;
    color:darkmagenta;
    cursor: pointer;
  }
  .book .fromAddress{
    font-size: 15px;
  }
</style>
