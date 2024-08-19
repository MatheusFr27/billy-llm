<template>
    <v-card min-width="50%" class="pa-2 d-flex flex-row align-center">
        <v-avatar size="60px" class="mr-2">
            <v-img alt="Foto do Billy" :src="billyImage"></v-img>
        </v-avatar>
        <h2>Billy</h2>
    </v-card>
</template>

<script setup>
import billyImage from '@/assets/billy.jpeg'
</script>