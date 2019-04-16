import * as React from 'react';
import {
	Button, Dialog, DialogActions,
	DialogContent, DialogContentText,
	DialogTitle, Typography, Divider, TextField,
	FormControl, FormControlLabel, FormLabel, Paper, Checkbox, Input, InputLabel, Avatar, ExpansionPanel, ExpansionPanelSummary
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { ExpandMore as ExpandMoreIcon } from '@material-ui/icons';


const styles = (theme: Theme) =>
	createStyles({
		root: {
			width: '100%',
		},
		heading: {
			fontSize: theme.typography.pxToRem(15),
		},
		secondaryHeading: {
			fontSize: theme.typography.pxToRem(15),
			color: theme.palette.text.secondary,
		},
		icon: {
			verticalAlign: 'bottom',
			height: 20,
			width: 20,
		},
		details: {
			alignItems: 'center',
		},
		column: {
			flexBasis: '33.33%',
		},
		helper: {
			borderLeft: `2px solid ${theme.palette.divider}`,
			padding: `${theme.spacing.unit}px ${theme.spacing.unit * 2}px`,
		},
		link: {
			color: theme.palette.primary.main,
			textDecoration: 'none',
			'&:hover': {
				textDecoration: 'underline',
			},
		},
	});



type State = {
};

class HomeC extends React.Component<WithStyles<typeof styles>, State> {

	render() {
		const { classes } = this.props;

		return (
			<main>
				<h3>My projects</h3>
			</main>
		);
	}
}

export const Home = withStyles(styles)(HomeC);
