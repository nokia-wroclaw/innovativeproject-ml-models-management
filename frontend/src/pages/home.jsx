import * as React from 'react';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';


const styles = (theme) =>
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
			padding: `${theme.spacing(1)}px ${theme.spacing(2)}px`,
		},
		link: {
			color: theme.palette.primary.main,
			textDecoration: 'none',
			'&:hover': {
				textDecoration: 'underline',
			},
		},
	});




class HomeC extends React.Component{

	render() {
		return (
			<main>
				<h3>My projects</h3>
			</main>
		);
	}
}

export const Home = withStyles(styles)(HomeC);
