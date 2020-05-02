import React, {useState, useEffect} from 'react';
import {InputBase, CircularProgress, Paper, Box, InputAdornment} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import Skeleton from '@material-ui/lab/Skeleton';
import {useDebounce} from 'use-debounce';
import CoursesList from './components/courses-list';
import {useDispatch, useSelector} from 'react-redux';
import {getCourses} from '../actions';
import useFocus from '../utils/use-focus';

const Courses = () => {
  const dispatch = useDispatch();
  // Const queryRef = useRef(null);
  const [queryRef, setQueryFocus] = useFocus();

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

  // Focus query input after loading is finished
  useEffect(() => {
    if (courses.loading === false) {
      setQueryFocus();
    }
  }, [courses, setQueryFocus]);

  return (
    <div>
      <Paper>
        <Box p={2}>
          <InputBase
            fullWidth
            inputRef={queryRef} disabled={courses.loading}
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
        {courses.loading ? (
          <Skeleton/>
        ) : (
          <span>Matched {filteredCourses.length} out of {courses.total ? courses.total : 0} results</span>
        )}
      </Box>

      <CoursesList data={filteredCourses} loading={courses.loading}/>
    </div>
  );
};

export default Courses;
