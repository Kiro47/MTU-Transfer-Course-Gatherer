import React from 'react'
import {connect} from 'react-redux'
import {getCourses} from '../actions/courses'
import {
  Input
} from '@material-ui/core'

import CoursesList from './components/coursesList';

function handleChange(event: object) {
  let e = event;
  let searchKey = e.target.value.toLowerCase();
  this.setState({ query: searchKey });
  let data = this.filterCourses(searchKey);
  setTimeout(function() {
    this.setState({ filtered: data })
  }.bind(this), 450)
}

class Courses extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      filtered: [],
      loading: true,
      query: ""
    }
    this.handleChange = handleChange.bind(this);
  }

  componentDidMount() {
    this.props.getCourses()
  }

  filterCourses = (filterKey) => {
    let filteredCourses = this.props.courses.results;
    filteredCourses = filteredCourses.filter((course) => {
      let searchString = JSON.stringify(course)
      return searchString.toLowerCase().indexOf(
        filterKey) !== -1
    })
    return filteredCourses;
  }

  render() {
    const courses = this.props.courses;
    const state = this.state;
    const loading = courses.loading;
    let data = courses.results;
    const filtered = state.filtered;
    if(filtered.length > 0 && filtered.length < data.length) {
      data = filtered;
    }
    if(!loading) {
      return (
        <div>
          <Input
            value={state.query}
            onChange={this.handleChange}
            fullWidth={true}
            placeholder="Search..."
            autoFocus={true}
          />
          <CoursesList data={data} />
        </div>
      );
    } else {
      return (<p> Loading... </p>);
    }
  }
}

function mapStateToProps(state) {
  return state
}

const mapDispatchToProps = {
  getCourses
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Courses)
