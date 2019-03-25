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

const styles = (theme: Theme) =>
	createStyles({
		main: {
			width: 'auto',
			display: 'block', // Fix IE 11 issue.
			marginLeft: theme.spacing.unit * 3,
			marginRight: theme.spacing.unit * 3,
			[theme.breakpoints.up(400 + theme.spacing.unit * 3 * 2)]: {
				width: 400,
				marginLeft: 'auto',
				marginRight: 'auto',
			},
		},
		paper: {
			marginTop: theme.spacing.unit * 8,
			display: 'flex',
			flexDirection: 'column',
			alignItems: 'center',
			padding: `${theme.spacing.unit * 2}px ${theme.spacing.unit * 3}px ${theme.spacing.unit * 3}px`,
		},
		avatar: {
			margin: theme.spacing.unit,
			backgroundColor: theme.palette.secondary.main,
		},
		form: {
			width: '100%', // Fix IE 11 issue.
			marginTop: theme.spacing.unit,
		},
		submit: {
			marginTop: theme.spacing.unit * 3,
		},
		logo:{
			height:"7rem",
			width:"auto",
			marginTop:"1rem",
			marginBottom:"2rem",
		}
	});

type State = {
};

class AccountC extends React.Component<WithStyles<typeof styles>, State> {

	render() {
		const { classes } = this.props;

		return (
			<main className={classes.main}>
				<Paper className={classes.paper}>
					<Logo className={classes.logo}/>
					<Typography component="h1" variant="h5">
						Sign in
        </Typography>
					<form className={classes.form}>
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="email">Email Address</InputLabel>
							<Input id="email" name="email" autoComplete="email" autoFocus />
						</FormControl>
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="password">Password</InputLabel>
							<Input name="password" type="password" id="password" autoComplete="current-password" />
						</FormControl>
						<FormControlLabel
							control={<Checkbox value="remember" color="primary" />}
							label="Remember me"
						/>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
						>
							Sign in
          </Button>
					</form>
				</Paper>
			</main>
		);
	}
}

export const Account = withStyles(styles)(AccountC);
