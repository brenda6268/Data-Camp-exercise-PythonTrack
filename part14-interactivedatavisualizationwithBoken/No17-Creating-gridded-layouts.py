#Creating gridded layouts
'''
Starting tabbed layouts
Tabbed layouts can be created in Bokeh by placing plots or layouts in Panels.

In this exercise, you'll take the four fertility vs female literacy plots from the last exercise and make a Panel() for each.

No figure will be generated in this exercise. Instead, you will use these panels in the next exercise to build and display a tabbed layout.

Instructions

Import Panel from bokeh.models.widgets.
Create a new panel tab1 with child p1 and a title of 'Latin America'.
Create a new panel tab2 with child p2 and a title of 'Africa'.
Create a new panel tab3 with child p3 and a title of 'Asia'.
Create a new panel tab4 with child p4 and a title of 'Europe'.
Click submit to check your work.
'''

# Code
# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')

'''

Displaying tabbed layouts
Tabbed layouts are collections of Panel objects. Using the figures and Panels from the previous two exercises, you'll create a tabbed layout to change the region in the fertility vs female literacy plots.

Your job is to create the layout using Tabs() and assign the tabs keyword argument to your list of Panels. The Panels have been created for you as tab1, tab2, tab3 and tab4.

After you've displayed the figure, explore the tabs you just added! The "Pan", "Box Zoom" and "Wheel Zoom" tools are also all available as before.

Instructions

Import Tabs from bokeh.models.widgets.
Create a Tabs layout called layout with tab1, tab2, tab3, and tab4.
Click 'Submit Answer' to output the file and show the figure.
'''

# Code
# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)