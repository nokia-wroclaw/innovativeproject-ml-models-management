import * as React from 'react';
import { Typography } from '@material-ui/core';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';

const styles = (theme) =>
	createStyles({
		
	});

class AccountC extends React.Component {

	render() {
		return (
			<main>
				<h1><Typography>Account</Typography></h1>
			</main>
		);
	}
}

export const Account = withStyles(styles)(AccountC);
