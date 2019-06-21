import * as React from 'react';
import { withStyles } from '@material-ui/core/styles';
import {SuperSnackbar} from './SuperSnackbar';
import { makeStyles } from '@material-ui/styles';

const styles = makeStyles(theme => ({
	
    }));

// const ex_alert = {
// 	type:"default", // error, warning, information, success
// 	msg: "bla bla",
// 	actions: [
// 		{
// 			label:"dda",
// 			handler:(alert)=>true
// 		}
// 	]
// }


class SnackbarControlerC extends React.Component {
	constructor(props){
		super();
		this.state={
			alerts:[]
		}
		props.ctrl.attach(this);
	}
   handler = (action,alert)=>{
		if(action==="close") this.setState({alerts:this.state.alerts.filter( al => al!==alert)});
	}
	drop = alert => {
		this.setState({alerts:this.state.alerts.filter(al => al !== alert)})
	}
	add = (alert)=>{
		this.setState({alerts:[...this.state.alerts,alert]})
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

let that={}

export const SnackbarControlerIO = {
	add:(msg,type,actions)=>{
		const alert = {msg,type,actions};
		that.add(alert);
		return alert;
	},
	drop:(alert)=>{
		that.drop(alert);
	},
	attach:(snackbarControlerComponentContext)=>{
		that=snackbarControlerComponentContext
	}
}
