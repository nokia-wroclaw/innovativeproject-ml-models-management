import * as React from 'react';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { Paper, Container, CircularProgress } from '@material-ui/core';
import { Row,Col } from '../components/layout'
import { CredsStore } from '../user/CredsStore'

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

function ProjectsTile(props){
	const {project} = props;
	return <Paper>
		<Col>
			<Row>a</Row>
			<Row>b</Row>
			<Row>c</Row>
		</Col>
	</Paper>
}

class MyProjects extends React.Component{
	constructor(){
		super();
		this.state = {
			status:"loading",
			projects:[]
		}
	}
	render() {
		const {status,projects} = this.state;
		let content = "error";
		if(status==="loading") content = <CircularProgress />
		return (
			<main>
				<h1>Your projects</h1>
				<Row>
					{content}
				</Row>
			</main>
		);
	}
}
class AllProjects extends React.Component{
	render() {
		return (
			<main>
				<h1>All projects</h1>
			</main>
		);
	}
}

class HomeC extends React.Component{
	render() {
		return (
			<main>
				<Container>
					{CredsStore.getLoggedIn() ? <MyProjects/> : ""}
					<AllProjects/>
				</Container>
			</main>
		);
	}
}

export const Home = withStyles(styles)(HomeC);
