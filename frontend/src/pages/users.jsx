import * as React from 'react';
import withStyles from '@material-ui/core/styles/withStyles';

import { User as UserFetch } from "../utils/connect";

import Button from '@material-ui/core/Button';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {Link} from 'react-router-dom'
import LabelImportant from '@material-ui/icons/LabelImportant';

const styles = theme => ({
  button: {
    margin: theme.spacing(1),
  },
  input: {
    display: 'none',
  },

  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
});


class UsersComponent extends React.Component {

  constructor(){
    super();
    this.state={
      users:[]
    }
  }
  loadUsers = async () => {
    const users = await UserFetch.getUsers();
    if(users.successful) {
      this.setState({users:users.data})
      console.info("users have been loaded", users)
    }
    else console.error(`failed to load users - statusText is not "OK"`,users)
  }
  componentDidMount(){
    this.loadUsers();
  }
  render() {
    const { classes } = this.props;
    const users = this.state.users;
    
    return (
      <Paper className={classes.root}>
        <Table className={classes.table}>
          <TableHead>
            <TableRow>
              <TableCell align="center">Name</TableCell>
              <TableCell align="center">Email</TableCell>
              <TableCell align="center">Go to</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {users.map(row => (
              <TableRow key={row.id}>
                <TableCell>
                  {row.full_name}
                </TableCell>
                <TableCell>{row.email}</TableCell>
                <TableCell>
                  <Button color='secondary' className={classes.button} to={`/user/${row.id}`} component={Link}>
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

export const Users = withStyles(styles,{ withTheme: true })(UsersComponent);



