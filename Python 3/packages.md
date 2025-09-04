## Packages with pip

You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index. You can browse the Python Package Index by going to it in your web browser.

### Install

You can install the latest version of a package by specifying a package’s name:

```
$ python -m pip install novas

Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

You can also install a specific version of a package by giving the package name followed by == and the version number:

```
$ python -m pip install requests==2.6.0
```

If you re-run this command, pip will notice that the requested version is already installed and do nothing. You can supply a different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

```
$ python -m pip install --upgrade requests

Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

### Uninstall

```python -m pip uninstall``` followed by one or more package names will remove the packages from the virtual environment.

```
$ python -m pip uninstall requests
```

### Show packages

```python -m pip show``` will display information about a particular package:

```
$ python -m pip show requests

---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
...
```

```python -m pip list``` will display all of the packages installed in the virtual environment:

```
$ python -m pip list

novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

### Export package list

```python -m pip freeze``` will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects. A common convention is to put this list in a ```requirements.txt``` file:

```
$ python -m pip freeze > requirements.txt
$ cat requirements.txt

novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

The ```requirements.txt``` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with ```install -r```:

```
$ python -m pip install -r requirements.txt

Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

```pip``` has many more options. Consult the [Installing Python Modules](https://docs.python.org/3/installing/index.html#installing-index) guide for complete documentation for pip. When you’ve written a package and want to make it available on the Python Package Index, consult the [Python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
