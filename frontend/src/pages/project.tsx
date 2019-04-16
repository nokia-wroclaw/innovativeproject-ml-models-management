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

const styles = (theme: Theme) =>
	createStyles({

	});

interface State extends ProjectDetails {
	status: "loading" | "loaded" | "failed";
};

interface ProjectRouterProps {
	projectId: string;   // This one is coming from the router
}
interface Props extends WithStyles<typeof styles>, RouteComponentProps<ProjectRouterProps> {

}
class ProjectComponent extends React.Component<Props, State> {
	lastReq: string = "";
	constructor(props: Props) {
		super(props);
		this.state = {
			status: "loading",
			id: 0,
			name: "please wait",
			description: "please wait",
			repoUrl: "please wait",
			allParameters: ["please wait"],
			allHiperParameters: ["please wait"],
			allModelTags: ["please wait"],
			allModelNames: ["please wait"],
			allMetrics: ["please wait"]
		}
	}
	getProject = async () => {
		const urlId = this.props.match.params.projectId;
		this.setState({ status: "loading" })
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
			allHiperParameters: project.allHiperParameters,
			allModelTags: project.allModelTags,
			allModelNames: project.allModelNames,
			allMetrics: project.allMetrics,
			status: "loaded"
		})
	}
	componentDidUpdate(prevProps: Props, prevState: State) {
		const urlId = this.props.match.params.projectId;
		const prevUrlId = prevProps.match.params.projectId;
		if (urlId !== prevUrlId) this.getProject();
	}
	componentDidMount() {
		this.getProject();
	}
	render() {
		if (this.state.status === "loaded") {
			const project = this.state;
			return (
				<div>
					<h1>This some project called {this.state.name}</h1>
					<p>{this.state.description}</p>
					<a href={this.state.repoUrl}>Go to code repo for some additional inside.</a>
					<ModelsSearchComponent 
						projectId={project.id}
						allHiperParameters={project.allHiperParameters}
						allMetrics={project.allMetrics}
						allModelNames={project.allModelNames}
						allModelTags={project.allModelTags}
						allParameters={project.allParameters}
					/>
				</div> 
			) 
		}
		else if (this.state.status === "loading") return (
			<p>loading</p>
		)
		return (
			<p>failed</p>
		)
	}
}

export const ProjectView = withStyles(styles)(ProjectComponent);