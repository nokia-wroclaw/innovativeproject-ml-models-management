import * as React from 'react';
import {
	Grid, TextField
} from '@material-ui/core';
import { createStyles} from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { Model as ModelConnect} from "../utils/connect"
import { ModelsList } from "./ModelsList"
import { SuperSelect } from './SuperSelect';

const styles = (theme) =>
	createStyles({
		flexRow:{
			display:"flex",
			flexDirection:"row"
		}
	});


class ModelsSearchComp extends React.Component{
	lastReq = "";
	constructor(props) {
		super(props);
		this.state = {
			status: "loading",
			modelName: "",
			tags: [],
			parameters: [],
			hiperParameters: [],
			metrics: [],
			branches: []
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
	componentDidUpdate(prevProps, prevState) {
		if (prevProps.projectId !== this.props.projectId) this.getModels();
	}
	componentDidMount() {
		this.getModels();
	}
	render() {
		const state = this.state;
		if (this.state.status === "loaded") return (
			<div>
				<h3>Models</h3>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={4}>
						<TextField
							id="standard-with-placeholder"
							label="model name"
							placeholder="eg. Model Marka"
							margin="normal"
							value={this.state.modelName}
							onChange={ e=>{this.setState({modelName:e.target.value})} }
						/>
					</Grid>
					<Grid item xs={12} sm={4}>
						<SuperSelect name="branches" selected={["not implemented"]} options={["not implemented"]} onChange={updated=>null}/>
					</Grid>
					<Grid item xs={12} sm={4}>

						{/*<SuperSelect name="branches" selected={this.state.branches} options={this.props.allBranches} onChange={updated=>this.setState({branches:updated})}/>*/}
					</Grid>
				</Grid>
				<Grid container spacing={24}>
					<Grid item xs={12} sm={4}>

						<SuperSelect selected={this.state.hiperParameters} options={this.props.allHiperParameters} onChange={updated=>this.setState({hiperParameters:updated})}/>
					</Grid>
					<Grid item xs={12} sm={4}>

						<SuperSelect selected={this.state.parameters} options={this.props.allParameters} onChange={updated=>this.setState({parameters:updated})}/>
					</Grid>
					<Grid item xs={12} sm={4}>

						<SuperSelect selected={this.state.metrics} options={this.props.allMetrics} onChange={updated=>this.setState({metrics:updated})}/>
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
