import {combineReducers} from 'redux';
import transferCourses from './transfer-courses/reducers';
import userSettings from './user-settings/reducers';

export default combineReducers({
  transferCourses,
  userSettings
});
