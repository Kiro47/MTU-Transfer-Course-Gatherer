import React from 'react';
import IconButton from '@material-ui/core/IconButton';
import Brightness4Icon from '@material-ui/icons/Brightness4';
import Brightness7Icon from '@material-ui/icons/Brightness7';
import {makeStyles} from '@material-ui/core/styles';
import {useDispatch, useSelector} from 'react-redux';
import {TOGGLE_THEME} from '../../store/user-settings/types';
import {hasLightTheme} from '../../store/selectors';

const useStyles = makeStyles({
  fixedButton: {
    position: 'absolute',
    top: 0,
    right: 0,
    margin: '1.5rem'
  }
});

const ThemeSelector = () => {
  const dispatch = useDispatch();
  const isLightTheme = useSelector(hasLightTheme);

  const classes = useStyles();

  return (
    <IconButton
      className={classes.fixedButton}
      color="primary"
      onClick={() => dispatch({type: TOGGLE_THEME})}
    >
      {isLightTheme ? (
        <Brightness7Icon/>
      ) : (
        <Brightness4Icon/>
      )}
    </IconButton>
  );
};

export default ThemeSelector;
