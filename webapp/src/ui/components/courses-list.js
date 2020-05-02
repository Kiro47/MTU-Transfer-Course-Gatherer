import React, {useState, useEffect} from 'react';
import {
  TableContainer,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHead,
  TablePagination
} from '@material-ui/core';

const columns = [
  {id: 'course_name', label: 'Course Name'},
  {id: 'course_subject', label: 'Subject'},
  {id: 'course_id', label: 'Course Code'},
  {id: 'course_credits', label: 'Credits'},
  {id: 'transfer_state', label: 'State'},
  {id: 'transfer_college', label: 'College'}
];

const CoursesList = ({data}) => {
  const [displayedData, setDisplayedData] = useState(data);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(50);

  useEffect(() => {
    setDisplayedData(data.slice(rowsPerPage * page, rowsPerPage * (page + 1)));
  }, [rowsPerPage, page, data]);

  return (
    <Paper>
      <TableContainer>
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
            {displayedData.map(row => (
              <TableRow key={row.id} hover>
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
      </TableContainer>

      <TablePagination
        component="div"
        rowsPerPageOptions={[10, 50, 100, 200]}
        rowsPerPage={rowsPerPage}
        count={data.length}
        page={page}
        onChangePage={(_, newPage) => setPage(newPage)}
        onChangeRowsPerPage={event => setRowsPerPage(event.target.value)}
      />
    </Paper>
  );
};

export default React.memo(CoursesList);
