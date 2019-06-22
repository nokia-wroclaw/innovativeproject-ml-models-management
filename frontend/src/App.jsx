import * as React from 'react';
import {
   CssBaseline
} from '@material-ui/core';
import createStyles from '@material-ui/core/styles/createStyles';
import withRoot from './withRoot';
import { Login } from './user/LoginPage';
import { Register } from './user/RegisterPage';
import { Account } from './user/AccountPage';
import { Projects } from './project/ProjectsListPage';
import { ProjectView } from './project/ProjectPage';
import { Users } from './pages/users';
import { Home } from './pages/home';
import { UserView } from './pages/user';
import { ModelPage } from './model/ModelPage';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import NavBar from './components/NavBar'
import 'typeface-roboto';
import { Auth } from './utils/connect';
import { makeStyles } from '@material-ui/styles';
import {SnackbarControler,SnackbarControlerIO} from './components/SnackbarControler';

const styles = makeStyles(theme => ({
      container: {
         maxWidth: "940px",
         marginLeft: "auto",
         marginRight: "auto"
      },
    }));

    
    

class App extends React.Component {
   constructor(){
      super();
   }
   alerts = SnackbarControlerIO;
   componentDidMount() {
      Auth.refresh();
      window.alerts = this.alerts;
   }
   render() {
      // @ts-ignore
      return (
         <div id="app">
            <SnackbarControler ctrl={this.alerts}/>
            <Router>
               <CssBaseline />
               <NavBar />
               <div id="main" className={this.props.classes.container}>
                  <Route path="/login" component={Login} />
                  <Route path="/register" component={Register} />
                  <Route path="/account" component={Account} />
                  <Route exact path="/projects" component={Projects} />
                  <Route exact path="/users" component={Users} />
                  <Route
                     path="/projects/:projectId"
                     component={ProjectView}
                  />
                  <Route
                     path="/users/:userId"
                     component={UserView}
                  />
                  <Route
                     path="/models/:userId"
                     component={ModelPage}
                  />
                  <Route exact path="/" component={Projects} />
               </div>
            </Router>
         </div>
      );
   }
}

export default withRoot(withStyles(styles)(App));
