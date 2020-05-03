import React, {useState, useEffect} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import {InputBase, Backdrop, CircularProgress, Paper, Box, InputAdornment} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import ErrorIcon from '@material-ui/icons/Error';
import {useDebounce} from 'use-debounce';
import CoursesList from './components/courses-list';
import {useDispatch, useSelector} from 'react-redux';
import {getCourses} from '../actions';

const useStyles = makeStyles(() => ({
  backdrop: {
    zIndex: 1000
  }
}));

const Courses = () => {
  const dispatch = useDispatch();

  // Update courses on load
  useEffect(() => {
    dispatch(getCourses());
  }, [dispatch]);

  const [query, setQuery] = useState('');
  const [debouncedQuery] = useDebounce(query, 300, {maxWait: 2000});
  const courses = useSelector(state => state.courses);
  const [filteredCourses, setFilteredCourses] = useState([]);
  const [isFiltering, setIsFiltering] = useState(false);

  useEffect(() => {
    setIsFiltering(false);

    if (!courses.results) {
      setFilteredCourses([]);
      return;
    }

    const searchFilter = debouncedQuery.split(' ');

    setFilteredCourses(courses.results.filter(course => {
      const entry = Object.values(course);
      const entryString = entry.slice(0, entry.length);
      const modifiedEntryString = entryString.join().toLowerCase();
      return searchFilter.every(key => {
        return modifiedEntryString.includes(key.toLowerCase());
      });
    }));
  }, [debouncedQuery, courses]);

  const onQueryChange = event => {
    setQuery(event.target.value);

    setIsFiltering(true);
  };

  const classes = useStyles();

  return (
    <div>
      <Paper>
        <Box p={2}>
          <InputBase
            fullWidth autoFocus
            startAdornment={
              <InputAdornment position="start">
                <SearchIcon/>
              </InputAdornment>
            }
            endAdornment={
              isFiltering ? (
                <InputAdornment position="end">
                  <CircularProgress color="inherit"/>
                </InputAdornment>
              ) : null
            }
            placeholder="Start typing to filter by university name, course code, subject..." onChange={onQueryChange}/>
        </Box>
      </Paper>

      <Box mt={2} mb={2}>
        Matched {filteredCourses.length} out of {courses.total ? courses.total : 0} results
      </Box>

      <CoursesList data={filteredCourses}/>

      <Backdrop open={courses.loading === true || courses.error !== undefined} className={classes.backdrop}>
        {courses.error ? (
          <Paper>
            <Box p={4} textAlign="center">
              <ErrorIcon style={{fontSize: 40}} color="inherit"/>

              <p>Oops, something weird happened. The network request failed.</p>
            </Box>
          </Paper>
        ) : (
          <CircularProgress color="inherit"/>
        )}
      </Backdrop>
    </div>
  );
};

export default Courses;
