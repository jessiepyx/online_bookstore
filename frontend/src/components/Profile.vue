<template>
    <el-row class="row">
      <el-row>
        <el-col :span="24"><div class="title">编辑个人信息</div></el-col>
      </el-row>
      <el-row>
        <el-form>
          <el-form-item label="用户名" :label-width="form.labelWidth">
            <el-input v-model="form.username" disabled></el-input>
          </el-form-item>
          <el-form-item label="邮箱" :label-width="form.labelWidth">
            <el-input v-model="form.username" placeholder="请添加邮箱" clearable></el-input>
          </el-form-item>
          <el-form-item label="手机号" :label-width="form.labelWidth">
            <el-input v-model="loginForm.password" placeholder="请添加电话号码" clearable></el-input>
          </el-form-item>
        </el-form>
        <el-dialog width="30%" title="编辑成功" :visible.sync="form.successVisible">
          <el-button type="primary" @click="form.successVisible = false">确 定</el-button>
        </el-dialog>
        <el-dialog width="30%" title="编辑失败" :visible.sync="form.failVisible">
          <el-button type="primary" @click="form.failVisible = false">确 定</el-button>
        </el-dialog>
      </el-row>
      <el-row>
          <el-button @click="reset">复 位</el-button>
          <el-button type="primary" @click="submit">确 定</el-button>
      </el-row>
    </el-row>
</template>

<script>
export default {
  name: 'profile',
  data () {
    return {
      form: {
        visible: false,
        username: '',
        email: '',
        telephone: '',
        labelWidth: '120px',
        successVisible: false,
        failVisible: false
      }
    }
  },
  methods: {
    submit () {
      this.$axios.post('', {
        operation: 'updateuser',
        username: this.form.username,
        email: this.form.email,
        telephone: this.form.telephone
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success !== true) {
              this.form.successVisible = true
            } else {
              alert(response.data.maindata)
              this.form.failVisible = true
            }
          } else {
            this.form.failVisible = true
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    reset () {
      this.form.email = this.user.email
      this.form.telephone = this.user.telephone
    }
  },
  computed: {
    user () {
      return this.$store.state.currentUser
    }
  },
  created () {
    this.form.username = this.user.username
    this.reset()
  }
}
</script>

<style scoped>
  .title {
    height: 50px;
    font-family: "PingFang SC", serif;
    font-size: xx-large;
  }
  .consumer *{
    box-sizing: border-box;
  }
  .consumer label{
    display: block;
    margin:10px 0 10px;
    font-weight: bold;
  }
  .consumer .bianji{
    display: block;
    margin:20px 0;
    color:#fff;
    padding:5px;
    border-radius:4px;
    cursor: pointer;
    background: darkgreen;
  }
</style>
