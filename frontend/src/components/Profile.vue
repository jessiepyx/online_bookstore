<template>
    <el-row class="row">
      <el-row>
        <el-col :span="24"><div class="title">编辑个人信息</div></el-col>
      </el-row>
      <el-row>
        <el-upload
          class="avatar-uploader"
          action="https://jsonplaceholder.typicode.com/posts/"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload">
          <img v-if="imgUrl" :src="imgUrl" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
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
      },
      imgUrl: ''
    }
  },
  methods: {
    submit () {
      var msg = {
        email: this.form.email,
        telephone: this.form.telephone,
        imgUrl: this.imgUrl
      }
      this.$axios.post('', {
        operation: 'updateuser',
        username: this.form.username,
        email: this.form.email,
        telephone: this.form.telephone,
        imgUrl: this.imgUrl
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success !== true) {
              this.$store.commit('changeUserMessage', msg)
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
      this.imgUrl = this.user.imgUrl
    },
    handleAvatarSuccess (res, file) {
      this.imgUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
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
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
