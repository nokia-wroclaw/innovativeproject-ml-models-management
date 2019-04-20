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

const styles = (theme: Theme) =>
	createStyles({
		left: {
			textAlign: "left"
		},
		root: {
			flexGrow: 1,
			height: 250,
		},
		input: {
			display: 'flex',
			padding: 0,
		},
		valueContainer: {
			display: 'flex',
			flexWrap: 'wrap',
			flex: 1,
			alignItems: 'center',
			overflow: 'hidden',
		},
		chip: {
			margin: `${theme.spacing.unit / 2}px ${theme.spacing.unit / 4}px`,
		},
		chipFocused: {
			backgroundColor: emphasize(
				theme.palette.type === 'light' ? theme.palette.grey[300] : theme.palette.grey[700],
				0.08,
			),
		},
		noOptionsMessage: {
			padding: `${theme.spacing.unit}px ${theme.spacing.unit * 2}px`,
		},
		singleValue: {
			fontSize: 16,
		},
		placeholder: {
			position: 'absolute',
			left: 2,
			fontSize: 16,
		},
		paper: {
			position: 'absolute',
			zIndex: 1,
			marginTop: theme.spacing.unit,
			left: 0,
			right: 0,
		},
		divider: {
			height: theme.spacing.unit * 2,
		},
	});

const toOption = (str: string) => ({
	value: str,
	label: str,
	color: "FF0000"
})

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

interface State {
	selected: string[]
};

interface Props extends WithStyles<typeof styles> {
	options: string[];
	onChange: (selection: string[]) => void;
	selected: string[];
}

type Action = "select-option" | "deselect-option" | "remove-value" | "pop-value" | "set-value" | "clear" | "create-option";

function NoOptionsMessage(props) {
	return (
		<Typography
			color="textSecondary"
			className={props.selectProps.classes.noOptionsMessage}
			{...props.innerProps}
		>
			{props.children}
		</Typography>
	);
}

function inputComponent({ inputRef, ...props }) {
	return <div ref={inputRef} {...props} />;
}

function Control(props) {
	return (
		<TextField
			fullWidth
			InputProps={{
				inputComponent,
				inputProps: {
					className: props.selectProps.classes.input,
					inputRef: props.innerRef,
					children: props.children,
					...props.innerProps,
				},
			}}
			{...props.selectProps.textFieldProps}
		/>
	);
}

function Option(props) {
	return (
		<MenuItem
			buttonRef={props.innerRef}
			selected={props.isFocused}
			component="div"
			style={{
				fontWeight: props.isSelected ? 500 : 400,
			}}
			{...props.innerProps}
		>
			{props.children}
		</MenuItem>
	);
}

function Placeholder(props) {
	return (
		<Typography
			color="textSecondary"
			className={props.selectProps.classes.placeholder}
			{...props.innerProps}
		>
			{props.children}
		</Typography>
	);
}

function SingleValue(props) {
	return (
		<Typography className={props.selectProps.classes.singleValue} {...props.innerProps}>
			{props.children}
		</Typography>
	);
}

function ValueContainer(props) {
	console.log("ValueContainer")
	console.log(props)
	return <div className={props.selectProps.classes.valueContainer}>{props.children}</div>;
}

function MultiValue(props) {
	console.log("MultiValue")
	console.log(props)
	return (
		<Chip
			tabIndex={-1}
			label={props.children}
			className={classNames(props.selectProps.classes.chip, {
				[props.selectProps.classes.chipFocused]: props.isFocused,
			})}
			onDelete={props.removeProps.onClick}
			deleteIcon={<CancelIcon {...props.removeProps} />}
		/>
	);
}

function Menu(props) {
	return (
		<Paper square className={props.selectProps.classes.paper} {...props.innerProps}>
			{props.children}
		</Paper>
	);
}

const components = {
	// Control,
	// Menu,
	// MultiValue,
	// NoOptionsMessage,
	// Option,
	// Placeholder,
	// SingleValue,
	// ValueContainer,
};

class SuperSelectComp extends React.Component<Props, State> {
	constructor(props: Props) {
		super(props);
	}
	handle = (option: any, action: ActionMeta) => {
		if (!action) return;
		else if (action.action === "clear")
			this.props.onChange([]);
		else if (action.action === "deselect-option" || action.action === "pop-value" || action.action === "remove-value")
			this.props.onChange(this.props.selected.filter(opt => opt !== option.value));
		else if (action.action === "select-option" || action.action === "set-value")
			this.props.onChange([...this.props.selected, option.value])
	}
	render() {

		const { classes } = this.props;

		const selectStyles = {
			input: base => ({
				...base,
				'& input': {
					font: 'inherit',
				},
			}),
		};

		return  <div><Select
		  defaultValue={[colourOptions[2], colourOptions[3]]}
		  isMulti
		  name="colors"
		  options={colourOptions}
		  className="basic-multi-select"
		  classNamePrefix="select"
		/>

		<Select
			// classes={classes}
			value={this.props.selected.map( o => ({label:o,value:o}) )}
			isMulti
			name="colors"
			// options={colourOptions}
			className="basic-multi-select"
			classNamePrefix="select"
			styles={selectStyles}
			textFieldProps={{
				label: 'Label',
				InputLabelProps: {
					shrink: true,
				},
			}}
			options={this.props.options.map(toOption)}
			components={components}
			onChange={this.handle}
			placeholder="Select multiple countries"
		/></div>
	}
}

export const SuperSelect = withStyles(styles)(SuperSelectComp);
