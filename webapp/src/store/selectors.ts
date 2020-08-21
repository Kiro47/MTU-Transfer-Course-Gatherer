import {createSelector} from 'reselect';
import {RootState} from './types';

export const userSettings = (state: RootState) => state.userSettings;
export const transferCourses = (state: RootState) => state.transferCourses;

export const hasLightTheme = createSelector(userSettings, settings => settings.lightTheme);
