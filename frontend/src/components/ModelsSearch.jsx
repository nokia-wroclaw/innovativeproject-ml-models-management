import * as React from 'react';
import {
	Divider,
	Grid, TextField
} from '@material-ui/core';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { Model as ModelConnect } from "../utils/connect"
import { ModelsList } from "./ModelsList"
import { SuperSelect } from './SuperSelect';
import Typography from "@material-ui/core/Typography";

const styles = (theme) =>
	createStyles({
		flexRow: {
			display: "flex",
			flexDirection: "row"
		},
		spacer: {
			width: "100%",
			height: "40px"
		}
	});


class ModelsSearchComp extends React.Component {
	lastReq = "";
	constructor(props) {
		super(props);
		this.state = {
			status: "loading",
			modelName: "",
			tags: [],
			parameters: [],
			hyperParameters: [],
			metrics: [],
			branches: []
		}
	}
	getModels = async () => {
		this.setState({ status: "loading" })
		const response = await ModelConnect.getModels({
			project: this.props.projectId,
			parameters: this.state.parameters,
			hyperparameters: this.state.hyperParameters,
			metrics: this.state.metrics,
		});
		console.log(`[ModelsSearch][getModels]`, response)
		if (response.successful) {
			response.data = response.data.map( model => {
				model.commitUrl = this.props.projectGit + "/commit/" + model.git.commit_hash
				return model;
			} )
			this.setState({
				models: response.data,
				status: response.text
			});
		}
		else {
			this.setState({
				status: response.text
			})
		}
	}
	componentDidUpdate(prevProps, prevState) {
		if (prevProps.projectId !== this.props.projectId) this.getModels();
	}
	componentDidMount() {
		this.getModels();
	}
	render() {
		const { classes } = this.props;
		if (this.state.status === "OK") return (
			<div>
				<Typography variant="h4">Models</Typography>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={8}>
						<SuperSelect name="name" label="Model name" placeholder="eg. Model Marka" disabled selected={[]} options={["not implemented"]} onChange={updated => null} />
					</Grid>
					<Grid item xs={12} sm={4}>
						<SuperSelect name="branches" label="Branches" placeholder="eg. master" disabled selected={[]} options={["not implemented"]} onChange={updated => null} />
					</Grid>
				</Grid>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={4}>

						<SuperSelect selected={this.state.hyperParameters} label="hyper Parameters" placeholder="hyper Parameters" options={this.props.allHyperParameters} onChange={updated => { this.setState({ hyperParameters: updated }); setTimeout(this.getModels, 100) }} />
					</Grid>
					<Grid item xs={12} sm={4}>

						<SuperSelect selected={this.state.parameters} label="Parameters" placeholder="Parameters" options={this.props.allParameters} onChange={updated => this.setState({ parameters: updated })} />
					</Grid>
					<Grid item xs={12} sm={4}>
						<SuperSelect selected={this.state.metrics} label="Metrics" placeholder="Metrics" options={this.props.allMetrics} onChange={updated => this.setState({ metrics: updated })} />
					</Grid>
				</Grid>
				<div className={classes.spacer} />
				<ModelsList models={this.state.models} />
			</div>
		)
		else if (this.state.status === "loading") return (
			<p>loading..</p>
		)
		return (
			<p>{this.state.status}</p>
		)
	}
}

export const ModelsSearchComponent = withStyles(styles)(ModelsSearchComp);
