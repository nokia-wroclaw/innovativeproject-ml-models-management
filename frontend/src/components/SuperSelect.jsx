import * as React from 'react';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';
import Select from 'react-select'
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import { ActionMeta } from 'react-select/lib/types';
import { emphasize } from '@material-ui/core/styles/colorManipulator';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import Typography from '@material-ui/core/Typography';
import NoSsr from '@material-ui/core/NoSsr';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Chip from '@material-ui/core/Chip';
import MenuItem from '@material-ui/core/MenuItem';
import CancelIcon from '@material-ui/icons/Cancel';

const colourOptions = [
	{ value: 'ocean', label: 'Ocean', color: '#00B8D9', isFixed: true },
	{ value: 'blue', label: 'Blue', color: '#0052CC', isDisabled: true },
	{ value: 'purple', label: 'Purple', color: '#5243AA' },
	{ value: 'red', label: 'Red', color: '#FF5630', isFixed: true },
	{ value: 'orange', label: 'Orange', color: '#FF8B00' },
	{ value: 'yellow', label: 'Yellow', color: '#FFC400' },
	{ value: 'green', label: 'Green', color: '#36B37E' },
	{ value: 'forest', label: 'Forest', color: '#00875A' },
	{ value: 'slate', label: 'Slate', color: '#253858' },
	{ value: 'silver', label: 'Silver', color: '#666666' },
 ];

const styles = theme => {};
const toOption = name => ({
	value: name,
	label: name
});

class SuperSelectComp extends React.Component {
	constructor(props) {
		super(props);
	}
	handle = (option, action) => {
		console.log("option",option);
		console.log("action",action);
		let updated = this.props.selected;
      if (action.action === "clear") updated = [];
		else if (action.action === "deselect-option" || action.action === "pop-value" || action.action === "remove-value")
			updated = this.props.selected.filter(opt => opt !== action.removedValue.value);
		else if (action.action === "select-option" || action.action === "set-value")
			updated = [...this.props.selected, action.option.value];
		console.log("updated",updated);
		this.props.onChange(updated);
	};
	render() {
		console.log(this.props)
		return (<Select
			value={this.props.selected.map( o => ({label:o,value:o}) )}
			isMulti
			name="colors"
			className="basic-multi-select"
			classNamePrefix="select"
			options={this.props.options.map(toOption)}
			onChange={this.handle}
		/>)
	}
}

export const SuperSelect = withStyles(styles)(SuperSelectComp);
