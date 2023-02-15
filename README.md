# MATLAB Adapter

The Deep Lynx MATLAB Adapter is a Python application that connects the Deep Lynx data warehouse with any MATLAB simulation. The Deep Lynx MATLAB Adapter receives events from [Deep Lynx](https://github.com/idaholab/Deep-Lynx), modifies the workspace variables in the MATLAB (.m) file, and runs the input file with MATLAB. Returns from the MATLAB simulation are sent back to Deep Lynx for use by other applications.

## Edit Input File

The `edit_input_file.py` script edits the workspace variables in a MATLAB file (.mat) with project-specific data from Deep Lynx. 

Requirements
* Load and save workspace variables to .mat file
    * See `data/example/example.m` for help
* Deep Lynx payload that is project-specific
* Update code at specified `TODOs` in `edit_input_file.py`

## Run MATLAB

The `run_matlab.py` script runs the MATLAB file (.m) using MATLAB Engine.

## Environment Variables (.env file)
To run this code, first copy the `.env_sample` file and rename it to `.env`. Several parameters must be present:
* DEEP_LYNX_URL: The base URL at which calls to Deep Lynx should be sent
* CONTAINER_NAME: The container name within Deep Lynx
* DATA_SOURCE_NAME: A name for this data source to be registered with Deep Lynx
* DEEP_LYNX_API_KEY: The unique Deep Lynx API key for authentication
* DEEP_LYNX_API_SECRET: The unique Deep Lynx API secret for authentication
* DATA_SOURCES: A list of Deep Lynx data source names which listens for events
* MATLAB_FILENAME: The name of the MATLAB file to run (Note: Do not include file extension)
* IMPORT_FILE_WAIT_SECONDS: the number of seconds to wait between attempts to find a file to import into Deep Lynx
* REGISTER_WAIT_SECONDS: the number of seconds to wait between attempts to register for events

## Getting Started

* Complete the [Poetry installation](https://python-poetry.org/) 
* All following commands are run in the root directory of the project:
    * Run `poetry update` to install the defined dependencies for the project.
    * Run `poetry shell` to spawns a shell.
    * Finally, run the project with the command `flask run`

Logs will be written to a log file, stored in the root directory of the project. The log filename is set in `src/__init__.py` and is called `MATLABAdapter.log`. 

## Installation
1. Install MATLAB and Simulink version e.g. `R2020b`
2. Add MATLAB executable to PATH environment 

```
export PATH=/Applications/MATLAB_R2020b.app/bin/:$PATH
```

3. Update `pyproject.toml` with `matlabengine` version for a specific MATLAB version

```
# pyproject.toml
matlabengine = "9.9.1" # for R2020b
```
4. Install dependencies through poetry

```
poetry update
```
* Resources
    * [matlabengine GitHub](https://github.com/mathworks/matlab-engine-for-python/tree/R2022b)
    *   User guide for [matlabengine installation](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
        * Note: `matlabroot` is  the path to MATLAB e.g., `/Applications/MATLAB_R2020b.app/`

## Contributing

This project uses [yapf](https://github.com/google/yapf) for formatting. Please install it and apply formatting before submitting changes.
1. `poetry shell`
2. `yapf --in-place --recursive . --style={column_limit:120}`)

## Other Software
Idaho National Laboratory is a cutting edge research facility which is a constantly producing high quality research and software. Feel free to take a look at our other software and scientific offerings at:

[Primary Technology Offerings Page](https://www.inl.gov/inl-initiatives/technology-deployment)

[Supported Open Source Software](https://github.com/idaholab)

[Raw Experiment Open Source Software](https://github.com/IdahoLabResearch)

[Unsupported Open Source Software](https://github.com/IdahoLabUnsupported)

## License

Copyright 2022 Battelle Energy Alliance, LLC

Licensed under the LICENSE TYPE (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  https://opensource.org/licenses/MIT  

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Licensing
-----
This software is licensed under the terms you may find in the file named "LICENSE" in this directory.


Developers
-----
By contributing to this software project, you are agreeing to the following terms and conditions for your contributions:

You agree your contributions are submitted under the MIT license. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer.



