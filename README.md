# cassini
Parsing and rendering OSRM raw data with Python

### First render :
![Capture](/images/capture1.png)

[Original Open street Map](http://www.openstreetmap.org/export#map=18/48.85470/2.37355)

### New Render, with roads included :
![Capture](/images/Capture2.PNG)

### Stylesheet support :
You are now able to use stylesheets to pick your own choice of colors!
The format of stylesheets is json, and heavily inspired on css:
* You can use selectors "key:value" to select an element (key or value can be omitted "key:" or "value:")
* The rules are cascading : if you have a previous rule for "building:", it will apply (if not overridden) in addition to any rule like "building:hospital"

### Moving around and zooming on the map:
You are now able to move around the map with the arrow keys of your keyboard, and to zoom with the mousewheel.

It's not really optimised yet, and moving around can be pretty slow, but we'll improve that soon!