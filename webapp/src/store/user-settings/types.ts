export interface UserSettingsState {
  lightTheme: boolean;
}

export const TOGGLE_THEME = 'TOGGLE_THEME';

interface ToggleThemeAction {
  type: typeof TOGGLE_THEME;
}

export type UserSettingsActionTypes = ToggleThemeAction;
