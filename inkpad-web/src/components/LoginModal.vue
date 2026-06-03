<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const emit = defineEmits(['close', 'login'])

const username = ref('')
const password = ref('')
const remember = ref(false)
const modalRef = ref(null)
const error = ref('')

function onOverlayClick(e) {
  if (modalRef.value && !modalRef.value.contains(e.target)) {
    emit('close')
  }
}

function onKeydown(e) {
  if (e.key === 'Escape') emit('close')
}

function handleLogin() {
  error.value = ''
  if (username.value === 'fushitian' && password.value === '197011') {
    emit('login', { username: username.value, remember: remember.value })
    emit('close')
  } else {
    error.value = '用户名或密码错误'
  }
}

onMounted(() => {
  document.addEventListener('keydown', onKeydown)
})

onUnmounted(() => {
  document.removeEventListener('keydown', onKeydown)
})
</script>

<template>
  <div class="overlay" @click="onOverlayClick">
    <div ref="modalRef" class="modal">
      <button class="close-btn" @click="emit('close')">&times;</button>
      <h1 class="brand">Inkpad</h1>
      <form class="form" @submit.prevent="handleLogin">
        <input
          v-model="username"
          type="text"
          class="input"
          placeholder="用户名或邮箱"
        />
        <input
          v-model="password"
          type="password"
          class="input"
          placeholder="密码"
        />
        <label class="remember">
          <input v-model="remember" type="checkbox" />
          记住我
        </label>
        <p v-if="error" class="error">{{ error }}</p>
        <button type="submit" class="login-btn">登录</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal {
  background: #fff;
  border-radius: 8px;
  padding: 40px 36px 32px;
  width: 360px;
  max-width: 90vw;
  position: relative;
  box-sizing: border-box;
}

.close-btn {
  position: absolute;
  top: 8px;
  right: 12px;
  background: none;
  border: none;
  font-size: 24px;
  color: #999;
  cursor: pointer;
  line-height: 1;
}

.close-btn:hover {
  color: #333;
}

.brand {
  font-family: 'Satisfy', cursive;
  font-size: 36px;
  color: #222;
  text-align: center;
  margin: 0 0 28px;
  font-weight: 400;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.input {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px 12px;
  font-size: 14px;
  font-family: inherit;
  color: #333;
  outline: none;
  transition: border-color 0.2s;
}

.input:focus {
  border-color: #222;
}

.input::placeholder {
  color: #aaa;
}

.remember {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: #555;
  cursor: pointer;
}

.remember input {
  margin: 0;
}

.error {
  color: #e74c3c;
  font-size: 13px;
  margin: -8px 0 0;
  text-align: center;
}

.login-btn {
  background: #222;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px;
  font-size: 15px;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.2s;
}

.login-btn:hover {
  background: #444;
}
</style>
