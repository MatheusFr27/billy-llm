<template>
  <main style="width: 100%; height: 100%;" class="d-flex flex-column align-center justify-center py-4">
    <Header></Header>
    <Message :messages="messages"></Message>
    <div style="width: 50%;" class="d-flex flex-row align-center justify-center mt-4">
      <v-text-field v-model="message" :onkeydown="(event: any) => onKeyDown(event)" class="mr-2" hide-details
        placeholder="Digite sua mensagem"></v-text-field>
      <v-btn :loading="loading" prepend-icon="mdi-send" variant="tonal" style="height: 100%;">
        Enviar
      </v-btn>
    </div>
  </main>
</template>

<script setup lang="ts">
import Message from '@/components/Message.vue'
import Header from '@/components/Header.vue'
import { useFetch } from '@/http/fetch'
import { ref } from 'vue';

const loading = ref(false);
const messages = ref<{ role: string; content: string }[]>([]);
const message = ref('');

function onKeyDown(event: { key: string; }) {
  if (event.key === 'Enter' && !loading.value) {
    sendMessage()
  }
}

// useFetch('http://localhost:8000/send-message', body).then(response => {
//   console.log(response)
//   messages.value = response.data.messages
// }).finally(() => {
//   loading.value = false
// })

function sendMessage() {
  loading.value = true;

  const messageUser = { role: 'user', content: message.value }

  messages.value.push(messageUser)
  message.value = ''

  const body = {
    messages: messages.value,
  }

  useFetch('http://localhost:8000/send-message', body).then(response => {
    console.log(response)
    messages.value = response.data.messages
  }).finally(() => {
    loading.value = false
  })
}
</script>