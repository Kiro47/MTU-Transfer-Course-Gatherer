import {createAction} from 'redux-api-middleware';
import {ENDPOINT} from '../../lib/config';
import {
  GET_TRANSFER_COURSES_REQUEST,
  GET_TRANSFER_COURSES_SUCCESS,
  GET_TRANSFER_COURSES_ERROR
} from './types';

export const getCourses = () => createAction({
  endpoint: `${ENDPOINT}/api/courses/?limit=15000`,
  method: 'GET',
  types: [
    GET_TRANSFER_COURSES_REQUEST,
    GET_TRANSFER_COURSES_SUCCESS,
    GET_TRANSFER_COURSES_ERROR
  ]
});
