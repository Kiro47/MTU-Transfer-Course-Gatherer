import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'
import configureStore from './store/configureStore'
import Page from './ui/page'
import 'typeface-roboto';
import {
  Container
} from '@material-ui/core'


const store = configureStore()

render(
  <Provider store={store}>
    <Container>
      <Page />
    </Container>
  </Provider>,
  document.getElementById('root')
)
