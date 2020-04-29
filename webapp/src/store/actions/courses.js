import {createAction} from 'redux-api-middleware';
import {ENDPOINT} from '../../config';

export const GET_COURSES_REQUEST = 'GET_COURSES_REQUEST';
export const GET_COURSES_SUCCESS = 'GET_COURSES_SUCCESS';
export const GET_COURSES_ERROR = 'GET_COURSES_ERROR';

export const getCourses = () => createAction({
  endpoint: `${ENDPOINT}/api/courses/?limit=11000`,
  method: 'GET',
  types: [
    'GET_COURSES_REQUEST',
    'GET_COURSES_SUCCESS',
    'GET_COURSES_ERROR'
  ]
});
