import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import DeleteIcon from '@material-ui/icons/Delete';
import FilterListIcon from '@material-ui/icons/FilterList';
import { lighten } from '@material-ui/core/styles/colorManipulator';
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
