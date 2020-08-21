import {UserSettingsState, UserSettingsActionTypes, TOGGLE_THEME} from './types';

const initialState: UserSettingsState = {
  lightTheme: window.localStorage.getItem('theme') ? window.localStorage.getItem('theme') === 'light' : !window.matchMedia('(prefers-color-scheme: dark)').matches
};

export default (state = initialState, action: UserSettingsActionTypes) => {
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
