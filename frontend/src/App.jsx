import * as React from 'react';
import {
   CssBaseline} from '@material-ui/core';
import { Theme } from '@material-ui/core/styles/createMuiTheme';
import createStyles from '@material-ui/core/styles/createStyles';
import { WithStyles } from '@material-ui/core/styles/withStyles';
import withRoot from './withRoot';
import { Login } from './pages/login';
import { Account } from './pages/account';
import { Home } from './pages/home';
import { Projects } from './pages/projects';
import { ProjectView } from './pages/project';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import NavBar from './components/NavBar'
import 'typeface-roboto';
import { Auth } from './utils/connect';

const styles = () =>
   createStyles({
      container:{
         maxWidth:"940px",
         marginLeft:"auto",
         marginRight:"auto"
      }
   });



class App extends React.Component {
   componentDidMount(){
      Auth.refresh();
   }
   render() {
      // @ts-ignore
      return (
         <div id="app">
               <Router>
                  <CssBaseline/>
                  <NavBar/>
                  <div id="main" className={this.props.classes.container}>
                     <Route path="/login" component={Login}/>
                     <Route path="/account" component={Account}/>
                     <Route path="/projects" component={Projects}/>
                     <Route
                        path="/project/:projectId"
                        component={ProjectView}
                     />
                     <Route exact path="/" component={Projects}/>
                  </div>
               </Router>
         </div>
      );
   }
}

export default withRoot(withStyles(styles)(App));
