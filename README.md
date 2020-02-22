# fscleaner

a file management utility to reame and delete files and folders

<a href="https://pypi.org/project/fscleaner/">
    <img src="https://img.shields.io/badge/pypi-v2.1.0-blue.svg"></a>

<a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-%E2%89%A53.5.3-yellow.svg"></a>

## License
Copyright © 2020 isubham

Licensed under the MIT License (see ``LICENSE.txt`` for details).


## Installing

To install fscleaner

    pip install fscleaner
## Requirements

- Python ≥3.5.3

## Quick Examples

_parameters_

specify location

-p c:\\some location (use absolute location)

removes space in file and folder names with _ or trim spaces

-s  "" default
    
removes the specified file types in this sceanario .zip and .VTT

-d .zip .vtt .png

    import fscleaner
    fs = fscleaner("-s _ -p c:\\ee\ee\\ -d .vtt .zip")
    fs.activate()
