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

function customSearch(obj, search) {
  let searchKey = search.toLowerCase();
  let searchArrays = obj.map(v => {
    let intMap = [];
    let keys = Object.keys(v)
    let myMap = keys.map(k => {
      if(typeof(v[k]) === 'object') {
        let subkeys = Object.keys(v[k])
        let subMap = subkeys.map(sk => {
          return v[k][sk]
        })
        return subMap;
      } else {
        return v[k]
      }
    })
    let savedValue = myMap[1];
    delete myMap[1];
    intMap.push(...myMap, ...savedValue)
    return intMap;
  })
  console.log(searchArrays.filter(a=>a.includes(searchKey)))
}

function handleChange(event: object) {
  let e = event;
  let coursesObjects = this.props.courses.results;
  let data = customSearch(coursesObjects, e.target.value);
  this.setState({
    filtered: data
  });
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

  render() {
    let data = this.props.courses.results;
    if(this.state.filtered) {
      data = this.state.filtered;
    }
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
