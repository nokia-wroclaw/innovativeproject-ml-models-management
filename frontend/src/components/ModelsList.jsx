import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Chip, Checkbox, Input, InputLabel, SnackbarContent, Grid, TableBody, Table, TableRow, TableCell, ExpansionPanelSummary, ExpansionPanel, Divider, ExpansionPanelActions, ExpansionPanelDetails
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import classNames from 'classnames';
import { RouteComponentProps } from 'react-router-dom';
import { GetModelsResponse, Parameter, Metric, Model as ModelConnect, Model } from "../utils/connect"

const styles = (theme) =>
	createStyles({
		left:{
			textAlign:"left"
		}
	});

function ModelsListComp(props) {
	const { classes } = props;
	const models = props.models || [];
	console.log(`[ModelsList][render]`,models)
	return (
		<div>
			{
				models.map(model =>{
					model.tags = model.tags || ["tagi","są","usefull"];
					const metrics = [];
					for (const key in model.metrics){
						metrics.push({
							id:key,
							value:model.metrics[key]
						})
					}
					const parameters = [];
					for (const key in model.parameters){
						parameters.push({
							id:key,
							value:model.parameters[key]
						})
					}
					const hyperparameters = [];
					for (const key in model.hyperparameters){
						hyperparameters.push({
							id:key,
							value:model.hyperparameters[key]
						})
					}
					console.log(`[ModelsList][render][map]`,{ model,metrics,parameters,hyperparameters })
					return (<ExpansionPanel>
						<ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
							<Grid container direction="row">
								<Grid item xs={5}>
									<Grid container direction="column" spacing={0}>
										<Grid item xs={12}><Typography className={classes.left}>name: {model.name}</Typography></Grid>
										<Grid item xs={12}><Typography className={classes.left}>description: {model.description}</Typography></Grid>
										<Grid item xs={12}><Typography className={classes.left}>author: {model.user.full_name}</Typography></Grid>
										<Grid item xs={12}><Typography className={classes.left}>added: {model.created}</Typography></Grid>
										<Grid item xs={12}><Typography className={classes.left}>commit: <a href={model.commitUrl}></a></Typography></Grid>
									</Grid>
								</Grid>
								<Grid item xs={5}>
									<Grid container direction="column" spacing={0}>
										<Grid item xs={12}>
											<Typography className={classes.left}>
												tags: <br/> {model.tags.map( tag => <Chip
														label={tag}
														color="primary"
														variant="outlined"
													/> )}
											</Typography>
										</Grid>
										<Grid item xs={12}><Typography className={classes.left}>metrics: <br/> {metrics.map( m => m.id + "=" + m.value ).join(", ")}</Typography></Grid>
									</Grid>
								</Grid>
								<Grid item xs={2} onClick={e => e.stopPropagation()} >
									<Grid container direction="column" spacing={0}>
										<Grid item xs={12}>
											<Button variant="outlined" fullWidth size="small" color="primary" className={classes.button} href={model.commitUrl}>
												go to commit
											</Button>
											<Button variant="outlined" fullWidth size="small" color="primary" className={classes.button}>
												ojej
											</Button>
										</Grid>
									</Grid>
								</Grid>
							</Grid>
						</ExpansionPanelSummary>
						<ExpansionPanelDetails>
							<Grid container direction="row">
								<Grid item xs={6}>
									<Typography className={classes.left}>parameters: <br/> {parameters.map( m => m.id + "=" + m.value ).join(", ")}</Typography>
								</Grid>
								<Grid item xs={6}>
									<Typography className={classes.left}>hyperparameters: <br/> {hyperparameters.map( m => m.id + "=" + m.value ).join(", ")}</Typography>
								</Grid>
							</Grid>
						</ExpansionPanelDetails>
					</ExpansionPanel>)}
				)
			}
		</div>
	)
}

export const ModelsList = withStyles(styles)(ModelsListComp);
