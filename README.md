# Tailored Pattern Maker
<H1>Description<H1>

Tailored Pattern Maker is a Python program designed to generate custom sewing patterns in SVG format based on user-provided measurements. This tool is ideal for creating precise patterns for clothing or other fabric-based projects. The generated SVG files can be easily imported into vector graphics software (such as Inkscape or Adobe Illustrator) for further editing or used directly for cutting fabric.

The program consists of three main Python files:





main.py: Contains the user-defined measurements and orchestrates the program's execution.



pattern_logic.py: Handles the calculations and conversions from measurements (in inches) to coordinates.



svg_generator.py: Uses the drawsvg library to create the SVG pattern based on the coordinates provided by pattern_logic.py.


Usage





Open main.py and locate the section where measurements are defined. Edit these variables to input your desired measurements.



Run the program using Python:

python main.py



The program will generate an SVG file named pattern.svg in the same directory as the script.

Important: The program currently requires users to edit main.py directly to set measurements. Future updates may include support for command-line arguments or configuration files for easier input.
