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
import { ProjectView } from './pages/project';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import NavBar from './components/NavBar'


const styles = () =>
   createStyles({
   });



class App extends React.Component {

   render() {
      // @ts-ignore
      return (
         <div id="app">
            <Router>
               <CssBaseline/>
               <NavBar></NavBar>
               <div id="main">
                  <Route path="/login" component={Login}/>
                  <Route path="/account" component={Account}/>
                  <Route
                     path="/project/:projectId"
                     component={ProjectView}
                  />
                  <Route exact path="/" component={Home}/>
               </div>
            </Router>
         </div>
      );
   }
}

export default withRoot(withStyles(styles)(App));
