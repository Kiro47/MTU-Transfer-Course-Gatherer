import React from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHead,
  TablePagination
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
  constructor(props) {
    super(props);
    this.state = {
      page: 0,
      rowsPerPage: 100
    }
  }
    handleChangePage = (event, newPage) => {
      const oldPage = this.state.page;
      this.setState({ page: newPage, oldPage: oldPage })
    };
    handleChangeRowsPerPage = (event) => {
      this.setState({ rowsPerPage: event.target.value })
    };

  render() {
    let data = this.props.data;
    const total = data.length;
    let page = this.state.page;
    let rowsPerPage = this.state.rowsPerPage;
    let startRange = rowsPerPage * page;
    let endRange = (page + 1) * rowsPerPage;

    data = data.slice(startRange, endRange);

    return (
      <div className="courses-list">
        <TablePagination
          component="div"
          rowsPerPageOptions={[100, 200]}
          rowsPerPage={rowsPerPage}
          count={total}
          page={page}
          onChangePage={this.handleChangePage}
          onChangeRowsPerPage={this.handleChangeRowsPerPage}

        />

        <Table stickyHeader>
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