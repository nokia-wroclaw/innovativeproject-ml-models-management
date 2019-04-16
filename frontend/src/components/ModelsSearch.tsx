import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Checkbox, Input, InputLabel, SnackbarContent, Grid, TableBody, Table, TableRow, TableCell
} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { RouteComponentProps } from 'react-router-dom';
import { GetModelsResponse, Parameter, Metric, Model as ModelConnect, Model } from "../utils/connect"
import { ModelsList } from "./ModelsList"

const styles = (theme: Theme) =>
	createStyles({
		flexRow:{
			display:"flex",
			flexDirection:"row"
		}
	});

interface State {
	status: "loading" | "loaded" | "failed";
	models?: Model[]
};

interface Props extends WithStyles<typeof styles> {
	projectId:number;
	allMetrics: string[],
	allParameters: string[],
	allHiperParameters: string[],
	allModelTags: string[];
	allModelNames: string[];
}
class ModelsSearchComp extends React.Component<Props, State> {
	lastReq: string = "";
	constructor(props: Props) {
		super(props);
		this.state = {
			status: "loading",
		}
	}
	getModels = async () => {
		
		this.setState({ status: "loading" })
		const response = await ModelConnect.getModels(this.props.projectId);

		if (!response.successful) {
			this.setState({ status: "failed" });
			return;
		}

		this.setState({
			models: response.models,
			status: "loaded"
		})
	}
	componentDidUpdate(prevProps: Props, prevState: State) {
		if (prevProps.projectId !== this.props.projectId) this.getModels();
	}
	componentDidMount() {
		this.getModels();
	}
	render() {
		console.log(this.state)
		if (this.state.status === "loaded") return (
			<div>
				<h3>Models</h3>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={4}>
						name
					</Grid>
					<Grid item xs={12} sm={4}>
						tags
					</Grid>
					<Grid item xs={12} sm={4}>
						branch
					</Grid>
				</Grid>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={4}>
						hiper parameters
					</Grid>
					<Grid item xs={12} sm={4}>
						parameters
					</Grid>
					<Grid item xs={12} sm={4}>
						metrics
					</Grid>
				</Grid>
				<div className={this.props.classes.flexRow}>
					<span>sort by</span>
					metric
					<span>named</span>
					fala
				</div>
				<ModelsList models={this.state.models}></ModelsList>
			</div>
		)
		else if (this.state.status === "loading") return (
			<p>loading</p>
		)
		return (
			<p>failed</p>
		)
	}
}

export const ModelsSearchComponent = withStyles(styles)(ModelsSearchComp);
