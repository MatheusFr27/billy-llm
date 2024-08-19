<template>
    <v-virtual-scroll height="80%" width="50%" :items="props.messages" class="px-2">
        <template v-slot:default="{ item }">
            <div :class="`d-flex ${item.role === 'user' ? 'justify-end' : 'justify-start'}`">
                <v-card variant="tonal" :class="`my-2 pa-2 ${item.role === 'user' ? 'bg-grey-darken-3' : 'primary'}`"
                    style="max-width: 60%;">
                    <p class="text-subtitle-1">
                        {{ item.content }}
                    </p>
                </v-card>
            </div>
        </template>
    </v-virtual-scroll>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    messages: {
        type: Object,
        required: true
    }
})
</script>

<style lang="css" scoped>
*::-webkit-scrollbar {
    height: 7px;
    width: 7px;
}

*::-webkit-scrollbar-track {
    border-radius: 1px;
    background-color: transparent;
}

*::-webkit-scrollbar-track:hover {
    background-color: transparent;
}

*::-webkit-scrollbar-track:active {
    background-color: transparent;
}

*::-webkit-scrollbar-thumb {
    border-radius: 1px;
    background-color: #C0C0C0;
}

*::-webkit-scrollbar-thumb:hover {
    background-color: #b4b4b4;
}

*::-webkit-scrollbar-thumb:active {
    background-color: #C0C0C0;
}

</style>