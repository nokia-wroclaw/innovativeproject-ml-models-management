import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Checkbox, Input, InputLabel, SnackbarContent, Grid
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { TransformRounded as Logo, LockOutlined as LockOutlinedIcon, Error as Icon } from '@material-ui/icons';
import { Response, Project as ProjectFetch } from "../utils/connect"
import { RouteComponentProps } from 'react-router-dom';

const styles = (theme: Theme) =>
	createStyles({

	});

type State = {
	status:"loading"|"loaded"|"failed";
	id?:string;
	name?:string;
	repoUrl?:string;
	allParameters?:string[];
	allHiperParameters?:string[];
};

interface ProjectRouterProps {
	projectId: string;   // This one is coming from the router
}
interface Props extends WithStyles<typeof styles>, RouteComponentProps<ProjectRouterProps> {
	
}
class ProjectComponent extends React.Component<Props, State> {
	lastReq:string = "";
	constructor(props: Props) {
		super(props);
		this.state = {
			status:"loading"
		}
	}
	getProject = async ()=>{
		const urlId = this.props.match.params.projectId;
		this.setState({status:"loading"})
		const project = await ProjectFetch.getProject(urlId);

		if(!project.successful){
			this.setState({status:"failed"});
			return;
		}

		this.setState({
			id:project.id,
			name:project.name,
			repoUrl:project.repoUrl,
			allParameters:project.allParameters,
			allHiperParameters:project.allHiperParameters,
			status:"loaded"
		})
	}
	render() {
		const urlId = this.props.match.params.projectId;
		if(urlId !== this.lastReq && urlId !== this.state.id){
			this.lastReq = urlId;
			this.getProject();
		}

		if(this.state.status === "loaded") return(
			<p>loaded</p>
		)
		else if(this.state.status === "loading") return(
			<p>loading</p>
		)
		return(
			<p>failed</p>
		)
	}
}

export const Project = withStyles(styles)(ProjectComponent);
