# Keyboard Heatmap Generator

This script generates a heatmap visualization of keyboard usage based on input text. It also calculates the total distance traveled by fingers while typing the input text.

## Prerequisites

The following libraries are used in the notebook, ensure they are installed before running them.

- matplotlib
- numpy
- scipy

```
pip install matplotlib numpy scipy
```

## Usage

1. Open the python notebook submitted. Modify the second cell which contains the layout file to add the name of the layout file which is being used for the testing. Ensure that the layout file is in the same directory as the notebook and contains exactly two dictionaries - keys and characters - which are of the same format as the given example

2. Execute all the cells in succession until the main() function prompts for input. Tweak the heatmap plotting parameters like smoothness and resolution to requirement. The heatmap cmap may also be adjusted if required. 

3. When prompted, enter the text you want to analyze. If you press Enter without inputting any text, the script will display the default keyboard layout without a heatmap. It is assumed that a press of Enter or newline marks the end of the input.

4. The script will generate a visualization of the keyboard with a heatmap overlay, showing the frequency of key usage.

5. After displaying the heatmap, the script will print the total keyboard travel distance for the input text.

## Features

- Generates a heatmap visualization of keyboard usage
- Displays both lowercase and uppercase characters on the keyboard, in a structure similar to what was given as the example
- Shows symbols accessible via the Shift key
- Calculates and displays the total distance traveled by fingers while typing
- Supports special keys like Shift, Ctrl, Alt, and Space

## Customization

You can modify the `keys` and `characters` dictionaries in the script to adjust the keyboard layout or character mappings if needed. Please ensure they are identical in format to the example as the notebook has been optimized for the same.

## Output

The notebook produces two main outputs:

1. A graphical representation of the keyboard with a heatmap overlay, displayed using matplotlib.
2. A console output showing the total keyboard travel distance for the input text.

## Note

This notebook uses a simplified model of typing and finger movement. The travel distance calculation is based on the assumption that fingers always return to their home row position after each keystroke. Also, the travel distances are computed only one way while in reality they must be counted twice. Please pay careful attention to the final plot to gain insights on the frequencies of the keystrokes.
