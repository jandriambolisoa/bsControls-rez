name = "bsControls"

version = "2018"

authors = [
    "Brandon Schaal",
    "Jeremy Andriambolisoa"
]

description = \
    """
    Tool to help creating rigging controls.
    """

requires = [
    ".python-3+",
    "maya-2022+",
]

uuid = "bsControls.bsControls"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")