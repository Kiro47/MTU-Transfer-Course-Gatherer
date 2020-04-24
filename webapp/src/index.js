import React from 'react';
import {render} from 'react-dom';
import {Provider} from 'react-redux';
import configureStore from './store/configure-store';
import Page from './ui/page';
import {Container} from '@material-ui/core';
import CssBaseline from '@material-ui/core/CssBaseline';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import {createMuiTheme, ThemeProvider} from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
// eslint-disable-next-line import/no-unassigned-import
import 'typeface-roboto';

const store = configureStore();

const App = () => {
	const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

	const theme = React.useMemo(
		() =>
			createMuiTheme({
				palette: {
					type: prefersDarkMode ? 'dark' : 'light'
				}
			}),
		[prefersDarkMode]
	);

	return (
		<Provider store={store}>
			<ThemeProvider theme={theme}>
				<CssBaseline/>

				<Container>
					<Box marginTop={8}>
						<Page/>
					</Box>
				</Container>
			</ThemeProvider>
		</Provider>
	);
};

render(<App/>, document.querySelector('#root'));
