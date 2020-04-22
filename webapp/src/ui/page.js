import React from 'react'
import {connect} from 'react-redux'
import {
  Card,
  CardContent,
  Grid,
  Paper,
} from '@material-ui/core'

import Courses from './courses';


const cardStyle = {
  fontSize: 40,
  justifyContent: 'center',
  alignContent: 'center',
  textAlign: 'center'
};

class Page extends React.Component {
  render() {
    return (
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Paper>
            <Card>
              <CardContent style={cardStyle}>
                Course Gather
              </CardContent>
            </Card>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper>
            <Card>
              <CardContent style={cardStyle}>
                <Courses />
              </CardContent>
            </Card>
          </Paper>
        </Grid>
      </Grid>
    )
  }
}

function mapStateToProps(state) {
  return state
}
const mapDispatchToProps = {
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Page)
