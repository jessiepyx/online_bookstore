<template>
  <div id="app">
    <div class="headertext">
      <span id="zju">浙江大学 </span><span id="bookstore">网上书城  </span>
      <span id="button">
        <el-button-group>
          <el-button plain type="primary" size="medium" @click="loginForm.visible = true">登录</el-button>
          <el-button plain type="primary" size="medium" @click="registerForm.visible = true">注册</el-button>
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
    <el-dialog title="登录" :visible.sync="loginForm.visible">
      <el-form>
        <el-form-item label="用户名" :label-width="loginForm.labelWidth">
          <el-input v-model="loginForm.username" placeholder="请输入用户名" clearable></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="loginForm.labelWidth">
          <el-input v-model="loginForm.password" placeholder="请输入密码" clearable show-password></el-input>
        </el-form-item>
      </el-form>
      <el-dialog width="30%" title="登录成功" :visible.sync="loginForm.successVisible" append-to-body>
        <el-button type="primary" @click="loginForm.successVisible = false; loginForm.visible = false">确 定</el-button>
      </el-dialog>
      <el-dialog width="30%" title="用户名或密码错误" :visible.sync="loginForm.failVisible" append-to-body>
        <el-button type="primary" @click="loginForm.failVisible = false">确 定</el-button>
      </el-dialog>
      <div slot="footer" class="dialog-footer">
        <el-button @click="loginForm.visible = false">取 消</el-button>
        <el-button type="primary" @click="onLogin">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog title="注册" :visible.sync="registerForm.visible">
      <el-form>
        <el-form-item label="用户名" :label-width="registerForm.labelWidth">
          <el-input v-model="registerForm.username" placeholder="请输入用户名" clearable></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="registerForm.labelWidth">
          <el-input v-model="registerForm.password" placeholder="请输入密码" clearable show-password></el-input>
        </el-form-item>
        <el-form-item label="确认密码" :label-width="registerForm.labelWidth">
          <el-input v-model="registerForm.password" placeholder="请再次输入密码" clearable show-password></el-input>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="registerForm.labelWidth">
          <el-input v-model="registerForm.password" placeholder="请输入email地址" clearable show-password></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="registerForm.labelWidth">
          <el-input v-model="registerForm.password" placeholder="请输入手机号码" clearable show-password></el-input>
        </el-form-item>
      </el-form>
      <el-dialog width="30%" title="注册成功" :visible.sync="registerForm.successVisible" append-to-body>
        <el-button type="primary" @click="registerForm.successVisible = false; registerForm.visible = false">确 定</el-button>
      </el-dialog>
      <el-dialog width="30%" title="注册失败" :visible.sync="registerForm.failVisible" append-to-body>
        <el-button type="primary" @click="registerForm.failVisible = false">确 定</el-button>
      </el-dialog>
      <div slot="footer" class="dialog-footer">
        <el-button @click="registerForm.visible = false">取 消</el-button>
        <el-button type="primary" @click="onRegister">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'app',
  data () {
    return {
      loginForm: {
        visible: false,
        username: '',
        password: '',
        labelWidth: '120px',
        successVisible: false,
        failVisible: false
      },
      registerForm: {
        visible: false,
        username: '',
        password: '',
        repeatPassword: '',
        email: '',
        telephone: '',
        labelWidth: '120px',
        successVisible: false,
        failVisible: false
      }
    }
  },
  components: {
    appHeader: Navbar
  },
  computed: {
    currentUser () {
      return this.$store.state.currentUser
    }
  },
  methods: {
    onLogin () {
      this.$axios.post('', {
        operation: 'login',
        username: this.loginForm.username,
        password: this.loginForm.password
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success === true) {
              this.$store.commit('setCurrentUser', response.data.maindata.username)
              this.$store.commit('setToken', true)
              console.log(this.$store.state.currentUser)
            } else {
              alert(response.data.maindata)
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    onRegister () {
      this.$axios.post('', {
        operation: 'register',
        username: this.registerForm.username,
        password: this.registerForm.password,
        repeatPassword: this.repeatPassword,
        email: this.email,
        telephone: this.telephone
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success !== true) {
              alert(response.data.maindata)
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    created () {
      this.$store.commit('logout')
    }
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
