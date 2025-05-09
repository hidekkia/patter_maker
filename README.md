
<H2>Description</H2>

Tailored Pattern Maker is a Python program designed to generate custom sewing patterns in SVG format based on user-provided measurements. This tool is ideal for creating precise patterns for clothing or other fabric-based projects. The generated SVG files can be easily imported into vector graphics software (such as Inkscape or Adobe Illustrator) for further editing or used directly for cutting fabric.

The program consists of three main Python files:

1. **main.py**: Contains the user-defined measurements and orchestrates the program's execution.
2. **pattern_logic.py**: Handles the calculations and conversions from measurements (in inches) to coordinates.
3. **svg_generator.py**: Uses the drawsvg library to create the SVG pattern based on the coordinates provided by pattern_logic.py.

<H2>Usage</H2>

1. Open main.py and locate the section where measurements are defined.
2. Edit the variables to input your desired measurements.
3. Run the program using Python (main.py):

  The program will generate an SVG file named pattern.svg in the same directory as the script.
  Expected Result:
  [![alt text](file:///D:/tailored%20pattern%20maker%202.0/GU_pattern_test.svg)](https://github.com/hidekkia/patter_maker/issues/1#issue-3050601133)

> Important: The program currently requires users to edit main.py directly to set measurements. Future updates may include support for command-line arguments or configuration files for easier input.
