import React from 'react';
import { Link } from 'react-router-dom'
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import {Button} from '@material-ui/core/';
import { withStyles } from '@material-ui/core/styles';
import Assignment from '@material-ui/icons/Assignment';
import People from '@material-ui/icons/People';
import { CredsStore } from '../user/CredsStore';

const styles = theme => ({
  root: {
    width: '100%',
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20,
  },
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
    },
  },
  link: {
    display: 'block',
  },
  section: {
    display: 'flex',
  },
});

class PrimarySearchAppBar extends React.Component {
  constructor(){
    super();
    this.state = {
      loggedIn:!!(CredsStore.getCreds() && CredsStore.getCreds().access_token)
    }
    CredsStore.subscribeToken("navbar",this.update); 
  }
  update = (creds)=>{
    console.log(creds)
    this.setState({
      loggedIn:!!(creds && creds.access_token)
    })
  }
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            <Typography className={classes.title} variant="h6" color="inherit" noWrap>
              <Button color="inherit" component={Link} to="/" >Maisie</Button>
            </Typography>
            <Button color="inherit"  component={Link} to="/projects/">
            Projects
            <Assignment color='inherit' className={classes.icon}/>
            </Button>
            <Button color="inherit"  component={Link} to="/users/" >
            Users
            <People color='inherit' className={classes.icon}/>
            </Button>
            <div className={classes.grow} />
            <div className={classes.section}>
              {this.state.loggedIn ? 
            <Button color="inherit" onClick={()=>CredsStore.setCreds(null)}>
              <Typography className={classes.link} variant="h6" color="inherit" noWrap>
                Log out
              </Typography>
            </Button> : 
            <Button color="inherit"  component={Link} to="/login" >
              <Typography className={classes.link} variant="h6" color="inherit" noWrap>
                Log in
              </Typography>
            </Button>}
            </div>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme:true })(PrimarySearchAppBar);