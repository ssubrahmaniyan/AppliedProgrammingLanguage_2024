import numpy as np #Numpy is used to populate matrices and solve the equation system
from typing import List, Dict, Tuple

START_OF_CIRCUIT = '.circuit'
END_OF_CIRCUIT = '.end'

def parse_file(filename: str) -> List[str]:
    """Parses the circuit file and returns the nodes.

    Parameter:
    filename(str): The name of the SPICE file which needs to be solved for.

    Returns:
    List[str]: A list of the nodes in the circuit, which are lines containing the component parameters alone.

    This function is used to open the file, read it and discard unnecessary data including inline comments starting with '#'. 
    The nodes are returned in the form of a list, each of which contain the useful part of the SPICE file as a string, which
    can be processed to extract different parameters such as names and node names.
    """
    
    # Check existence of the file and create a filehandle
    try:
        filehandle = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("Please give the name of a valid SPICE file as input")
    
    # Read the file contents into a list and close the handle
    lines = filehandle.readlines()
    filehandle.close()
    
    # Extract useful information from the lines by removing comments
    # and renameing GND for convenience
    for i, line in enumerate(lines):
        lines[i] = line.split("#")[0].strip("\n")
        lines[i] = lines[i].replace('GND', 'n0')
    
    # Verify proper structure of the SPICE circuit and find boundaries
    try:
        st_ind = lines.index(START_OF_CIRCUIT) 
        end_ind = lines.index(END_OF_CIRCUIT)
        ckt_count = lines.count(START_OF_CIRCUIT)
        end_count = lines.count(END_OF_CIRCUIT)
    except ValueError:
        raise ValueError("Malformed circuit file")
    if ckt_count != 1 or end_count != 1:
        raise ValueError("Netlist has too many start/end identifiers")
    if end_ind - st_ind == 1:
        raise ValueError("No component found in the netlist")
    # Sorts the nodes by name for convenience and extract the component lines alone
    lines = lines[st_ind+1:end_ind]
    lines.sort()
    return lines

def make_dicts(components: List[List]) -> List[Dict]:
    """
    Makes dictionaries of nodes, resistances, voltage sources and current sources in the circuit.
    
    Parameters:
    components(List[List]): A list of components in the circuit, containing names, nodes connected to and the value of the component.

    Returns:
    List[Dict]: Returns 4 dictionaries, which map corresponding components to their parameter lists.

    This function makes dictionaries of the components in the circuit for easy handling during the equation matrix building.
    """
    # Initialize dictionary objects to hold values

    nodes = dict() # A dictionary, whose keys are the nodes, and values which are the connected components
    Resistances = dict()
    Vsources = dict()
    Isources = dict()
    
    # Process the components list
    for i in range(len(components)):
        temp = components[i].split() # Split the component into name, nodes, and value
        
        # Check if the node already exists in the dictionary and add the component
        if temp[1] in nodes.keys():
            nodes[temp[1]].append(temp[0])
        # If the node does not exist, make a new dictionary key and add the component
        else:
            nodes[temp[1]] = [temp[0]]
        if temp[2] in nodes.keys():
            nodes[temp[2]].append(temp[0])
        else:
            nodes[temp[2]] = [temp[0]]
        
        # Check if the components already exist in the corresponding lists and add them if not
        if components[i][0] == 'R':
            if len(temp) != 4: # Check for valid resistance specification
                raise ValueError("Invalidly specified resistance element")
            if temp[0] not in Resistances.keys():
                Resistances[temp[0]] = temp
        elif components[i][0] == 'V':
            if len(temp) != 5: # Check for valid presence of source type
                raise ValueError("Invalidly specified voltage source element")
            elif temp[0] not in Vsources.keys():
                Vsources[temp[0]] = temp
        elif components[i][0] == 'I':
            if len(temp) != 5: # Check for valid presence of source type
                raise ValueError("Invalidly specified current source element")
            if temp[0] not in Isources.keys():
                Isources[temp[0]] = temp
        else: # Raise error when components other than resistances or voltage/current sources are encountered
            raise ValueError("Only V, I, R elements are permitted")

    # Check for the valid presence of a GND node, otherwise, deem circuit invalid
    if 'n0' not in nodes.keys():
        raise ValueError("No GND node found")
    return [nodes, Resistances, Vsources, Isources]

