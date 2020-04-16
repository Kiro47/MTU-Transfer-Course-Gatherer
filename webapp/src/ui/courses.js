import React from 'react'
import {connect} from 'react-redux'
import {getCourses} from '../actions/courses'
import {
  Input,
  LinearProgress,
} from '@material-ui/core'

import CoursesList from './components/coursesList';


class Courses extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      filtered: [],
      loading: true,
      query: ""
    }
  }

  componentDidMount() {
    this.props.getCourses()
  }

  filterCourses = (filterKey) => {
    let filteredCourses = this.props.courses.results;
    if(!filteredCourses) return 0;
    filteredCourses = filteredCourses.filter((course) => {
      let searchString = JSON.stringify(course)
      return searchString.toLowerCase().indexOf(
        filterKey) !== -1
    })
    return filteredCourses;
  }

  handleChange = (event: object) => {
    let searchKey = event.target.value.toLowerCase();
    this.setState({ query: searchKey });
    let data = this.filterCourses(searchKey);
    setTimeout(function() {
      this.setState({ filtered: data })
    }.bind(this), 450)
  }

  render() {
    const courses = this.props.courses;
    const state = this.state;
    let data = courses.results;
    const filtered = state.filtered;
    if(filtered.length > 0 && filtered.length < data.length) {
      data = filtered;
    }
    return (
      <div className="courses">
        <Input
          value={state.query}
          onChange={this.handleChange}
          fullWidth={true}
          placeholder="Search..."
          autoFocus={true}
        />
        {data
          ? <CoursesList data={data} />
          : <LinearProgress />
        }
      </div>
    );
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
