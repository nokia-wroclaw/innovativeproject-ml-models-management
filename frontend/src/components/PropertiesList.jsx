import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import withStyles from '@material-ui/core/styles/withStyles';

const styles = theme => ({
	root: {
	  width: '100%',
	  marginTop: theme.spacing(3),
	  overflowX: 'auto',
	},
	table: {
	  width: "100%",
	},
 });

function PropertiesListComp(props) {
	const { classes, data, title } = props;

	return (
			<Table className={classes.table} size="small">
				<TableHead>
					<TableRow>
						<TableCell>{title}</TableCell>
						<TableCell align="right">value</TableCell>
					</TableRow>
				</TableHead>
				<TableBody>
					{data.map(row => (
						<TableRow key={row.id}>
							<TableCell component="th" scope="row">
								{row.id}
							</TableCell>
							<TableCell align="right">{row.value}</TableCell>
							<TableCell align="right">{row.fat}</TableCell>
						</TableRow>
					))}
				</TableBody>
			</Table>
	);
}


export const PropertiesList = withStyles(styles)(PropertiesListComp);
