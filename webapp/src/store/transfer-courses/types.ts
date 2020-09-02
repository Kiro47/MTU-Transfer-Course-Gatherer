import {RequestError, ApiError} from 'redux-api-middleware';
import {APITransferCourse, APIResult} from '../../lib/api-types';

export const GET_TRANSFER_COURSES_REQUEST = 'GET_TRANSFER_COURSES_REQUEST';
export const GET_TRANSFER_COURSES_SUCCESS = 'GET_TRANSFER_COURSES_SUCCESS';
export const GET_TRANSFER_COURSES_ERROR = 'GET_TRANSFER_COURSES_ERROR';

export interface TransferCoursesState {
  loading: boolean;
  results: APITransferCourse[];
  count: number;
  error: Error | null;
}

interface RequestAction {
  type: typeof GET_TRANSFER_COURSES_REQUEST;
}

interface SuccessAction {
  type: typeof GET_TRANSFER_COURSES_SUCCESS;
  payload: APIResult<APITransferCourse>;
}

interface ErrorAction {
  type: typeof GET_TRANSFER_COURSES_ERROR;
  payload: RequestError | ApiError;
}

export type TransferCoursesActionTypes = RequestAction | SuccessAction | ErrorAction;
