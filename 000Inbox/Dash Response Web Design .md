---
tags:
  - frontend
---
# Dash Response Web Design 



基本知識

<https://medium.com/misa-design-%E5%A0%AF%E8%88%9C%E8%A8%AD%E8%A8%88/bootstrap-4-%E5%81%9A-rwd-%E8%B6%85%E7%B0%A1%E5%96%AE-%E5%85%A9%E6%AD%A5%E9%A9%9F%E5%81%9A%E5%87%BA%E6%B5%81%E8%AE%8A%E6%A0%BC%E7%B7%9A%E7%B6%B2%E9%A0%81-f10c09c41031>

字體

<https://aoimonotw.blogspot.com/2021/02/max-font-size.html>



## Basic CSS

- Priority of Select:   important > inline style > ID  > class > Tag > \* 萬用 >  繼承上層

- `` `<div id”> ``

```html
<div id="main-header" class="menu"> Word </div>
```

```css
#main-header {
  color: red;
}

.menu{
  color: bule;
}
div{
  color: green;
}

*{
  color: red !important;
}
```

- How to Do RWD

   - Fluid Grids: Instead of fixed pixel widths, use relative units like percentages or ems to define the layout. This allows elements to scale proportionally to the screen size.

   - flex / flexbox***/*** in css:

   - Flexible Images: Use CSS to ensure images resize dynamically and fit their containers without overflowing. Set max-width: 100%; to prevent images from exceeding their parent's width.

      Media Queries: These are CSS rules that apply styles based on specific conditions, such as screen width, resolution, or orientation. Use them to create breakpoints and customize the layout for different screen sizes.

## Basic RWD in Dash

- **Use Percentage-Based Widths:** Set the width of your components using percentages instead of fixed pixel values. For example:

```python
html.Div([
    dcc.Graph(id='example-graph')

], style={'width': '100%'})
```





- **Automatic Sizing:** Set `responsive=True` in your `dcc.Graph` component to automatically adjust the graph size based on the container.

   - `dcc.Graph(id='example-graph', figure=fig, config={'responsive': True})`



## Dashboard

Source:

- [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/theme-explorer/gallery)

- 

```python

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
import dashboard1
import dashboard2

# Initialize the app
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# Define the layout with a location component to handle URLs
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Define the callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard1':
        return dashboard1.dashboard1_layout
    elif pathname == '/dashboard2':
        return dashboard2.dashboard2_layout
    else:
        return '404 Page Not Found'

if __name__ == '__main__':
    app.run_server(debug=True)

```