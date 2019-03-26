import * as React from 'react';
import {
	Button, Dialog, DialogActions,
	DialogContent, DialogContentText,
	DialogTitle, Typography, Divider, TextField, CssBaseline
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import createStyles from '@material-ui/core/styles/createStyles';
import withStyles, { WithStyles } from '@material-ui/core/styles/withStyles';
import withRoot from './withRoot';
import { Login } from './pages/login';
import { Account } from './pages/account';
import { Home } from './pages/home';
import { Project } from './pages/project';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

const styles = (theme: Theme) =>
	createStyles({
		root: {
			textAlign: 'center',
		},
	});

type State = {
};

class App extends React.Component<WithStyles<typeof styles>, State> {

	render() {
		const classes = this.props.classes;
		return (
			<div className={classes.root}>
				<CssBaseline />		
				<Router>
					<Route path="/login" component={Login} />
					<Route path="/account" component={Account} />
					<Route
						path="/project/:projectId"
						component={Project}
					/>
					<Route exact path="/" component={Home} />
				</Router>		
			</div>
		);
	}
}

export default withRoot(withStyles(styles)(App));
