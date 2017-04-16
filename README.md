# Sequential-Circuit-Transformation
Research project for Dr. Jackie Rice

## Getting Started
This project assumes a Linux environment and requires at least Python version 2.7.0 or higher to be installed. 

In order to use the GUI, Python 3.0 or higher and Tkinter must be installed.

Once dependencies are installed, download the latest release [here.](https://github.com/CPSC3720/Sequential-Circuit-Transformation/releases/tag/v1.0)

## How to use
After downloading and unpacking the latest release, processing .kiss2 files and gathering metrics can be done via command-line or GUI. It is important the .kiss2 files that need to be processed are contained either in the `inputs/` directory included in the release, or your own specified directory:

To begin gathering metrics, type:

```
python main.py
```

The call above assumes the .kiss2 files are contained in the `inputs/` directory. To specify another directory, simply pass the path to that directory as an argument to `main.py`:

```
python main.py path/to/another/directory
```

In order to use the GUI, from the root of the project, type:

```
python3 GUI/gui.py
```
