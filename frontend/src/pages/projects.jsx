import * as React from 'react';
import { createStyles, WithStyles } from '@material-ui/core/styles';
import withStyles from '@material-ui/core/styles/withStyles';

import PropTypes from 'prop-types';
import { Project as ProjectFetch } from "../utils/connect";

import Button from '@material-ui/core/Button';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { Typography } from '@material-ui/core';
import {Link} from 'react-router-dom'
import LabelImportant from '@material-ui/icons/LabelImportant';

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
  },
  input: {
    display: 'none',
  },

  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});


class ProjectsComponent extends React.Component {

  constructor(){
    super();
    this.state={
      projects:[]
    }
  }
  loadProjects = async () => {
    const projects = await ProjectFetch.getProjects();
    if(projects.successful) {
      this.setState({projects:projects.data})
      console.info("projects has been loaded",projects)
    }
    else console.error(`failed to load projects - statusText is not "OK"`,projects)
  }
  componentDidMount(){
    this.loadProjects();
  }
  render() {
    const { classes } = this.props;
    const projects = this.state.projects;
    

    return (
      <Paper className={classes.root}>
        <Table className={classes.table}>
          <TableHead>
            <TableRow>
              <TableCell align="center">Name</TableCell>
              <TableCell align="center">Description</TableCell>
              <TableCell align="center">Go to</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {projects.map(row => (
              <TableRow key={row.id}>
                <TableCell>
                  {row.name}
                </TableCell>
                <TableCell>{row.description}</TableCell>
                <TableCell>
                  <Button color='secondary' className={classes.button} to={`/project/${row.id}`} component={Link}>
                    <LabelImportant color='secondary' className={classes.icon}/>
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    )

  }
}

export const Projects = withStyles(styles,{ withTheme: true })(ProjectsComponent);



