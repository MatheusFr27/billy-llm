import { ref } from 'vue'

export async function useFetch<B>(url: string, body: B) {
    const result = ref<Response>()

    result.value = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify(body),
    })

    return { data: await result.value.json() }
}