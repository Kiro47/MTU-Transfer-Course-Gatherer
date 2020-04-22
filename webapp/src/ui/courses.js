import React from 'react'
import CoursesList from './components/coursesList';
import styled from 'styled-components';
import {
  Input,
  LinearProgress
} from '@material-ui/core'
import { connect } from 'react-redux'
import { getCourses } from '../actions/courses'

const Span = styled.span`
  font-size: 10px;
  text-align: left;
  display: flex;
  justify-content: left,
  align-content: left,
  text-align: left
`;


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
    if(!this.props.courses.results) return [];
    let filteredCourses = this.props.courses.results;
    let searchFilter = filterKey.split(' ');
    filteredCourses = filteredCourses.filter(course => {
      let entry = Object.values(course);
      let entryString = entry.slice(0, entry.length)
      let modifiedEntryString = entryString.join().toLowerCase();
      return searchFilter.every(key => {
        return modifiedEntryString.includes(key.toLowerCase())
      });
    });
    return filteredCourses;
  }

  handleChange = (event: object) => {
    let searchKey = event.target.value.toLowerCase();
    this.setState({ query: searchKey });
    let data = this.filterCourses(searchKey);
    this.setState({ filtered: data })
  }


  render() {
    const courses = this.props.courses;
    const state = this.state;
    const filtered = state.filtered;
    const totalData = courses.total;
    let data = courses.results;
    if(filtered.length > 0 && filtered.length < data.length) {
      data = filtered;
    }
    return (
      <div className="courses">
        <Span>
          Matched {filtered.length} results
        </Span>
        <Span> Got {totalData ? totalData : 0} results </Span>
        <Input
          value={state.query}
          onChange={(e) => this.handleChange(e)}
          fullWidth={true}
          placeholder="Search..."
          autoFocus={true}
        />
        {!this.props.courses.loading
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
