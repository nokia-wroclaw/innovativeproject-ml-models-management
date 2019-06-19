import * as React from 'react';
import {
	Button, Typography, FormControl, Paper, Input, InputLabel, SnackbarContent
} from '@material-ui/core';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { LockOutlined as LockOutlinedIcon, Error as ErrorIcon } from '@material-ui/icons';
import {Auth} from "../utils/connect"

const styles = (theme) =>
	createStyles({
	});

class RegisterComponent extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			login: "",
			password: "",
			name: "",
			state: "initial",
			msg:""
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
		const { login, name, password } = this.state;
		const response = await Auth.Register(  );
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
					</div>
				</Paper>
			</main>
		);
	}
}

export const Register = withStyles(styles)(RegisterComponent);
