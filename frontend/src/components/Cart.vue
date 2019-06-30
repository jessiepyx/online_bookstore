<template>
  <div>
    <el-dialog width="30%" title="支付成功" :visible.sync="alerted">
      <el-button type="primary" @click="closeAlert">确 定</el-button>
    </el-dialog>
    <div class="row" >
      <div class="col-sm-12 col-md-12 cart" style="margin-top: 20px">
        <h2>购物车</h2>
        <button class="btn btn-sm btn-outline-primary" @click="save">保存购物车</button>
        <span style="color:crimson;font-size:12px">离开页面前先保存，防止数据丢失哦～</span>
        <ul>
          <li v-for="book in baskets" :key="book.id">
            <img :src="book.imageUrl" class="imgClass" alt="book picture">
            <div class="message">
              <p style="font-size: 16px;font-weight: bold;">{{book.title}}</p>
              <p><span style="font-size: 14px;color:#222;margin-left: 5px">{{book.author}}</span></p>
              <p style="font-size: 15px;color:purple;margin-top: 5px">店铺：{{book.bookStore}}</p>
              <p style="margin-top: 20px">
                <a href="#" style="color: darkred;font-size: 12px;text-decoration:underline" @click.prevent="deleteBook(book.cartid)">删除</a>
                <span>|</span>
                <a href="#" style="color: grey;font-size: 12px" >移入收藏夹</a>
              </p>
            </div>
            <div class="price">
              ￥{{book.price}}
            </div>
            <div class="number">
              <button type="button" class="btn btn-outline-secondary btn-sm" style="border-radius: 50%" @click="subNumber(book.cartid)">-</button>
              {{book.number}}
              <button type="button" class="btn btn-outline-secondary btn-sm" style="border-radius: 50%" @click="addNumber(book.cartid)">+</button>
            </div>
          </li>
        </ul>
        <div class="totalPrice">小计：￥{{totalPrice}}</div>
        <button class="btn btn-danger btn-lg button" @click="confirm">结算</button>
      </div>
      <div class="box" v-show="makeSure">
        <div class="box1">
          <button class="close" @click="closeTheBox">X</button>
          <p >需支付金额:<span>￥{{totalPrice}}</span></p>
          <button type="button" class="btn btn-block btn-warning" @click="pay">支付</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cart',
  data () {
    return {
      alerted: false,
      makeSure: false,
      baskets: []
    }
  },
  computed: {
    totalPrice () {
      let price = 0
      for (let i = 0; i < this.baskets.length; i++) {
        price += this.baskets[i].number * this.baskets[i].price
      }
      return price
    },
    user () {
      return this.$store.state.currentUser
    }
  },
  methods: {
    subNumber (id) {
      for (let i = 0; i < this.baskets.length; i++) {
        if (id === this.baskets[i].cartid) {
          if (this.baskets[i].number > 1) {
            this.baskets[i].number--
          }
        }
      }
    },
    addNumber (id) {
      for (let i = 0; i < this.baskets.length; i++) {
        if (id === this.baskets[i].cartid) {
          this.baskets[i].number++
        }
      }
    },
    deleteBook (id) {
      this.$axios.get('/server', {
        params: {
          'operation': 'viewcart',
          'id': this.user.userid
        }
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success === true) {
              for (let i = 0; i < this.baskets.length; i++) {
                if (id === this.baskets[i].cartid) {
                  this.baskets.splice(i, 1)
                } else {
                  alert(response.data.maindata)
                }
              }
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    save () {
      var arr = []
      for (let i = 0; i < this.baskets.length; i++) {
        arr.push({cartid: this.baskets[i].cartid, number: this.baskets[i].number})
      }
      this.$axios.post('/server', {
        operation: 'savecart',
        id: this.user.userid,
        items: arr
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success === true) {
              alert('保存成功')
            } else {
              alert(response.data.maindata)
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    confirm () {
      this.makeSure = true
    },
    pay () {
      document.documentElement.scrollTop = 0
      this.$axios.get('/server', {
        params: {
          'operation': 'viewcart',
          'id': this.user.userid
        }
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success === true) {
              this.baskets = []
            } else {
              alert(response.data.maindata)
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
      this.alerted = true
    },
    closeTheBox () {
      this.makeSure = false
    },
    closeAlert () {
      this.alerted = false
      this.makeSure = false
    }
  },
  created () {
    this.$axios.get('/server', {
      params: {
        'operation': 'viewcart',
        'id': this.user.userid
      }
    })
      .then((response) => {
        if (response.status === 200) {
          if (response.data.success === true) {
            this.baskets = response.data.maindata
          } else {
            alert(response.data.maindata)
          }
        }
      })
      .catch(err => {
        console.log(err)
      })
    this.makeSure = false
  }
}
</script>

<style scoped>
  .cart ul{
    width:100%;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .cart ul li{
    width: 100%;
    border:1px solid #eee;
    border-radius: 8px;
    margin: 10px;
    padding: 5px;
  }
  .cart ul li::after{
    content:"";
    display: block;
    clear: both;
  }
  .cart ul li img{
    float: left;
    display: inline-block;
    margin-right: 20px;
    width: 100px;
    height: 150px;
  }
  .cart ul li .message{
    float: left;
  }
  .cart ul li .price{
    float: left;
    margin-top: 30px;
    margin-left: 20%;
    font-size: 18px;
    font-weight: bold;
    color:crimson;
  }
  .cart ul li p{
    margin: 0;
    padding: 0;
  }
  .cart ul li .number{
    float: left;
    margin-top: 30px;
    margin-left: 20%;
  }
  .totalPrice{
    color: crimson;
    font-size: 20px;
    font-weight: bold;
    position: absolute;
    right: 100px;
    border: 1px solid #222;
    padding: 10px;
    border-radius: 8px;
  }
  .button{
    position: absolute;
    right: 0px;
  }
  .box{
    width: 400px;
    height: 200px;
    border: 1px solid #eee;
    background: #eee;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    left: 50%;
    top:50%;
    transform: translate(-50%,-50%);
  }
  .box1{
    text-align: center;
  }
  .box1 p{
    font-size: 25px;
  }
  .close{
    display: inline-block;
    width: 50px;
    height: 50px;
    position: absolute;
    right: 0;
    top: 0;
  }
</style>
