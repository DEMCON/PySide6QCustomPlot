
# Introduction

These are PySide6 bindings for the [QCustomPlot library](https://www.qcustomplot.com/).

# Building

## Windows

Install required software:
- Qt 6.3.2
- Visual studio 2019 C++ compiler
- CMake
- Ninja

Create a virtual environment:

    > python -m venv .venv
    > .venv\scripts\activate.bat

We are targetting Qt 6.3.2. Install the apropriate shiboken6 generator:

    > pip install --index-url=https://download.qt.io/official_releases/QtForPython/ --trusted-host download.qt.io shiboken6==6.3.2 pyside6==6.3.2 shiboken6_generator==6.3.2

Use visual studio 2019 for compilation:

    > "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvars64.bat"

Now check the file CMakeLists.txt, and adjust paths to Qt and python.

Build the bindings:

    > mkdir build
    > cd build
    > cmake -G Ninja ..
    > ninja

To build a python wheel:

    > pip install build py-build-cmake
    > python -m build --no-isolation --wheel

Install the wheel:

    > pip install dist\pyside6qcustomplot-0.0.1-cp38-cp38-win_amd64.whl

## Linux

TODO

# TODO

- Release a python wheel package, so this extension can be installed with pip

# References

## Qt6.2 compatibility

For Qt6.2, the patch mentioned here is important: https://www.qcustomplot.com/index.php/support/forum/2380

## Shiboken binding example

- https://code.qt.io/cgit/pyside/pyside-setup.git/tree/examples/samplebinding/CMakeLists.txt

## Python packaging backend for CMake

A nice build backend to use when using CMake: https://github.com/tttapa/py-build-cmake

## Other binding projects

- https://github.com/mattja/QCustomPlot_PySide2/blob/master/bindings.xml

- https://github.com/SBGit-2019/Pyside-QCP/blob/master/src/bindings.xml
