import React, {useState, useEffect} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import {InputBase, Backdrop, CircularProgress, Paper, Box, InputAdornment} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import CoursesList from './components/courses-list';
import {useDispatch, useSelector} from 'react-redux';
import {getCourses} from '../store/actions/courses';

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
	const courses = useSelector(state => state.courses);
	const [filteredCourses, setFilteredCourses] = useState([]);

	useEffect(() => {
		if (!courses.results) {
			setFilteredCourses([]);
			return;
		}

		const searchFilter = query.split(' ');

		setFilteredCourses(courses.results.filter(course => {
			const entry = Object.values(course);
			const entryString = entry.slice(0, entry.length);
			const modifiedEntryString = entryString.join().toLowerCase();
			return searchFilter.every(key => {
				return modifiedEntryString.includes(key.toLowerCase());
			});
		}));
	}, [query, courses]);

	const classes = useStyles();

	return (
		<div>
			<Paper>
				<Box p={2}>
					<InputBase
						fullWidth autoFocus value={query}
						startAdornment={
							<InputAdornment position="start">
								<SearchIcon/>
							</InputAdornment>
						}
						placeholder="Start typing to filter by university name, course code, subject..." onChange={event => setQuery(event.target.value)}/>
				</Box>
			</Paper>

			<Box mt={2} mb={2}>
				Matched {filteredCourses.length} out of {courses.total ? courses.total : 0} results
			</Box>

			<CoursesList data={filteredCourses}/>

			<Backdrop open={courses.loading} className={classes.backdrop}>
				<CircularProgress color="inherit"/>
			</Backdrop>
		</div>
	);
};

export default Courses;
