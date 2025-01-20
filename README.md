# Explainable AI for Affective Computing
##### SoSe2024 Bielefeld University

In this seminar we will learn about the latest research in eXplainable AI (XAI) and its application for the field of affective computing.  This reposity will contain a series of [Jupyter Notebooks](https://jupyter.org/) to give you practical experience in implementing state-of-the-art explainablity techniques using various Python packages.

## Installation Instructions

### Install Anaconda

We will use Anaconda for the management of virtual environments and python package installations.

Download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html), a lightweight installation of anaconda (if you already have the full version of anaconda installed, that will work as well).

### Create Virtual Environment and Install Necessary Python Packages

After installing miniconda, you now have the ability to easily create and manage Python virtual environments using the `conda` command. For the Jupyter Notebooks used in this seminar, we recommend you create a new virtual environment to manage the various Python packages we will use through out the semester.  

If you're not already familiar with `conda`, you may want to familiarize your self with the [documentation](https://docs.conda.io/projects/conda/en/latest/commands.html) and the various commands in [this cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

To create a new virutal env for this seminar, run the following commands from your conda terminal.

1. Create a new virtual env named 'ml_bias_seminar' with the latest version of Python3:
 	- `conda create -n sose24_xai_ac python=3.10`
2. Activate the new virtual env:
	- `conda activate sose24_xai_ac`
3. Install the required Python packages (The requirements.txt will be updated to include all necessary packages for the notebook assignments)
	- `pip install -r requirements.txt`


## Getting Started with the Notebooks

### Clone the Seminar GitHub Repo

All notebooks during the semester will be provided through this GitHub repository.  The easiest way to obtain the notebooks is to `clone` this repository, and then perfrom a `git pull` when we announce that new notebooks are available. Here I will provide terminal instructions to clone and pull the repo, but you are free to use your preferred GUI or Git interface.

1. To `clone` the repository:
	- First make sure you have in a directory where you would like to store the repository
	- `git clone \<LINK TO REPO\>`
	- This will download all the current notebooks and material into a folder named \<REPO NAME\>

2. If we announce a new notebook or repository changes, then `pull` from the repo to get the latest material
	- make sure you are in the cloned directory named \<REPO NAME\>
	- run: `git pull`
	- You should recieve a message indicating new files were downloaded

### Running a JupyterLab and Launching a Notebook

For this seminar, we will use [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) to run and manage our Notebooks.

1. Start JupyterLab
	- make sure you virtual env is activated
	- run: `jupyter lab`
	- This should automatically open JupyterLab in your browswer window
	- if not, open the URL provided in your terminal output
2. To create a new Notebook
	- Go to the "Launcher" tab and click the Python icon in the "Notebook" section
3. To open an existing notebook
	- In the file explorer pane on the left, browse to an `.ipynb` file and doubleclick it

### Validate Your Virtual Environmenmt Installation

To validate your virtual env installation, and make sure you are able to run a simple notebook

1. In JupyterLab, open `validate_installation.ipynb`
2. Follow the instructions in the Notebook

### (Optional) Intro to ML Notebook

As an example, you can also familiarize yourself with the Notebook we will use in our first lecture: `intro_ml.ipynb`

## Notebook 1
To get started with Notebook 1:

**Note:** these instructions assume you've previously cloned the repository and set up your python environment per the above instructions. If not, return to the beginning of the README and follow the installation instructions.

1. Update your local repository with `git pull`
2. Activate your conda env (if not already activated): `conda activate sose24_xai_ac`
3. Update your conda env with the latest python packages: `pip install -r requirements.txt`
4. Download necessary models from Moodle, section [Jupyter Notebook #1](https://moodle.uni-bielefeld.de/course/view.php?id=4376#section-6).
    - Extract files to the `models` folder in your local repository
5. Launch Jupyter Lab: ```jupyter lab```
6. Test importing tensorflow and other packages from the `requirements.txt` file
	1. You can also test loading the tensorflow model:
```python
# make sure you've downloaded the models from Moodle 
model_path = '../models/affectnet_model_e=60/affectnet_model'

# load the weights
model_xai = cnn_model(input_shape=(128, 128, 3), num_classes=8)
model_xai.load_weights(model_path).expect_partial()
```
7. Open the notebook called `notebooks/1. simplification_attribution.ipynb`
8. Follow the instructions in the notebook

## Notebook 2
To get started with Notebook 2:

**Note:** these instructions assume you've previously cloned the repository and set up your python environment per the above instructions. If not, return to the beginning of the README and follow the installation instructions.

1. Update your local repository with `git pull`
2. Activate your conda env (if not already activated): `conda activate sose24_xai_ac`
3. Update your conda env with the latest python packages: `pip install -r requirements.txt`
4. Download necessary models from Moodle, section [Jupyter Notebook #2](https://moodle.uni-bielefeld.de/course/view.php?id=4376#section-12).
    - Extract files to the `models` folder in your local repository
5. Launch Jupyter Lab: ```jupyter lab```
6. In this session, I've created two notebooks to make each task easier to manage
   - Notebook 2 Part 1: `notebooks/2.1 dice_cfs_ser.ipynb`
   - Notebook 2 Part 1: `notebooks/2.2 shap_attribution_ser.ipynb`
7. Open each notebook and ensure you can successfully run the imports statements
   - If not, try recreating your conda environment
   - Email me for support
7. Follow the instructions in the notebook to complete the tasks