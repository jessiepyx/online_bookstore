<template>
  <div id="app">
    <div class="headertext">
      <span id="zju">浙江大学 </span><span id="bookstore">网上书城  </span>
      <span id="button">
        <el-button-group>
          <el-button plain type="primary" size="medium">登录</el-button>
          <el-button plain type="primary" size="medium">注册</el-button>
      </el-button-group>
      </span>
    </div>
    <div class="headerlogo">
      <img src="./assets/header.png" alt="header">
    </div>
    <div class="body">
      <el-container>
        <el-aside>
          <app-header></app-header>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'app',
  components: {
    appHeader: Navbar
  }
}
</script>

<style>
  .headertext {
    margin: 5px 20px;
    width: 100%;
    height: 50px;
    font-family: "PingFang SC", serif;
    font-size: xx-large;
  }
  .headertext #zju {
    color: cadetblue;
    text-align: left;
  }
  .headertext #bookstore {
    color: dimgrey;
    text-align: left;
  }
  .headerlogo {
    margin: 5px 2px;
    width: 100%;
    height: 200px;
  }
  .headerlogo img {
    width: 100%;
    height: 100%;
  }
  .body {
    width: 100%;
    margin: 10px 20px;
  }
</style>
