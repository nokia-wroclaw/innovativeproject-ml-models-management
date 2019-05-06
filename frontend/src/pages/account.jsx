import * as React from 'react';
import {
	Button, Dialog, DialogActions,
	DialogContent, DialogContentText,
	DialogTitle, Typography, Divider, TextField,
	FormControl, FormControlLabel, FormLabel, Paper, Checkbox, Input, InputLabel, Avatar
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { TransformRounded as Logo , LockOutlined as LockOutlinedIcon} from '@material-ui/icons';

const styles = (theme) =>
	createStyles({
		
	});

class AccountC extends React.Component {

	render() {
		const { classes } = this.props;

		return (
			<main>
				<h1><Typography>Account</Typography></h1>
			</main>
		);
	}
}

export const Account = withStyles(styles)(AccountC);
