# bsControls-rez
A rez package for bsControls.

Easily create control curves, change control curve colors, and replace control curve shapes. Changes colors on the shape level to 
avoid all children of the controls inheriting drawing overrides, resets the colors at both shape and transform levels, and can replace 
multiple shapes on controllers with either one or an equal amount of replacement shapes.

## Requirements
* Maya 2022+

## Launch the tool in Maya
```
from bsControls import bs_controlsUI
bsCon = bs_controlsUI.BSControlsUI()
bsCon.bsControlsUI()
```