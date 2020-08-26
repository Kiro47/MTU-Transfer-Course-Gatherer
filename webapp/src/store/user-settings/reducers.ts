import {UserSettingsState, UserSettingsActionTypes, TOGGLE_THEME} from './types';

const isInitialThemeLight = () => {
  const storedTheme = window.localStorage.getItem('theme');

  if (storedTheme === 'light') {
    return true;
  }

  return !window.matchMedia('(prefers-color-scheme: dark)').matches;
};

const initialState: UserSettingsState = {
  lightTheme: isInitialThemeLight()
};

const reducer = (state = initialState, action: UserSettingsActionTypes) => {
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

export default reducer;
