import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom'
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import * as MUI from '@material-ui/core/';
import {Button} from '@material-ui/core/';
import { WithStyles } from '@material-ui/core/styles/withStyles';
import { withStyles } from '@material-ui/core/styles';
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
  render() {
    const { classes } = this.props;
    console.log(MUI);

    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            <Typography className={classes.title} variant="h6" color="inherit" noWrap>
              Maisie
            </Typography>
            <Button color="inherit"  component={Link} to="/project/1" >Example project</Button>
            <div className={classes.grow} />
            <div className={classes.section}>
              <Typography className={classes.link} variant="h6" color="inherit" noWrap>
                Ask Marek
              </Typography>
            </div>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(styles)(PrimarySearchAppBar);