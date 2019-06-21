import * as React from 'react';
import { TextField} from '@material-ui/core';
import withStyles from '@material-ui/core/styles/withStyles';
import createStyles from '@material-ui/core/styles/createStyles';
import { Model as ModelConnect } from "../utils/connect"
import { ModelsList } from "./ModelsList"
import Typography from "@material-ui/core/Typography";


const styles = theme => (
	createStyles({
		flexRow: {
			display: "flex",
			flexDirection: "row"
		},
		spacer: {
			width: "100%",
			height: "40px"
		},
		container: {
			display: 'flex',
			flexWrap: 'wrap',
		},
		textField: {
			marginLeft: theme.spacing(1),
			marginRight: theme.spacing(1),
		},
		dense: {
			marginTop: theme.spacing(2),
		},
		fullwidth: {
			width:"100%",
		},
		menu: {
			width: 200,
		}
	})
);

const inputStyles = createStyles({
	root:{
		margin:0
	}
});

class ModelsSearchComp extends React.Component {
	lastReq = "";
	constructor(props) {
		super(props);
		this.state = {
			status: "loading",
			querry: ""
		}
	}
	getModels = async () => {
		this.setState({ status: "loading" })
		const response = await ModelConnect.getModels(this.props.projectId,this.state.querry);
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
			<div className={classes.container}>
				<Typography variant="h4">Models</Typography>
				<div className={classes.spacer} />
				<TextField
					id="outlined-full-width"
					label="Search"
					style={{ margin: 8 }}
					placeholder="name=lorem11|sort=metric.acc,asc,filter"
					helperText=""
					fullWidth
					margin="normal"
					variant="outlined"
					InputLabelProps={{
						shrink: true,
					}}
					value={this.state.querry}
					onChange={(newQuerry)=>this.setState({querry:newQuerry})}
					classes={inputStyles.root}
				/>
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
