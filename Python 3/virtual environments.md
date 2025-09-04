## venv
The module is used to create and manage virtual environments.

### Create environment 
This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.
```
$ python --version
python3.12
$ python -m venv tutorial-env
```

### Activate environment

Windows:
```
$ tutorial-env\Scripts\activate
```

MacOS:
```
$ source tutorial-env/bin/activate
```

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python.

```
$ tutorial-env\Scripts\activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
```

### Deactivate environment

```
$ deactivate
```
