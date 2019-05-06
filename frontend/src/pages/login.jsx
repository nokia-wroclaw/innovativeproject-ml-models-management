import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Checkbox, Input, InputLabel, SnackbarContent
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { TransformRounded as Logo, LockOutlined as LockOutlinedIcon, Error as Icon } from '@material-ui/icons';
import {Auth, LoginResponse, Response} from "../utils/connect"

const styles = (theme) =>
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
		logo: {
			height: "7rem",
			width: "auto",
			marginTop: "1rem",
			marginBottom: "2rem",
		},
		snackbar: {
			backgroundColor: theme.palette.error.dark,
		},
		icon: {
		  fontSize: 20,
		  opacity: 0.9,
		  marginRight: theme.spacing.unit,
		},
		message: {
		  display: 'flex',
		  alignItems: 'center',
		},
	});

class LoginComponent extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			username: "",
			password: "",
			reamember: true,
			error: ""
		}
	}
	handle = (event) => {
		const target = event.target;
		const value = target.type === 'checkbox' ? target.checked : target.value;
		const name = target.name;
		this.setState({
		  [name]: value
		});
	}
	send = async () => {
		const { username, password, reamember } = this.state
		const response = await Auth.login( username, password, reamember)
		if( !response ) throw new Error("we're in trouble, deep trouble")
		response.errorDescription = response.errorDescription || "";
		this.setState({error:response.errorDescription})
		return;
	}
	render() {
		const { classes } = this.props;
		let alert = "";
		if(this.state.error){
			alert = (<SnackbarContent
			className={classes.snackbar}
			aria-describedby="client-snackbar"
			message={
				<span id="client-snackbar" className={classes.message}>
					<Icon className={classes.icon} />
					{this.state.error}
				</span>
			}
			/>)
		}
		return (
			<main className={classes.main}>
				<Paper className={classes.paper}>
					<Logo className={classes.logo} />
					<Typography component="h1" variant="h5">
						Sign in
        			</Typography>
					  { alert }
					<div className={classes.form} >
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="email">Email Address</InputLabel>
							<Input onChange={this.handle}  value={this.state.username} id="email" name="username" autoComplete="email" autoFocus />
						</FormControl>
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="password">Password</InputLabel>
							<Input onChange={this.handle} value={this.state.password} name="password" type="password" id="password" autoComplete="current-password" />
						</FormControl>
						<FormControlLabel
							control={<Checkbox onChange={this.handle}  checked={this.state.reamember} name="reamember" value="remember" color="primary" />}
							label="Remember me"
						/>
						<Button
							onClick={this.send}
							type="button"
							fullWidth
							variant="contained"
							color="primary"
							className={classes.submit}
						>
							Sign in
          			</Button>
					</div>
				</Paper>
			</main>
		);
	}
}

export const Login = withStyles(styles)(LoginComponent);