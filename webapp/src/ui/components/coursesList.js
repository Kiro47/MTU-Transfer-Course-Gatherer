import React from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHead,
} from '@material-ui/core'

const columns = [
  { id: 'course_name', label: 'Course Name'},
  { id: 'course_subject', label: 'Subject'},
  { id: 'course_id', label: 'Course Code'},
  { id: 'course_credits', label: 'Credits'},
  { id: 'transfer_state', label: 'State'},
  { id: 'transfer_college', label: 'College'},
];

class CoursesList extends React.Component {
  render() {
    let data = this.props.data;
    data = data.slice(0, 50)
    return (
      <div className="courses-list">
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
                <TableCell>{row.course_name}</TableCell>
                <TableCell>{row.course_subject}</TableCell>
                <TableCell>{row.course_id}</TableCell>
                <TableCell>{row.course_credits}</TableCell>
                <TableCell>{row.transfer_state}</TableCell>
                <TableCell>{row.transfer_college}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    )
  }
}

export default CoursesList;
