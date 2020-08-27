import {
  GET_TRANSFER_COURSES_REQUEST,
  GET_TRANSFER_COURSES_SUCCESS,
  GET_TRANSFER_COURSES_ERROR,
  TransferCoursesActionTypes,
  TransferCoursesState
} from './types';

const initialState: TransferCoursesState = {
  loading: false,
  results: [],
  count: 0,
  error: null
};

const reducer = (
  state = initialState,
  action: TransferCoursesActionTypes
): TransferCoursesState => {
  switch (action.type) {
    case GET_TRANSFER_COURSES_REQUEST:
      return {...state, loading: true};
    case GET_TRANSFER_COURSES_SUCCESS: {
      return {
        ...state,
        results: action.payload.results,
        count: action.payload.count,
        loading: false,
        error: null
      };
    }

    case GET_TRANSFER_COURSES_ERROR:
      return {
        ...state,
        error: action.payload,
        loading: false
      };
    default:
      return state;
  }
};

export default reducer;
