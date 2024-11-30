# This script MUST be in the same directory as the python notebook for errorless execution

import matplotlib
import matplotlib.pyplot as plt, matplotlib.patches as patches, numpy as np
from scipy.ndimage import gaussian_filter
from matplotlib.colors import LinearSegmentedColormap
from collections import Counter
from math import sqrt
import random, copy
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

from typing import List, Dict, Tuple, Optional
from qwerty_layout import keys, characters

def get_shift_char(key: str) -> Tuple[str, str]:
    
    """Returns the decomposition of the key.
    
    Parameters:
    key(str): The key that needs to be decomposed
    
    Returns:
    Tuple(str, str): The key pressed to print the character, and the corresponding
    shift key if pressed.
    
    For instance, # would return 3, Shift_R because those two keys are pressed
    to type the character #
    """
    
    shift_char = None
    normal_char = None
    
    #Iterate over the array of characters to see if a shift key is pressed
    for char, sequence in characters.items():
        if len(sequence) == 1 and sequence[0] == key:
            normal_char = char
        elif len(sequence) > 1 and sequence[1] == key:#Shift pressed
            shift_char = char
    return normal_char, shift_char

def calculate_key_frequencies(text: str) -> Dict:

    """Returns a dictionary of keys and frequencies
    Parameters:
    text(str): The text string for which the frequencies are counted.
    Returns:
    Dict: A dictionary holding all the unique key presses as keys and
    frequency of presses as values of the keys
    """

    key_frequency = Counter() #Initialises a Counter object which can be the dictionary

    for character in text:
        if character in characters:
            key_sequence = characters[character] #This handles the cases such
            # as special characters which have two keys pressed
            for key in key_sequence:
                key_frequency[key] += 1
    return key_frequency

def draw_key(ax, key: str, info: Dict[str, Tuple[float, float]], key_size: Tuple[float, float]) -> None:
    """
    Draws a single key on the keyboard plot.
    
    Parameters:
    ax (matplotlib.axes.Axes): The Matplotlib axis object where the key will be drawn.
    key (str): The label of the key
    info (Dict[str, Tuple[float, float]]): A dictionary containing information about the key,
    specifically the position of the key on the keyboard.
    key_size (Tuple[float, float]): The size (width, height) of the key.
    
    Returns:
    None: The function simply draws on the axes given as inputs.
    """
    
    x, y = info['pos'] #Finding position of the key
    key_width, key_height = key_size
    
    #Adjusting my key spacing and position for best viewability
    key_spacing = 0.1
    adjusted_x = x
    adjusted_y = y
    
    #Using patches to make the outline of the keys on the keyboard
    rect = patches.FancyBboxPatch(
        (adjusted_x, adjusted_y), 
        key_width - key_spacing, 
        key_height - key_spacing,
        boxstyle="round,pad=0.05", 
        linewidth=1.5, 
        edgecolor='black', 
        facecolor='none'
    )
    ax.add_patch(rect)
    
    #Find the base key and the shifts pressed for the key
    normal_char, shift_char = get_shift_char(key)
    
    #Display characters on the key
    if normal_char and shift_char and not normal_char.isalpha():
        ax.text(adjusted_x + (key_width - key_spacing) * 0.3, 
                adjusted_y + (key_height - key_spacing) * 0.7, 
                shift_char, ha='center', va='center', fontsize=14, color='black')
        ax.text(adjusted_x + (key_width - key_spacing) * 0.7, 
                adjusted_y + (key_height - key_spacing) * 0.3, 
                normal_char, ha='center', va='center', fontsize=18, fontweight='bold', color='black')
    else:
        #Display only the base key for no special character support
        ax.text(adjusted_x + (key_width - key_spacing) / 2, 
                adjusted_y + (key_height - key_spacing) / 2, 
                key, ha='center', va='center', fontsize=18, fontweight='bold', color='black')

def dist(pos1: Tuple, pos2: Tuple) -> float:
    """Returns the Euclidean distance between keys.
    
    Parameters:
    pos1, pos2: The position tuples indicating the (x, y) coordinates.
    
    Returns:
    float: The Euclidean distance between the two points.
    
    """
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def calc_distance(c: str, keys: Dict, characters: Dict) -> float:
    """
    Evaluates the travel distance to press this key from the home row.
    
    Parameters:
    c(str): The key whose travel distance is computed.
    
    Returns:
    float: The distance moved by the fingers to make the stroke.
    """
    
    key_sequence = characters[c] #Checks if more than one key is pressed for this key
    c1 = key_sequence[-1] #Takes the last key as the main key
    
    if c1 == 'Space': #Handling Space separately
        return dist(keys[c1]['pos'], keys[keys[c1]['start']]['pos'])
    
    elif len(characters[c]) == 1:
        return dist(keys[c]['pos'], keys[keys[c]['start']]['pos'])
    
    else: #Computing distance as sum when Shift is also pressed for special keys
        return dist(keys[characters[c][0]]['pos'], keys[keys[characters[c][0]]['start']]['pos']) + dist(keys[characters[c][1]]['pos'], keys[keys[characters[c][1]]['start']]['pos']) 