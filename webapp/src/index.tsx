import React from 'react';
import {render} from 'react-dom';
import {Provider, useSelector} from 'react-redux';
import {Container} from '@material-ui/core';
import CssBaseline from '@material-ui/core/CssBaseline';
import {createMuiTheme, ThemeProvider} from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import 'typeface-roboto';
import configureStore from './store/configure-store';
import {hasLightTheme} from './store/selectors';
import Page from './ui/page';
import ThemeSelector from './ui/components/theme-selector';

const store = configureStore();

const App = () => {
  const isLightTheme = useSelector(hasLightTheme);

  const theme = React.useMemo(
    () =>
      createMuiTheme({
        palette: {
          type: isLightTheme ? 'light' : 'dark'
        }
      }),
    [isLightTheme]
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline/>

      <Container>
        <ThemeSelector/>
        <Box marginTop={8}>
          <Page/>
        </Box>
      </Container>
    </ThemeProvider>
  );
};

const AppWithRedux = () => (
  <Provider store={store}>
    <App/>
  </Provider>
);

render(<AppWithRedux/>, document.querySelector('#root'));
