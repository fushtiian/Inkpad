<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import LoginModal from './LoginModal.vue'

const router = useRouter()
const route = useRoute()

const moreOpen = ref(false)
const searchQuery = ref('')
const dropdownRef = ref(null)
const showLogin = ref(false)
const isLoggedIn = ref(false)
const currentUser = ref('')
const avatarOpen = ref(false)
const avatarRef = ref(null)

const moreItems = ['子项1', '子项2', '子项3']
const avatarItems = ['我的空间', '个人中心', '退出登录']

function toggleMore() {
  moreOpen.value = !moreOpen.value
}

function closeMore() {
  moreOpen.value = false
}

function navigate(path) {
  router.push(path)
  closeMore()
  avatarOpen.value = false
}

function onLogin(data) {
  isLoggedIn.value = true
  currentUser.value = data.username
}

function toggleAvatar() {
  avatarOpen.value = !avatarOpen.value
}

function handleAvatarAction(item) {
  if (item === '退出登录') {
    isLoggedIn.value = false
    currentUser.value = ''
    avatarOpen.value = false
  } else if (item === '我的空间') {
    navigate('/home')
  } else if (item === '个人中心') {
    navigate('/home')
  }
}

function onClickOutside(e) {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target)) {
    closeMore()
  }
  if (avatarRef.value && !avatarRef.value.contains(e.target)) {
    avatarOpen.value = false
  }
}

const avatarLetter = computed(() => currentUser.value ? currentUser.value[0].toUpperCase() : 'U')

onMounted(() => {
  document.addEventListener('click', onClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', onClickOutside)
})
</script>

<template>
  <nav class="navbar">
    <div class="nav-inner">
      <button
        class="nav-btn brand"
        @click="navigate('/home')"
      >
        Inkpad
      </button>
      <button
        class="nav-btn"
        :class="{ active: route.path === '/home' }"
        @click="navigate('/home')"
      >
        首页
      </button>
      <button
        class="nav-btn"
        :class="{ active: route.path === '/theory' }"
        @click="navigate('/theory')"
      >
        理论
      </button>
      <button
        class="nav-btn"
        :class="{ active: route.path === '/apps' }"
        @click="navigate('/apps')"
      >
        应用
      </button>

      <div ref="dropdownRef" class="dropdown-wrapper">
        <button
          class="nav-btn dropdown-toggle"
          :class="{ active: moreOpen || route.path.startsWith('/more') }"
          @click="toggleMore"
        >
          更多
          <span class="arrow" :class="{ open: moreOpen }">&#9660;</span>
        </button>
        <ul v-if="moreOpen" class="dropdown-menu">
          <li v-for="(item, idx) in moreItems" :key="idx">
            <button
              :class="{ active: route.path === '/more/' + (idx + 1) }"
              @click="navigate('/more/' + (idx + 1))"
            >
              {{ item }}
            </button>
          </li>
        </ul>
      </div>

      <div class="search-wrapper">
        <input
          v-model="searchQuery"
          type="text"
          class="search-input"
          placeholder="搜索..."
        />
        <svg class="search-icon" viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
          <circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="2" fill="none" />
          <line x1="16.5" y1="16.5" x2="21" y2="21" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
        </svg>
      </div>

      <button
        class="nav-btn"
        :class="{ active: route.path === '/app-download' }"
        @click="navigate('/app-download')"
      >
        App
      </button>
      <button v-if="!isLoggedIn" class="nav-btn" @click="showLogin = true">
        登录/注册
      </button>
      <div v-else ref="avatarRef" class="avatar-wrapper">
        <button class="nav-btn avatar-btn" @click="toggleAvatar">
          <span class="avatar">{{ avatarLetter }}</span>
          <span class="arrow" :class="{ open: avatarOpen }">&#9660;</span>
        </button>
        <ul v-if="avatarOpen" class="avatar-menu">
          <li v-for="item in avatarItems" :key="item">
            <button @click="handleAvatarAction(item)">
              {{ item }}
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <LoginModal v-if="showLogin" @close="showLogin = false" @login="onLogin" />
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: #222222;
  z-index: 1000;
  display: flex;
  justify-content: center;
  overflow: visible;
}

.nav-inner {
  display: flex;
  align-items: stretch;
  gap: 2px;
  padding: 0 16px;
  height: 54px;
  overflow: visible;
}

.nav-btn {
  background: #222222;
  color: #9d9d9d;
  border: none;
  padding: 0 14px;
  margin: 3px 0;
  cursor: pointer;
  font-size: 15px;
  font-family: inherit;
  transition: background 0.15s, color 0.15s;
  white-space: nowrap;
}

.nav-btn:hover {
  background: #222222;
  color: #ffffff;
}

.nav-btn:active {
  outline: 1px solid #ffffff;
  outline-offset: -1px;
}

.nav-btn:focus-visible {
  outline: 1px solid #ffffff;
  outline-offset: -1px;
}

.nav-btn.active {
  color: #ffffff;
  background: #080808;
}

.dropdown-wrapper {
  position: relative;
  display: flex;
  align-items: stretch;
}

.dropdown-toggle {
  display: inline-flex;
  align-items: center;
}

.arrow {
  margin-left: 4px;
  font-size: 9px;
  display: inline-block;
  transition: transform 0.2s;
}

.arrow.open {
  transform: rotate(180deg);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 4px;
  background: #fff;
  list-style: none;
  padding: 4px 0;
  border-radius: 4px;
  min-width: 120px;
  z-index: 9999;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.dropdown-menu li button {
  display: block;
  width: 100%;
  background: #fff;
  border: none;
  color: #333;
  padding: 8px 16px;
  text-align: left;
  cursor: pointer;
  font-size: 14px;
  font-family: inherit;
}

.dropdown-menu li button:hover {
  background: #f5f5f5;
}

.dropdown-menu li button.active {
  background: #337ab7;
  color: #fff;
}

.search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  border-left: 1px solid #444;
  padding-left: 10px;
  margin: 6px 0;
}

.search-input {
  background: #fff;
  border: 1px solid #555;
  border-radius: 5px;
  padding: 4px 28px 4px 10px;
  color: #333;
  font-size: 14px;
  font-family: inherit;
  width: 180px;
  outline: none;
  transition: border-color 0.15s;
}

.search-input::placeholder {
  color: #999;
}

.search-input:focus {
  border-color: #222;
}

.search-icon {
  position: absolute;
  right: 8px;
  color: #999;
  pointer-events: none;
}

.brand {
  font-family: 'Satisfy', cursive;
  font-size: 25px;
  padding: 0 16px;
}

.avatar-wrapper {
  position: relative;
  display: flex;
  align-items: stretch;
}

.avatar-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #555;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
}

.avatar-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 4px;
  background: #fff;
  list-style: none;
  padding: 4px 0;
  border-radius: 4px;
  min-width: 120px;
  z-index: 9999;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.avatar-menu li button {
  display: block;
  width: 100%;
  background: #fff;
  border: none;
  color: #333;
  padding: 8px 16px;
  text-align: left;
  cursor: pointer;
  font-size: 14px;
  font-family: inherit;
}

.avatar-menu li button:hover {
  background: #f5f5f5;
}

.avatar-menu li button.active {
  background: #337ab7;
  color: #fff;
}
</style>