def evalSpice(filename):
    """
    Evaluates the SPICE circuit and returns node voltages and currents through voltage sources.

    Parameters:
    filename(str): The name of the file which contains the circuit to be evaluated.

    Returns:
    Tuple[Dict]: Two dictionaries. The first contains the node voltages of all the nodes in the circuit while
    the second contains the currents through the voltage sources.

    This function runs all routine checks on the file given as input to solve for the circuit variables. It is 
    assumed that the circuit consists purely of resistances, and independent current and voltage sources and 
    will raise errors when not compliant. It also runs checks on the solvability of the circuit and returns the 
    solved variables for evaluation.
    """

    components = parse_file(filename)
    nodes, Resistances, Vsources, Isources = make_dicts(components)
    
    # Ensure the nodes dictionary contains only unique nodes without redundancies
    for node in nodes.keys():
        nodes[node] = list(dict.fromkeys(nodes[node]))
    
    # Create mappings of the nodes in the circuit to whole numbers which are used to index the coefficient matrix
    nodemap = {}
    i = 0
    for key in nodes.keys():
        if not key == 'n0': #Ignore GND node
            nodemap[key] = i
            i += 1
    # The index i is carefully handled to ensure the matrix is of the form required to solve
    # Create mappings of the voltage sources in the circuit to whole numbers, similar to node mapping above
    vsource_map = {}
    for v in Vsources.keys():
        vsource_map[v] = i
        i += 1
    
    # Compute the number of rows and columns the coefficient matrix will have
    num_rows = len(nodes.keys()) + len(Vsources) - 1 # Ignoring the GND node
    num_cols = num_rows

    # Initializing numpy zero matrices for coefficients and constants
    coeffs = np.zeros((num_rows, num_cols))
    consts = np.zeros((num_rows, 1))
    
    # Populating the matrices according to nodal analysis equations
    i = 0
    for node in nodes.keys():
        if not node == 'n0':
            for element in nodes[node]:
                if element[0] == 'R':
                    if float(Resistances[element][3]) == 0:
                        raise ValueError("Short circuit leading to infinite current encountered")
                    if Resistances[element][1] == node:
                        coeffs[i][nodemap[Resistances[element][1]]] += 1/float(Resistances[element][3])
                    elif Resistances[element][1] != 'n0':
                        coeffs[i][nodemap[Resistances[element][1]]] -= 1 / float(Resistances[element][3])
                    if Resistances[element][2] == node:
                        coeffs[i][nodemap[Resistances[element][2]]] += 1/float(Resistances[element][3])
                    elif Resistances[element][2] != 'n0':
                        coeffs[i][nodemap[Resistances[element][2]]] -= 1 / float(Resistances[element][3])
               
                elif element[0] == 'I':
                    if Isources[element][1] == node:
                        consts[i][0] -= float(Isources[element][4])
                    else:
                        consts[i][0] += float(Isources[element][4])
                
                elif element[0] == 'V':
                    if Vsources[element][1] == node:
                        coeffs[i][vsource_map[element]] += 1 
                    elif Vsources[element][2] == node:
                        coeffs[i][vsource_map[element]] -= 1
            i += 1

    for v in Vsources.keys():
        if not Vsources[v][1] == 'n0':
            coeffs[i][nodemap[Vsources[v][1]]] += 1

        if not Vsources[v][2] == 'n0':
            coeffs[i][nodemap[Vsources[v][2]]] -= 1
        consts[i] += float(Vsources[v][4])
        i+=1

    # Use numpy to solve the system and raise an error if the circuit is unsolvable
    try:
        ans = np.linalg.solve(coeffs, consts)
    except np.linalg.LinAlgError:
        raise ValueError("Circuit error: no solution")
    
    # Create the return dictionaries by mapping the solution values to the corresponding nodes
    nodeV = dict()
    for key in nodes.keys():
        if key == 'n0':
            nodeV['GND'] = float(0)
        else:
            nodeV[key] = float(ans[nodemap[key]][0])
    
    sourceI = dict()
    for key in Vsources.keys():
        sourceI[key] = float(ans[vsource_map[key]][0])
    
    # Returns dictionaries for evaluation
    return (nodeV, sourceI)

