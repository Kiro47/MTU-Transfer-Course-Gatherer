import React, {useState, useEffect, useCallback} from 'react';
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
import Skeleton from '@material-ui/lab/Skeleton';

const columns = [
  {id: 'course_name', label: 'Course Name'},
  {id: 'course_subject', label: 'Subject'},
  {id: 'course_id', label: 'Course Code'},
  {id: 'course_credits', label: 'Credits'},
  {id: 'transfer_state', label: 'State'},
  {id: 'transfer_college', label: 'College'}
];

const CoursesList = ({data, loading}) => {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(50);

  const getPromisedData = useCallback(() => {
    return loading ? [...new Array(rowsPerPage).keys()] : data;
  }, [loading, rowsPerPage, data]);

  const [displayedData, setDisplayedData] = useState(getPromisedData());

  useEffect(() => {
    setDisplayedData(getPromisedData().slice(rowsPerPage * page, rowsPerPage * (page + 1)));
  }, [rowsPerPage, page, getPromisedData]);

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
                <TableCell>{loading ? <Skeleton/> : <span>{row.course_name}</span>}</TableCell>
                <TableCell>{loading ? <Skeleton/> : <span>{row.course_subject}</span>}</TableCell>
                <TableCell>{loading ? <Skeleton/> : <span>{row.course_id}</span>}</TableCell>
                <TableCell>{loading ? <Skeleton/> : <span>{row.course_credits}</span>}</TableCell>
                <TableCell>{loading ? <Skeleton/> : <span>{row.transfer_state}</span>}</TableCell>
                <TableCell>{loading ? <Skeleton/> : <span>{row.transfer_college}</span>}</TableCell>
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
