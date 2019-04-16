import * as React from 'react';
import {
	Button, Typography, FormControl, FormControlLabel, Paper, Checkbox, Input, InputLabel, SnackbarContent, Grid, TableBody, Table, TableRow, TableCell, ExpansionPanelSummary, ExpansionPanel, Divider, ExpansionPanelActions, ExpansionPanelDetails, Chip
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import classNames from 'classnames';
import { RouteComponentProps } from 'react-router-dom';
import { GetModelsResponse, Parameter, Metric, Model as ModelConnect, Model } from "../utils/connect"

const styles = (theme: Theme) =>
	createStyles({
		left:{
			textAlign:"left"
		}
	});

interface State {
};

interface Props extends WithStyles<typeof styles> {
	models?: Model[],
}
class ModelsListComp extends React.Component<Props, State> {
	lastReq: string = "";
	constructor(props: Props) {
		super(props);
		this.state = {
		}
	}
	render() {
		const { classes } = this.props;
		const models = this.props.models || [];
		return (
			<div>
				{
					models.map(model =>
						<ExpansionPanel defaultExpanded>
							<ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
								<Grid container direction="row">
									<Grid item xs={6}>
										<Grid container direction="column" spacing={0}>
											<Grid item xs={12}><Typography className={classes.left}>name: {model.name}</Typography></Grid>
											<Grid item xs={12}><Typography className={classes.left}>description: {model.description}</Typography></Grid>
											<Grid item xs={12}><Typography className={classes.left}>author: not implemented</Typography></Grid>
											<Grid item xs={12}><Typography className={classes.left}>added: not implemented</Typography></Grid>
										</Grid>
									</Grid>
									<Grid item xs={6}>
										<Grid container direction="column" spacing={0}>
											<Grid item xs={12}><Typography className={classes.left}>tags: {model.tags.join(", ")}</Typography></Grid>
											<Grid item xs={12}><Typography className={classes.left}>metrics: {model.metrics.map( m => m.id + "=" + m.value ).join(", ")}</Typography></Grid>
										</Grid>
									</Grid>
								</Grid>
							</ExpansionPanelSummary>
							<ExpansionPanelDetails>
								<Grid container direction="row">
									<Grid item xs={6}>
										<Typography className={classes.left}>parameters: {model.parameters.map( m => m.id + "=" + m.value ).join(", ")}</Typography>
									</Grid>
									<Grid item xs={6}>
										<Typography className={classes.left}>hiperparameters: {model.hiperParameters.map( m => m.id + "=" + m.value ).join(", ")}</Typography>
									</Grid>
								</Grid>
							</ExpansionPanelDetails>
						</ExpansionPanel>
					)
				}
			</div>
		)
	}
}

export const ModelsList = withStyles(styles)(ModelsListComp);
