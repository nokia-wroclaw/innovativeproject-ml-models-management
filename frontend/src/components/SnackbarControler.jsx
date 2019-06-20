import * as React from 'react';
import {
   CssBaseline
} from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';
import {SuperSnackbar} from './SuperSnackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import { makeStyles } from '@material-ui/styles';

const styles = makeStyles(theme => ({
	
    }));

const ex_alert = {
	type:"default", // error, warning, information, success
	msg: "bla bla",
	actions: [
		{
			label:"dda",
			handler:(alert)=>true
		}
	]
}


class SnackbarControlerC extends React.Component {
	constructor(props){
		super();
		this.state={
			alerts:[]
		}
		props.ctrl.that = this;
	}
   handler = (action,alert)=>{
		if(action==="close") this.setState({alerts:this.state.alerts.filter( al => al!==alert)});
	}
   render() {
      return (
         <div>
				{this.state.alerts.map(alert => <SuperSnackbar alert={alert} handler={(action)=>this.handler(action,alert)} />)}
         </div>
      );
   }
}

export const SnackbarControler = withStyles(styles, { withTheme:true })(SnackbarControlerC);

export class SnackbarControlerIO {
	that={}
	add =(alert)=>{
		console.log(alert,this,this.that)
		this.that.setState({alerts:[...this.that.state.alerts,alert]})
	}
	drop=(alert)=>{
		this.that.setState({alerts:this.that.alerts.filter(al => al !== alert)})
	}
}
