import * as React from 'react';
import {
	Button, Typography, FormControl, Paper, Input, InputLabel, SnackbarContent
} from '@material-ui/core';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { LockOutlined as LockOutlinedIcon, Error as ErrorIcon } from '@material-ui/icons';
import {Auth} from "../utils/connect"
import { Link } from 'react-router-dom'

const styles = (theme) =>
	createStyles({
		main: {
			width: 'auto',
			display: 'block', // Fix IE 11 issue.
			marginLeft: theme.spacing(3),
			marginRight: theme.spacing(3),
			[theme.breakpoints.up(400 + theme.spacing(3) * 2)]: {
				width: 400,
				marginLeft: 'auto',
				marginRight: 'auto',
			},
		},
		paper: {
			marginTop: theme.spacing(8),
			display: 'flex',
			flexDirection: 'column',
			alignItems: 'center',
			padding: `${theme.spacing(2)}px ${theme.spacing(3)}px ${theme.spacing(3)}px`,
		},
		avatar: {
			margin: theme.spacing(1),
			backgroundColor: theme.palette.secondary.main,
		},
		form: {
			width: '100%', // Fix IE 11 issue.
			marginTop: theme.spacing(1),
		},
		submit: {
			marginTop: theme.spacing(3),
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
		  marginRight: theme.spacing(1),
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
		const { username, password } = this.state;
		const response = await Auth.login( username, password );
		if( !response ){
			this.setState({error:"We were unable to communicate with server :c"});
			return;
		}
		if( response.message ){
			this.setState({error:response.message});
			return;
		}
		if(response.successful) this.props.history.goBack();
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
					<ErrorIcon className={classes.icon} />
					{this.state.error}
				</span>
			}
			/>)
		}
		return (
			<main className={classes.main}>
				<Paper className={classes.paper}>
					<LockOutlinedIcon className={classes.logo} />
					<Typography component="h1" variant="h5">
						Sign in
        			</Typography>
					  { alert }
					<div onKeyDownCapture={(e)=>{if(e.key==='Enter') this.send()}} className={classes.form} >
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="email">Email Address</InputLabel>
							<Input onChange={this.handle} value={this.state.username} id="email" name="username" autoComplete="email" autoFocus />
						</FormControl>
						<FormControl margin="normal" required fullWidth>
							<InputLabel htmlFor="password">Password</InputLabel>
							<Input onChange={this.handle} value={this.state.password} name="password" type="password" id="password" autoComplete="current-password" />
						</FormControl>
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
						<Button
							type="button"
							fullWidth
							variant="outlined"
							color="primary"
							className={classes.submit}
							component={Link} to="/register" 
						>
							Register
          			</Button>
					</div>
				</Paper>
			</main>
		);
	}
}

export const Login = withStyles(styles)(LoginComponent);
