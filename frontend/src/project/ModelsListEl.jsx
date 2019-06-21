import * as React from 'react';
import {
	Button, Typography, Chip, Grid, ExpansionPanelSummary, ExpansionPanel, ExpansionPanelDetails
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';

import {PropertiesList} from "../components/PropertiesList"

import {
	Label as LabelIcon,
	Person as PersonIcon,
	CalendarToday as CalendarTodayIcon,
	Reorder as ReorderIcon
} from '@material-ui/icons';

const styles = (theme) =>
	createStyles({
		left: {
			textAlign: "left"
		},
		valign: {
			display: "flex",
			justifyContent: "flex-start",
			alignItems: "center",
			margin: "0.2rem 0",
			"&>*:first-child": {
				marginRight: "0.25rem"
			}

		},
		spacing: {
			padding: theme.spacing(1)
		}
	});


function ModelsListComp(props) {
	const { classes } = props;
	const model = props.model;
	return (<ExpansionPanel TransitionProps={{ unmountOnExit: true }} >
		<ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
			<Grid container direction="row">
				<Grid item xs={5}>
					<Grid container direction="column" spacing={0}>
						<Grid item xs={12}><div className={classes.valign}><LabelIcon color="primary" /><Typography> {model.name}</Typography></div></Grid>
						<Grid item xs={12}><div className={classes.valign}><PersonIcon color="primary" /><Typography> {model.user.full_name}</Typography></div></Grid>
					</Grid>
				</Grid>
				<Grid item xs={5}>
					<Grid container direction="column" spacing={0}>
						<Grid item xs={12}><div className={classes.valign}><CalendarTodayIcon color="primary" /><Typography> {model.created}</Typography></div></Grid>
						<Grid item xs={12}><div className={classes.valign}><ReorderIcon color="primary" /><Typography> {model.dataset.name}</Typography></div></Grid>
					</Grid>
				</Grid>
				<Grid item xs={2} onClick={e => e.stopPropagation()} >
					<Grid container direction="column" spacing={0}>
						<Grid item xs={12}>
							<div className={classes.valign}>
								<Button variant="outlined" fullWidth size="small" color="primary" className={classes.button} href={model.commitUrl}>
									go to commit
								</Button>
							</div>
						</Grid>
						<Grid item xs={12}>
							<div className={classes.valign}>
								<Button variant="outlined" fullWidth size="small" color="primary" className={classes.button}>
									edit
								</Button>
							</div>
						</Grid>
					</Grid>
				</Grid>
				<Grid item xs={12}>
					{
						model.tags.map(tag => <Chip
							label={tag.name}
							key={"tag_"+tag.id}
							color="primary"
							variant="outlined"
						/>)
					}
				</Grid>
			</Grid>
		</ExpansionPanelSummary>
		<ExpansionPanelDetails>
			<Grid container direction="row">
				<Grid item xs={4}>
					<PropertiesList data={model.metrics} title="Metrics" />
				</Grid>
				<Grid item xs={4}>
					<PropertiesList data={model.hyperparameters} title="Hyperparameters" />
				</Grid>
				<Grid item xs={4}>
					<PropertiesList data={model.parameters} title="parameters" />
				</Grid>
			</Grid>
		</ExpansionPanelDetails>
	</ExpansionPanel>)
}

export const ModelsListEl = withStyles(styles)(ModelsListComp);
