import * as React from 'react';
import { Button, Typography } from '@material-ui/core'; 
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { Project as ProjectFetch } from "../utils/connect" 
import { ModelsSearchComponent } from './ModelsSearch'


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
			marginBottom: theme.spacing(1)
		},
		button: {
			margin: theme.spacing(1),
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
			id: this.props.match.params.projectId,
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
		const response = await ProjectFetch.getProject(Number(urlId));

		if (!response.successful) {
			this.setState({ status: response.text });
			return;
		}

		const project = response.data;
		console.log(`[Project][getProjects]`,response)
		this.setState({
			id: project.id,
			name: project.name,
			description: project.description,
			repoUrl: project.git_url,
			allParameters: project.all_parameters,
			allHyperParameters: project.all_hyperparameters,
			allModelTags: project.all_modeltags || [],
			allModelNames: project.all_modelnames || [],
			allMetrics: project.all_metrics,
			status: "OK"
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
		if (this.state.status === "OK") {
			const project = this.state;
			return (
				<div>
					<div className={classes.cover}>
						<Typography className={classes.coverItem} variant={"h3"}>{state.name}</Typography>
						<Typography className={classes.coverItem} variant={"h5"}>{state.description}</Typography>
						<div className={classes.row}>
							<Button variant="outlined" size="small" color="primary" className={classes.button} href={state.repoUrl}>
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
						projectGit={project.repoUrl}
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
			<p>{this.state.status}</p>
		)
	}
}

export const ProjectView = withStyles(styles)(ProjectComponent);