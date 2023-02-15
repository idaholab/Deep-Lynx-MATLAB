import os
from scipy.io import loadmat, savemat
import numpy as np  
import settings
import json


def edit_input_file(payload = None):
    """
    Edits the workspace variables in a MATLAB file (.mat)
    """
    concentration = 2

    # TODO Get "payload" value from Deep Lynx to update the workspace variables
    
    # Load workspace variables from .mat file
    matlab_path = os.path.abspath("data")
    matlab_file = os.getenv("MATLAB_FILENAME") + ".mat"
    filename = os.path.join(matlab_path, matlab_file)
    input_file = loadmat(filename, mat_dtype=True)
    
    # Get list of variables in workspace
    variables = input_file.keys()
    variables = [ x for x in variables if "__" not in x ]
    
    # Update variables
    for i in variables:
        print(i)
        # TODO Update workspace variable "i" within "input_file" variable
        # input_file[i] = payload

    # Save updated workspace variables to a .mat file
    savemat(filename, input_file)

if __name__ == "__main__":
    edit_input_file()