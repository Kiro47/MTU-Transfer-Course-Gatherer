import {createAction} from 'redux-api-middleware';
import {ENDPOINT} from './config';
import {
  GET_COURSES_REQUEST,
  GET_COURSES_SUCCESS,
  GET_COURSES_ERROR
} from './action-types';

export const getCourses = () => createAction({
  endpoint: `${ENDPOINT}/api/courses/?limit=11000`,
  method: 'GET',
  types: [
    GET_COURSES_REQUEST,
    GET_COURSES_SUCCESS,
    GET_COURSES_ERROR
  ]
});
