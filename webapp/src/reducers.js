import {combineReducers} from 'redux';
import {
  GET_COURSES_REQUEST,
  GET_COURSES_SUCCESS,
  GET_COURSES_ERROR,
  TOGGLE_THEME
} from './action-types';

// Store.courses
const courses = function (state = {loading: true}, action) {
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
};

const settingsInitalState = {
  lightTheme: window.localStorage.getItem('theme') ? window.localStorage.getItem('theme') === 'light' : !window.matchMedia('(prefers-color-scheme: dark)').matches
};

const userSettings = function (state = settingsInitalState, action) {
  switch (action.type) {
    case TOGGLE_THEME:
      window.localStorage.setItem('theme', state.lightTheme ? 'dark' : 'light');

      return {
        lightTheme: !state.lightTheme
      };
    default:
      return state;
  }
};

export default combineReducers({
  courses,
  userSettings
});
