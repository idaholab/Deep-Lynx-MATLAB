% Change directories to data/ folder in repository
newFolder = cd("Deep-Lynx-MATLAB/data/")

% Load workspace variables
load('workplace_variables.mat');

% Run Simulink file (no file extension)
sim('simulink_file');

% Create table
results_table = table()
disp(results_table)

% Write table to csv
writetable(results_table,'results_table.csv') 

% Save workspace variables
% save('workplace_variables.mat');