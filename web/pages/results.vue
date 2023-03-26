<script setup lang="ts">
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

const { data: time } = await useFetch<TimeResponse>('http://localhost:8080/get_time')
const { data: trip } = await useFetch<TripResponse>('http://localhost:8080/get_trip')
const { data: user } = await useFetch<UserResponse>('http://localhost:8080/get_user')
</script>

<template>
	<div class="">
		<div class="relative pt-8 overflow-y-hidden">
			<div
				class="
				absolute z-0 inset-0
				bg-gradient-to-b from-purple-200/50 to-white
				w-full h-48"
			/>
			<div class="flex flex-col mt-10 w-full">
				<h1 class="relative z-10 font-bold text-2xl mb-4 pl-16">
					Time Data
				</h1>
				<div
					class="
					relative z-10
					flex items-center justify-start
					w-full overflow-x-scroll gap-10
					px-16 pb-16"
				>
					<Card
						class="bg-emerald-500"
						title="Busiest hour"
						icon="bx:hourglass"
						:value="time ? `${time.hour.value}:00` : ''"
						:note="[time?.hour.count || 0, 'users', 'material-symbols:person-3-rounded']"
					/>
					<Card
						class="bg-amber-500"
						title="Busiest day"
						icon="material-symbols:calendar-view-day-rounded"
						:value="time?.day.value.toString().slice(0, 3) || ''"
						:note="[time?.day.count || 0, 'users', 'material-symbols:person-3-rounded']"
					/>
					<Card
						class="bg-rose-500"
						:value="time ? months[time.month.value - 1] : ''"
						title="Busiest month"
						icon="fluent:calendar-month-20-filled"
						:note="[time?.month.count || 0, 'users', 'material-symbols:person-3-rounded']"
					/>
				</div>
			</div>
			<div class="flex flex-col w-full">
				<h1 class="relative z-10 font-bold text-2xl mb-4 pl-16">
					Trip Data
				</h1>
				<div
					class="
					relative z-10
					flex items-center justify-start
					overflow-x-scroll gap-10
					px-16 pb-16"
				>
					<Card
						class="bg-violet-500"
						title="Most popular route"
						icon="ic:twotone-route"
						:value="trip?.full_trip || ''"
						:note="[trip?.count || 0, 'users', 'material-symbols:person-3-rounded']"
						is-compact
						expand
					/>
					<Card
						class="bg-orange-500"
						title="Most popular start station"
						icon="material-symbols:line-start-circle-outline-rounded"
						:value="trip?.station.start.value || ''"
						:note="[trip?.station.start.count || 0, 'users', 'material-symbols:person-3-rounded']"
						is-compact
						expand
					/>
					<Card
						class="bg-sky-500"
						title="Most popular end station"
						icon="material-symbols:line-end-circle-outline-rounded"
						:value="trip?.station.end.value || ''"
						:note="[trip?.station.end.count || 0, 'users', 'material-symbols:person-3-rounded']"
						is-compact
						expand
					/>
					<Card
						class="bg-emerald-500"
						title="Average duration"
						icon="bx:hourglass"
						:value="trip ? `${Math.round(trip.duration.avg / 60)} min` : ''"
					/>
					<Card
						class="bg-red-600"
						title="Total hours ridden"
						icon="bx:hourglass"
						:value="Math.round((trip?.duration.total || 0) / 3600)"
					/>
				</div>
			</div>
			<div class="flex flex-col">
				<h1 class="relative z-10 font-bold text-2xl mb-4 pl-16">
					User Data
				</h1>
				<div
					class="
					relative z-10
					flex items-center justify-start
					w-full overflow-x-scroll gap-10
					px-16 pb-16"
				>
					<Card
						class="bg-amber-500"
						title="Subscribers"
						icon="ph:star-four-bold"
						:value="user?.type.subscriber || 0"
					/>
					<Card
						class="bg-indigo-500"
						title="Customers"
						icon="material-symbols:person-3-rounded"
						:value="user?.type.customer || 0"
					/>
					<Card
						v-if="user?.gender"
						class="bg-sky-500"
						title="Male users"
						icon="ic:round-male"
						:value="user.gender.male"
					/>
					<Card
						v-if="user?.gender"
						class="bg-pink-500"
						title="Female users"
						icon="ic:round-female"
						:value="user.gender.female"
					/>
					<Card
						v-if="user?.birth"
						class="bg-rose-500"
						title="Most common birth year"
						icon="bx:hourglass"
						:value="user.birth.mode"
						expand
					/>
					<Card
						v-if="user?.birth"
						class="bg-violet-500"
						title="Oldest user"
						icon="bx:hourglass"
						:value="user.birth.earliest"
					/>
					<Card
						v-if="user?.birth"
						class="bg-orange-500"
						title="Youngest user"
						icon="bx:hourglass"
						:value="user.birth.latest"
					/>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>

</style>
