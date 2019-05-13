import { MuiThemeProvider, createMuiTheme } from '@material-ui/core';  
import { pink, teal } from '@material-ui/core/colors'

export const theme = createMuiTheme({
    palette: {
      primary: pink,
      secondary: {
        main: teal[500]
      }
    }
  })