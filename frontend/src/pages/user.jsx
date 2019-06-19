import * as React from 'react';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';

import { User as UserFetch } from "../utils/connect"
import { ModelsList } from '../project/ModelsList'



const styles = (theme) =>
	createStyles({
		cover: {
			width: "100%",
			padding: "40px 0",
			display: "flex",
			flexDirection: "column",
			justifyContent: "space-between"
		},
		coverItem: {
			marginBottom: theme.spacing(1)
		},
		button: {
			margin: theme.spacing(1),
		},
		row: {
			display: "flex",
			flexDirection: "row",
			marginTop: "10px",
			"& *:first-child": {
				marginLeft: 0
			}
		}
	});


class UserComponent extends React.Component {
	lastReq = "";
	constructor(props) {
		super(props);
		this.state = {
			status: "loading",
			id: this.props.match.params.userId,
			name: "please wait",
			description: "please wait",
			allParameters: ["please wait"],
			allHyperParameters: ["please wait"],
			allModelTags: ["please wait"],
			allModelNames: ["please wait"],
			allMetrics: ["please wait"]
		}
	}
	getUser = async () => {
		const urlId = this.props.match.params.userId;
		this.setState({ status: "loading" })
		const response = await UserFetch.getUser(Number(urlId));

		if (!response.successful) {
			this.setState({ status: response.text });
			return;
		}

		const user = response.data;
		console.log(`[User][getUsers]`, response)
		this.setState({
			id: user.id,
			name: user.full_name,
			description: user.description,
			repoUrl: user.git_url,
			allParameters: user.all_parameters,
			allHyperParameters: user.all_hyperparameters,
			allModelTags: user.all_modeltags || [],
			allModelNames: user.all_modelnames || [],
			allMetrics: user.all_metrics,
			status: "OK"
		})
	}

	render() {
		return (
			<div>
				<ModelsList />
			</div>
		)
	}

}

export const UserView = withStyles(styles)(UserComponent);