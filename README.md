## Supplementary code for "Finding Hamiltonian cycles with Graph neural networks"
## I am updating this project as part of my graduate work and graduate thesis. All credit goes to the original authors: Filip Bosnic (University Zagreb) and Mile Sikic (Genome Institute of Singapore)

### Paper
* [Paper](https://arxiv.org/pdf/2306.06523) on arxiv

### Requirements:
* [Python](https://www.python.org/) 3.8 or later
* [PyTorch](https://pytorch.org/) 1.8 or later
* [PyTorch geometric](https://pytorch-geometric.readthedocs.io/en/latest/index.html) 1.6.3 or later
* [Networkit](https://networkit.github.io/)
* [Concorde TSP solver](http://www.math.uwaterloo.ca/tsp/concorde.html) (optional)

### Setup
(Commands are supposed to be run from the root environment)
* Use conda to create a new environemnt with (Linux)
```
export ENV_NAME="hamgnn"
conda env create --file requirements.yaml --name $ENV_NAME
```
Windows equivalent: 
```
set ENV_NAME=hamgnn
conda env create --file requirements_windows.yaml --name %EVN_NAME%
```
* Then add this package in develop mode (same for Linux and Windows)
```
pip install -e .
```

### Main model training
* Start the training with
```
python terminal_scripts/train_main_model.py
```
This should log a wandb run and produce a checkpoint in `MODEL_CHECKPOINTS` directory. Training data is generated on the fly.

### Generate testing data with an exact solver
* Install Concorde TSP solver from [https://www.math.uwaterloo.ca/tsp/concorde.html]
* Update the following fields in `./config.cfg` file:
    * CONCORDE_SCRIPT_PATH - path to "concorde" executable created during concorde install
* Generate data for various experiments by running
```
python terminal_scripts/generate_data.py
```
After completion, this should create several dataset in the `./DATA` folder.
* The model can be tested on generated data by running
```
python terminal_scripts/test_main_model.py
```
It prints the output in somewhat raw format, the percentage of HCP solved can be seen in `perc_hamilton_found` column. A nicer output format will be added soon...
* To generate all the figures presented in the paper, run
```
python terminal_scripts/generate_figures.py
```
**Note, this will take a very long time since several different models need to be trained.**
* A list of model that have been tried out during experimentation can be found in `hamgnn/models_list.py`. All models listed there should theoretically be runnable with:
```
python terminal_scripts/train_model_variation.py <experiment_name>
```
where <experiment_name> corresponds to the name of the python variable to which the experiment has been assigned inside `hamgnn/models_list.py` file.

## Notes:
* The code in ```hamgnn/legacy/``` is depricated and will be removed eventually
