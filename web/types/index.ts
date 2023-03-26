/* eslint-disable no-mixed-spaces-and-tabs */

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

    interface QueryBody {
    	city: string
    	filter: string
    	month: string
    	day: string
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
}
