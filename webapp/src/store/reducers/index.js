import {combineReducers} from 'redux';
import courses from './courses';
import userSettings from './user-settings';

export default combineReducers({
  courses,
  userSettings
});
