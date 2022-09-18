# MDS-BSG-Rosalind

## Instructions

### Create new virtual environment

To create a new virtual environment in which we are going to work we should install virtualenv (better than venv).

First we should upgrade pip3:
```sh
py -m pip install --upgrade pip
```

Then, we should install virtualenv.exe

```sh
pip3.10 install virtualenv
```

Once we have virtualenv we should create the new environment, we have to name it. In my case I named as .venv:
```sh
virtualenv .venv
```

### Activate the environment
Then we have to activate the environment:

```sh
source .venv/Scripts/activate
```

We can use pip list to see the current packages installed. We should see something like this:

```sh
$ pip list
Package    Version
---------- -------
pip        22.2.2
setuptools 65.3.0
wheel      0.37.1
(.venv) 
```

Now, we have to install the required packages or use a requirements.txt file:

```sh
pip install networkx
pip install matplotlib
pip install biopython
```

Once we have installed all the required packages, we can generate a requirements file using pip freeze comand:

```sh
pip freeze > requirements.txt
```

### Install the required packeges from requirements file
If we want to install the same packages with the current versions we have to use the requirements file:

```sh
pip install -r requirements.txt
```

This help us to ignore the virtual environment in a source control system, we only need to import the requirements file.
