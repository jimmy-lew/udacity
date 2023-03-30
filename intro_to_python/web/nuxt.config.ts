export default defineNuxtConfig({
	modules: [
		'@nuxtjs/tailwindcss',
		'@nuxt/content',
		'nuxt-icon',
	],
	content: {
		documentDriven: {
			surround: false,
			injectPage: false,
		},
	},
	app: {
		head: {
			charset: 'utf-16',
			viewport: 'width=device-width, initial-scale=1',
			title: 'Udacity Project',
			meta: [
				{ name: 'description', content: '' },
			],
			link: [
				{ rel: 'stylesheet', href: 'https://rsms.me/inter/inter.css' },
			],
		},
	},
})
