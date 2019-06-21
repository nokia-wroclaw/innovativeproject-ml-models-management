import * as React from 'react';
import { createStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import { ModelsListEl } from './ModelsListEl'
import {decodeModel} from '../model/decodeModel'

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
		},
		fullwidth: {
			width:"100%"
		}
	});

function ModelsListComp(props) {
	const models = props.models || [];
	return (
		<div classes={styles.fullwidth}>
			{
				models.map(model => {
					model = decodeModel(model)
					return <ModelsListEl key={"model_"+model.id} model={model} />
				})
			}
		</div>
	)
}

export const ModelsList = withStyles(styles)(ModelsListComp);
