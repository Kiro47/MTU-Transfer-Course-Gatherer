import React from 'react'
import {connect} from 'react-redux'
import {getCourses} from '../actions/courses'
import {
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHead,
  Input
} from '@material-ui/core'

const columns = [
  { id: 'mtu_equiv.mtu_course_name', label:'Class Name'},
  { id: 'mtu_equiv.mtu_course_subject', label: 'Class'},
];

function handleChange(event: object) {
  let e = event;
  let searchKey = e.target.value.toLowerCase();
  let data = this.filterCourses(searchKey);
  setTimeout(function() {
    this.setState({ filtered: data })
  }.bind(this), 400)
}

class Courses extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      filtered: []
    }
    this.handleChange = handleChange.bind(this);
  }
  componentDidMount() {
    this.props.getCourses()
    this.setState({
      filtered: this.props.results
    });
  }

  static getDerivedStateFromProps(props, state) {
    if(state.filtered) {
      if(state.filtered.length !== props) {
        return state;
      }
    }
    state = {
      filtered: props.results
    };
    return state;
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
    let data = this.props.courses.results;
    if(this.state.filtered) {
      data = this.state.filtered;
    }
    console.log(this.state)
    if(!this.props.loading && data) {
      return (
        <div className="courses">
          <Input
            onChange={this.handleChange}
            fullWidth={true}
            placeholder="Search..."
            autoFocus={true}
          />
          <Table>
            <TableHead>
              <TableRow>
                {columns.map(column => (
                  <TableCell
                    key={column.id}
                  >
                    {column.label}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {data.map(row => (
                <TableRow key={row.id}>
                  <TableCell>{row.mtu_equiv.mtu_course_name}</TableCell>
                  <TableCell>
                    {row.mtu_equiv.mtu_subject} {row.mtu_equiv.mtu_course_id}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      )
    } else {
      return (
        <p>Loading...</p>
      )
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
