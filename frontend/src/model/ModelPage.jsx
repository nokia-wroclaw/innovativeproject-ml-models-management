import * as React from 'react';
import {
	Button, Typography, Chip, Grid, Paper, Container
} from '@material-ui/core';
import CircularProgress from '@material-ui/core/CircularProgress';
import withStyles from '@material-ui/core/styles/withStyles';
import { PropertiesList } from "../components/PropertiesList"
import { CenterBox } from "../components/layout"

import { Model } from "../utils/connect"

import {
	Label as LabelIcon,
	Person as PersonIcon,
	CalendarToday as CalendarTodayIcon,
	Reorder as ReorderIcon
} from '@material-ui/icons';
import { decodeModel } from './decodeModel';


const styles = theme => ({
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
	},
	progress: {
	  margin: theme.spacing(2),
	},
});



class ModelPage extends React.Component {
	loadModel = async () => {
		try {
			const res = await Model.getModel(this.props.match.params.modelId);
			console.log("res:",res);
			if(res.successful) {
				this.setState({model:decodeModel(res.data),status:"success"});
			}
			else{
				this.setState({status:res.message});
			}
		} catch(error) {
			console.error(error);
			this.setState({status:"random-fail"});
		}
	}
	componentDidMount(){
			this.loadModel();
	}
	constructor(props){
		super();
		this.state = {
			model:{},
			status:"loading"
		}
	}
	
	render() {
		const { classes } = this.props;
		const { model,status } = this.state;
		let response = this.state.status;
		if(status === "loading") response = ( <CenterBox>
			<CircularProgress className={classes.progress} />
		</CenterBox>)
		if(status === "success") response = (<Container>
			<Paper>
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
								key={"tag_" + tag.id}
								color="primary"
								variant="outlined"
							/>)
						}
					</Grid>
				</Grid>
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
			</Paper>
		</Container>)

		return response;
	}
}

export default withStyles(styles)(ModelPage)