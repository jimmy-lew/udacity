<script setup lang="ts">

</script>

<template>
	<div class="rounded-lg bg-white my-shadow px-8 py-2 font-bold">
		<slot />
	</div>
</template>

<style scoped>
.my-shadow {
	box-shadow: 0px 22px 56px rgba(180, 155, 190, 0.22);
}
</style>
