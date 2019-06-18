import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Checkbox, Input, InputLabel, SnackbarContent, Grid, TableBody, Table, TableRow, TableCell
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { TransformRounded as Logo, LockOutlined as LockOutlinedIcon, Error as Icon } from '@material-ui/icons';
import { Response, Project as ProjectFetch } from "../utils/connect"
import { RouteComponentProps } from 'react-router-dom';
import { Project, GetProjectResponse, ProjectDetails } from "../utils/connect"
import { ModelsSearchComponent } from '../components/ModelsSearch'

const styles = (theme) =>
	createStyles({
		cover: {
			width: "100%",
			padding: "40px 0",
			display: "flex",
			flexDirection: "column",
			justifyContent: "space-between"
		},
		coverItem: {
			marginBottom: theme.spacing.unit
		},
		button: {
			margin: theme.spacing.unit,
		},
		row: {
			display: "flex",
			flexDirection: "row",
			marginTop: "10px",
			"& *:first-child":{
				marginLeft:0
			}
		}
	});

class ProjectComponent extends React.Component {
	lastReq = "";
	constructor(props) {
		super(props);
		this.state = {
			status: "loading",
			id: 0,
			name: "please wait",
			description: "please wait",
			repoUrl: "please wait",
			allParameters: ["please wait"],
			allHyperParameters: ["please wait"],
			allModelTags: ["please wait"],
			allModelNames: ["please wait"],
			allMetrics: ["please wait"]
		}
	}
	getProject = async () => {
		const urlId = this.props.match.params.projectId;
		this.setState({ status: "loading" })
		console.info("szybkie pytanie co do kurwy",urlId,Number(urlId))
		const project = await ProjectFetch.getProject(Number(urlId));

		if (!project.successful) {
			this.setState({ status: "failed" });
			return;
		}

		this.setState({
			id: project.id,
			name: project.name,
			description: project.description,
			repoUrl: project.repoUrl,
			allParameters: project.allParameters,
			allHyperParameters: project.allHyperParameters,
			allModelTags: project.allModelTags,
			allModelNames: project.allModelNames,
			allMetrics: project.allMetrics,
			status: "loaded"
		})
	}
	componentDidUpdate(prevProps, prevState) {
		const urlId = this.props.match.params.projectId;
		const prevUrlId = prevProps.match.params.projectId;
		if (urlId !== prevUrlId) this.getProject();
	}
	componentDidMount() {
		this.getProject();
	}
	render() {
		const {classes} = this.props;
		const {state} = this;
		if (this.state.status === "loaded") {
			const project = this.state;
			return (
				<div>
					<div className={classes.cover}>
						<Typography className={classes.coverItem} variant={"h3"}>{state.name}</Typography>
						<Typography className={classes.coverItem} variant={"h5"}>{state.description}</Typography>
						<div className={classes.row}>
							<Button variant="outlined" size="small" color="primary" className={classes.button}>
								Code Repo
							</Button>
							<Button variant="outlined" size="small" color="primary" className={classes.button}>
								Issue Tracker
							</Button>
							<Button variant="outlined" size="small" color="primary" className={classes.button}>
								Live Demo
							</Button>
						</div>
					</div>
					<ModelsSearchComponent 
						projectId={project.id}
						allHyperParameters={project.allHyperParameters}
						allMetrics={project.allMetrics}
						allNames={project.allModelNames}
						allTags={project.allModelTags}
						allParameters={project.allParameters}
						allBranches={project.allBranches}
					/>
				</div> 
			) 
		}
		else if (this.state.status === "loading") return (
			<p>loading</p>
		);
		return (
			<p>failed</p>
		)
	}
}

export const ProjectView = withStyles(styles)(ProjectComponent);