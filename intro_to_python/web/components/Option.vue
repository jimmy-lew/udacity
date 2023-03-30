<script setup lang="ts">
defineProps<{
	name: string
	value: string
}>()

const emits = defineEmits<{
	(e: 'optionSelect', data: PromptAnswer): void
}>()

const option = ref<HTMLButtonElement>() as Ref<HTMLButtonElement>
</script>

<template>
	<button
		ref="option"
		class="
        flex justify-center items-center
        rounded-md bg-zinc-50 select-none cursor-pointer
        py-2 px-4
        hover:scale-105 hover:bg-zinc-100
        transition-all duration-200 ease-in-out
        font-semibold"
		:name="name"
		:value="value"
		@click="emits('optionSelect', { name, value })"
	>
		{{ value }}
	</button>
</template>

<style scoped>

</style>
