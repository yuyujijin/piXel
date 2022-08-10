# piXel

**piXel** is a short program used to parse Pi's binary floating numbers and search for a given pixel art.

## Requierements

`python` is required to launch the program.

## Usage

**piXel** can be used by executing the following command : `./main.py <ART_FILENAME>`, where `<ART_FILENAME>` is the name of your pixel art file

## Pixel Arts

Pixel Arts must be of a rectangular shape, with 'X' and '.' only (thus it's a 1 bit pixel art). 

Pixel Arts must also be quite small, since the program will only look onto Pi's first 10^6 numbers (written in hexadecimals). 
This means that the program can sometime (often) fail to find your pixel art.
