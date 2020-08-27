import {UserSettingsState} from './user-settings/types';
import {TransferCoursesState} from './transfer-courses/types';

export interface RootState {
  userSettings: UserSettingsState;
  transferCourses: TransferCoursesState;
}
