<template>

<nav class="navbar navbar-light bg-light">
  <div class="container-fluid">
    <router-link class="navbar-brand" to="/">whoame的博客</router-link>
    <button class="navbar-toggler" type="button" data-bs-target="#navbarToggleMenu" data-bs-toggle="collapse"
            aria-controls="navbarToggleMenu" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarToggleMenu">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link" to="/">主页</router-link>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button"
             data-bs-toggle="dropdown" aria-expanded="false">
            更多
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><router-link class="dropdown-item" to="/">Home</router-link></li>
            <li><router-link class="dropdown-item" to="/list">文章列表</router-link></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">else</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="搜索内容..." aria-label="Search">
      <button class="btn btn-outline-success" type="submit"><i class="bi bi-search"></i></button>
    </form>
    </div>

  </div>

</nav>

</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>

</style>
