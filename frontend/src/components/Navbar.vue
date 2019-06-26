<template>
  <header>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-menu-item index="1" @click="toHome">
          <i class="el-icon-s-home"></i>
          <span slot="title">商城</span>
      </el-menu-item>
      <el-menu-item index="2" @click="toCart">
        <i class="el-icon-shopping-cart-2"></i>
        <span slot="title">购物车</span>
      </el-menu-item>
      <el-menu-item index="3" @click="toProfile">
        <i class="el-icon-user"></i>
        <span slot="title">个人中心</span>
      </el-menu-item>
      <el-menu-item index="4" @click="toHistory">
        <i class="el-icon-document"></i>
        <span slot="title">历史记录</span>
      </el-menu-item>
    </el-menu>
  </header>
</template>

<script>
export default {
  name: 'navbar',
  data () {
    return {
      isCollapse: false
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    toHome () {
      this.$router.push({name: 'home'})
    },
    toCart () {
      if (this.$store.state.token === true) {
        this.$router.push({name: 'cart'})
      } else {
        this.$alert('未登录无法使用购物车哟~', '请先登录', {
          confirmButtonText: '知道了'
        })
      }
    },
    toProfile () {
      if (this.$store.state.token === true) {
        this.$router.push({name: 'profile'})
      } else {
        this.$alert('未登录无法查看个人信息哟~', '请先登录', {
          confirmButtonText: '知道了'
        })
      }
    },
    toHistory () {
      if (this.$store.state.token === true) {
        this.$router.push({name: 'history'})
      } else {
        this.$alert('未登录无法查看历史订单哟~', '请先登录', {
          confirmButtonText: '知道了'
        })
      }
    }
  }
}
</script>

<style scoped>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
  a {
    text-decoration: none;
  }
</style>
