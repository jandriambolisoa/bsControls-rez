name = "bsControls"

version = "2022"

authors = [
    "Brandon Schaal",
    "Jeremy Andriambolisoa"
]

description = \
    """
    Easily create control curves, change control curve colors, and replace control curve shapes. Changes colors on the shape level to 
    avoid all children of the controls inheriting drawing overrides, resets the colors at both shape and transform levels, and can replace 
    multiple shapes on controllers with either one or an equal amount of replacement shapes.
    """

requires = [
    ".python-3+",
    "maya-2022+",
]

uuid = "bsControls.bsControls"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")