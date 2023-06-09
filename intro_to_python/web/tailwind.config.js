const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./components/*.{vue,js}',
		'./components/**/*.{vue,js}',
		'./layouts/**/*.{vue,js}',
		'./layouts/*.{vue,js}',
		'./pages/*.vue',
		'./pages/**/*.vue',
		'./plugins/**/*.{js,ts}',
		'./*.{vue,js,ts}',
		'./nuxt.config.{js,ts}',
	],
	darkMode: 'class',
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter var', ...defaultTheme.fontFamily.sans],
			},
			content: {
				default: '""',
			},
			keyframes: {
				expand: {
					'0%': { transform: 'scale(1)' },
					'100%': { transform: 'scale(1.05)' },
				},
			},
			animation: {
				expand: 'expand 0.5s ease-in-out',
			},
			colors: {
				error: '#fa5152',
			},
			backgroundImage: {
				'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
			},
			borderRadius: {
				inherit: 'inherit',
			},
		},
	},
	safelist: [
		'p-2',
	],
	plugins: [
		function ({ addVariant }) {
			addVariant('child', '& > *')
			addVariant('child-hover', '& > *:hover')
			addVariant('child-focus', '& > *:focus')
		},
	],
}
