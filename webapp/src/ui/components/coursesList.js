import React from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHead,
} from '@material-ui/core'

const columns = [
  { id: 'mtu_equiv.mtu_course_name', label:'Class Name'},
  { id: 'mtu_equiv.mtu_course_subject', label: 'Subject'},
  { id: 'mtu_equiv.mtu_course_id', label: 'Class Code'},
  { id: 'mtu_equiv.mtu_credits', label: 'Credits'},
  { id: 'transfer_course_college_code.college_name', label: 'transfer college'},
  { id: 'transfer_course_state_code.state_name', label: 'transfer state'},
  { id: 'transfer_course_credit', label: 'transfer course credit'},
];

class CoursesList extends React.Component {
  render() {
    let data = this.props.data;
    data = data.slice(0, 50)
    return (
      <div className="courses">
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
                <TableCell>{row.mtu_equiv.mtu_subject}</TableCell>
                <TableCell>{row.mtu_equiv.mtu_course_id}</TableCell>
                <TableCell>{row.mtu_equiv.mtu_credits}</TableCell>
                <TableCell>{row.transfer_course_college_code.college_name}</TableCell>
                <TableCell>{row.transfer_course_state_code.state_name}</TableCell>
                <TableCell>{row.transfer_course_credit}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    )
  }
}

export default CoursesList;
