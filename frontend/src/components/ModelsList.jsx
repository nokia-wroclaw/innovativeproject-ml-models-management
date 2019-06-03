import * as React from 'react';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import {ModelsListEl} from './ModelsListEl'

const styles = (theme) =>
	createStyles({
		left:{
			textAlign:"left"
		},
		valign:{
			display: "flex",
			justifyContent: "flex-start",
			alignItems: "center",
			margin:"0.2rem 0",
			"&>*:first-child":{
				marginRight:"0.25rem"
			}

		},
		spacing:{
			padding:theme.spacing.unit
		}
	});

function ModelsListComp(props) {
	const { classes } = props;
	const models = props.models || [];
	return (
		<div>
			{
				models.map(model =>{
					model.tags = model.tags || ["tagi","są","useful"];
					model.created = (new Date(model.created)).toLocaleDateString()
					const metrics = [];
					for (const key in model.metrics){
						metrics.push({
							id:key,
							value:model.metrics[key]
						})
					}
					model.metrics = metrics;
					const parameters = [];
					for (const key in model.parameters){
						parameters.push({
							id:key,
							value:model.parameters[key]
						})
					}
					model.parameters = parameters;
					const hyperparameters = [];
					for (const key in model.hyperparameters){
						hyperparameters.push({
							id:key,
							value:model.hyperparameters[key]
						})
					}
					model.hyperparameters = hyperparameters;
					console.log(`[ModelsList][render][map]`,{ model,metrics,parameters,hyperparameters })
					return <ModelsListEl key={model.id} model={model} />
				})
			}
		</div>
	)
}

export const ModelsList = withStyles(styles)(ModelsListComp);
