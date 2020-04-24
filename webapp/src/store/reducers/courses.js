import {
	GET_COURSES_REQUEST,
	GET_COURSES_SUCCESS,
	GET_COURSES_ERROR
} from '../actions/courses';

const initialState = {
	loading: true
};

export default function (state = initialState, action) {
	switch (action.type) {
		case GET_COURSES_REQUEST:
			return {...state, loading: true};
		case GET_COURSES_SUCCESS: {
			const results = action.payload.results;
			const next = action.payload.next;
			const total = action.payload.count;

			return {
				...state,
				results,
				next,
				total,
				loading: false
			};
		}

		case GET_COURSES_ERROR:
			return {
				...state,
				error: action.payload,
				loading: false
			};
		default:
			return state;
	}
}
