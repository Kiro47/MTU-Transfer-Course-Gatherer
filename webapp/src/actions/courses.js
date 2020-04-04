import {RSAA} from 'redux-api-middleware'

export const GET_COURSES_REQUEST = 'GET_COURSES_REQUEST'
export const GET_COURSES_SUCCESS = 'GET_COURSES_SUCCESS'
export const GET_COURSES_ERROR = 'GET_COURSES_ERROR'

export const getCourses = (options = {}) => dispatch => {
  return dispatch ({
    [RSAA]: {
      endpoint: `http://localhost:8000/api/courses/?limit=11000`,
      method: 'GET',
      types: [
        'GET_COURSES_REQUEST',
        'GET_COURSES_SUCCESS',
        'GET_COURSES_ERROR'
      ]
    }
  })
}
