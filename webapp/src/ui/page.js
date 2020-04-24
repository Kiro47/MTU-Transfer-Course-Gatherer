import React from 'react';
import {connect} from 'react-redux';
import {Grid, Typography, Link} from '@material-ui/core';

import Courses from './courses';

const Page = () => (
	<Grid container spacing={2}>
		<Grid item xs={12}>
			<Typography gutterBottom variant="h2">
				Approved Transfer Courses
			</Typography>

			<Typography gutterBottom variant="h4">
				at <Link href="https://mtu.edu" target="_blank" rel="noopener noreferrer">Michigan Tech</Link>
			</Typography>

			<Typography variant="subtitle1" align="right">
				Last updated <b>6 hours ago</b>
			</Typography>
		</Grid>

		<Grid item xs={12}>
			<Courses/>
		</Grid>
	</Grid>
);

function mapStateToProps(state) {
	return state;
}

const mapDispatchToProps = {
};

export default connect(
	mapStateToProps,
	mapDispatchToProps
)(Page);
