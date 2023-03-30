<script setup lang="ts">
const { data } = await useAsyncData(() => queryContent('/prompts').findOne())

const prompts = ref<Prompt[]>(data.value?.prompts)
const loading = ref(true)
const error = ref('')
const is_api_online = ref(false)
const ptr = ref(0)
const tail = ref(3)

const queryData = ref<QueryBody>({
	city: '',
	filter: '',
	month: '',
	day: '',
})

const handleComplete = async () => {
	const { data, pending } = await useFetch('http://localhost:8080/load/', {
		method: 'POST',
		body: {
			...queryData.value,
			month: prompts.value[2].options.indexOf(queryData.value.month) + 1,
		},
		headers: {
			'Content-Type': 'application/json',
		},
	})

	loading.value = pending.value
	error.value = ''

	const res = data.value as StatusResponse

	if (res.status === 'OK') {
		setTimeout(() => {
			navigateTo('/results')
		}, 1000)
	}
	if (res.code === 400) {
		error.value = res.message || 'Bad Request'
		setTimeout(() => {
			window?.location.reload()
		}, 3000)
	}
}

const handleOption = async ({ name, value }: PromptAnswer) => {
	queryData.value[name as keyof QueryBody] = value

	if (ptr.value === 1) {
		const { filter } = queryData.value
		if (filter === 'Month') tail.value = 2
		if (filter === 'Day') ptr.value++
		if (filter === 'None') tail.value = 0
	}

	if (ptr.value++ >= tail.value) return handleComplete()
}

// Poll the API to check if it's online [TODO: replace with websocket]
onMounted(() => {
	const { data } = useFetch<StatusResponse>('http://localhost:8080/ok/')

	is_api_online.value = data.value?.status === 'OK'
	if (is_api_online.value) return

	const api_checker = setInterval(() => {
		const { data } = useFetch<StatusResponse>('http://localhost:8080/ok/')
		is_api_online.value = data.value?.status === 'OK'
		if (is_api_online.value) clearInterval(api_checker)
	}, 500)
})
</script>

<template>
	<div class="w-screen h-screen bg-white">
		<div class="flex items-center justify-center h-full">
			<div class="flex flex-col items-center rounded-xl max-w-lg bg-white my-shadow px-10 py-8">
				<h1 class="text-4xl font-bold text-center">
					Hi there!
				</h1>
				<h2 class="text-lg font-bold text-center mt-2">
					Let's explore some US bikeshare data!
				</h2>
				<Transition>
					<div v-if="ptr <= tail" class="pt-4 flex flex-col items-center text-center gap-2">
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
					<div v-else class="pt-4">
						<div v-if="loading">
							<Icon size="32" name="svg-spinners:3-dots-bounce" />
						</div>
						<div v-if="!loading && !error">
							<Icon size="32" name="material-symbols:check-circle" />
						</div>
						<div v-if="!loading && error">
							<Icon size="32" name="material-symbols:add-circle-rounded" class="rotate-45" />
						</div>
					</div>
				</Transition>
			</div>
		</div>
	</div>
	<div v-if="!is_api_online" class="absolute m-4 top-16 left-1/2 -translate-x-1/2 w-12 h-12 p-2 rounded-md bg-white my-shadow">
		<div class="flex items-center justify-center">
			<Icon class="pulse" size="32" name="material-symbols:portable-wifi-off-rounded" />
		</div>
	</div>
	<Transition name="right">
		<div v-if="error" class="absolute top-4 right-4">
			<Toast class="pulse">
				{{ error }}
			</Toast>
		</div>
	</Transition>
</template>

<style>
.v-enter-active,
.v-leave-active {
  transition: all 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.right-enter-active,
.right-leave-active {
  transition: all 0.5s ease;
}
.right-enter-from,
.right-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

.pulse {
	animation: pulse-red 2s infinite ease-in-out;
}

.my-shadow {
	box-shadow: 0px 22px 56px rgba(180, 155, 190, 0.22);
}

@keyframes pulse-red
{
	0% { color: #000; }
	50% { color: #e11d48; }
	100% { color: #000; }
}
</style>
