<template>
  <div class="home">
    <el-container>
      <el-header class="search">
        <el-row :gutter="20">
          <el-col :span="16">
            <el-input type="text" placeholder="你要找哪本书？" prefix-icon="el-icon-search" v-model="searchString"></el-input>
          </el-col>
          <el-col :span="8">
            <el-button type="primary" icon="el-icon-search"  @click="search">搜索</el-button>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <books></books>
      </el-main>
      <el-footer>
        <el-pagination
          background
          layout="prev, pager, next"
          :total="10">
        </el-pagination>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import books from './Books'
export default {
  name: 'home',
  components: {
    books
  },
  data () {
    return {
      searchString: null
    }
  },
  methods: {
    search () {
      this.$axios.get('', {
        params: {
          'operation': 'searchbook',
          'bookname': 'searchString'
        }
      })
        .then((response) => {
          if (response.status === 200) {
            if (response.data.success === true) {
              this.$store.commit('setBookItems', response.data.maindata)
            } else {
              alert(response.data.maindata)
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    created () {
      this.search()
    }
  }
}
</script>

<style scoped>

</style>
