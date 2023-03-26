/* eslint-disable no-mixed-spaces-and-tabs */

export { }

declare global {
    type Nullable<T> = T | null

    type RoundTypes = SizeTypes
    type SizeTypes = 'none' | 'sm' | 'md' | 'lg' | 'xl' | '2xl' | '3xl' | 'full'

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

    interface QueryResponse {
    	[key: string]: string
    }

    interface StatusCheck {
    	code: number
    	status: string
    }

    interface ValueCount<T extends string | number> {
    	value: T
    	count: number
    }

    interface TimeResponse {
    	hour: ValueCount<number>
    	day: ValueCount<string>
    	month: ValueCount<number>
    }

    interface TripResponse {
    	duration: {
    		total: number
    		avg: number
    	}
    	station: {
    		start: ValueCount<string>
    		end: ValueCount<string>
    	}
    	full_trip: string
    	count: number
    }

    interface UserResponse {
    	type: {
    		subscriber: number
    		customer: number
    	}
    	gender?: {
    		male: number
    		female: number
    	}
    	birth?: {
    		earliest: number
    		latest: number
    		mode: number
    	}
    }

 	interface QueryResponse_ {
    	time: TimeResponse
    	trip: TripResponse
    	user: UserResponse
    }
}
