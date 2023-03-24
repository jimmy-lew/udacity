<script setup lang="ts">
const { data }= await useAsyncData(() => queryContent('/prompts').findOne())

const prompts = ref<Prompt[]>(data.value?.prompts)
const ptr = ref(0) 

const queryData = ref<QueryData>({
	city: '',
	filter: '',
	month: '',
	day: '',
})

const handleOption = ({ name, value }: PromptAnswer) => {
	const key = name as keyof QueryData
	queryData.value[key] = value
	ptr.value++
	if (ptr.value <= 3) return
}
</script>

<template>
	<div class="w-screen h-screen bg-white">
		<div class="flex items-center justify-center h-full">
			<div class="flex flex-col items-center rounded-md max-w-lg bg-zinc-100 px-10 py-6">
				<h1 class="text-4xl font-bold text-center">
					Hi there!
				</h1>
				<h2 class="text-lg font-bold text-center mt-2">
					Let's explore some US bikeshare data!
				</h2>
				<Transition>
					<div v-if="ptr <= 3" class="pt-4 flex flex-col items-center text-center gap-2">
						<p class="">
							{{ prompts[ptr].prompt }}
						</p>
						<div class="flex flex-wrap mt-4 justify-center gap-2">
							<Option
								v-for="(option, index) in prompts[ptr].options"
								:key="index"
								:name="prompts[ptr].name"
								:value="option"
								@option-select="handleOption"
							/>
						</div>
					</div>
					<div v-else class="">
						empty
					</div>
				</Transition>
			</div>
		</div>
	</div>
	<div class="absolute m-4 top-0 right-0 w-10 h-10 p-2 rounded-md bg-zinc-200">
		<div class="flex items-center justify-center">
			<Icon size="24" name="material-symbols:portable-wifi-off-rounded" />
		</div>
	</div>
</template>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
