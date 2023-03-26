<script lang="ts">
export default {
	inheritAttrs: false,
}
</script>

<script setup lang="ts">
const { note, expand, isCompact } = withDefaults(defineProps<{
	title: string
	value: string | number
	icon: string
	note?: [string | number, string, string] // [value, unit, icon]
	isCompact?: boolean
	expand?: boolean
}>(), {
	isCompact: false,
	expand: false,
})

const stat_class = computed(() => {
	return [
		isCompact ? 'text-lg' : 'text-3xl',
		!note ? 'mt-5' : isCompact ? 'mt-2' : 'mt-1',
	]
})
</script>

<template>
	<div
		class="
		flex flex-col
		rounded-2xl h-52 p-6
		my-shadow bg-white
		hover:scale-105 transition-all duration-500 ease-in-out"
		:class="`${expand ? 'min-w-max' : 'aspect-square'}`"
	>
		<div class="inline-flex items-center justify-start mb-2">
			<div class="flex items-center justify-center w-8 h-8 p-1 rounded-lg" :class="$attrs.class">
				<Icon size="20" :name="icon" class="text-white" />
			</div>
		</div>
		<h3 class="font-semibold text-sm mt-2 mb-1">
			{{ title }}
		</h3>
		<h1 v-if="value" class="font-bold" :class="stat_class">
			{{ value }}
		</h1>
		<div v-if="value && note" class="mb-2 flex items-center justify-start text-zinc-400 text-xs" :class="`${isCompact ? 'mt-4' : 'mt-3'}`">
			<Icon v-if="note[2]" size="16" :name="note[2]" class="mr-1" />
			<p class="text-center mt-0.5">
				<span class="font-bold">{{ note[0] }}</span> {{ note[1] }}
			</p>
		</div>
		<div v-if="!value" class="flex items-center justify-center h-full">
			<Icon size="36" name="svg-spinners:270-ring" />
		</div>
	</div>
</template>

<style scoped>
.my-shadow {
	box-shadow: 0px 22px 56px rgba(180, 155, 190, 0.22);
}
</style>
