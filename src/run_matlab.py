import matlab.engine
import os 
import settings

def run_matlab():
    """
    Runs the MATLAB file (.m) using MATLAB Engine
    """
    # Start MATLAB Engine
    eng = matlab.engine.start_matlab()
    
    # Add path the MATLAB files
    matlab_path = os.path.abspath("data")
    eng.addpath(matlab_path)
    
    # Run MATLAB file
    matlab_command = "eng.{0}(nargout=0)".format(os.getenv("MATLAB_FILENAME"))
    print(matlab_command)
    ret = exec(matlab_command)
    
    # Quit MATLAB Engine
    eng.quit()

if __name__ == "__main__":
    run_matlab()



