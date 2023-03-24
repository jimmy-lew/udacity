/* eslint-disable no-mixed-spaces-and-tabs */
import type { MarkdownParsedContent } from '@nuxt/content/dist/runtime/types'

export { }

declare global {
    type Nullable<T> = T | null

	interface Prompt {
		prompt: string
		name: string
		options: string[]
	}

	interface PromptAnswer {
		name: string
		value: string
	}

	interface QueryData {
		city: string
		filter: string
		month: string
		day: string
	}
}