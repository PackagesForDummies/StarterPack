# PackagesForDummies Starter Pack
## Introduction
Writing a Python package and installing it in your Python environment can't be easy, right?

*Right?*

Wrong. At least in newer Python versions.

To see how easy it is, let us first install this StarterPack package in a Python environment and use it in our code.

After that, we can look into what the package consists of, and how it was created.

## Installing the package
(Obs! This requires that the [Git command line client](https://git-scm.com/downloads) is already installed in your system. It also requires pip version 19 (from 2019) or newer in your Python environment. It has been tested with Python 3.10 and 3.12, but will probably work from Python 3.8 and up.)

If you are already working in an activated virtual environment (venv), install the package into that environment with this command:

    python -m pip install git+https://github.com/PackagesForDummies/StarterPack

You will notice that the syntax is different from a normal installation of a pre-built package where you just write the name of the package. More on this later. 

If you are **not** working in a virtual environment, you should. Please read [this guy's recommendations](https://www.bitecode.dev/p/relieving-your-python-packaging-pain), especially point 4, 5, 6 and 6 (yes, there are two).

## Using the package in a python script.
The package only contains two functions. They convert back and forth between °C and °F.

To test it, fire up your preferred editor and create a new python script with these contents:

    from starterpack import C2F, F2C

    tempF = 68.
    print(f"{tempF    = } °F")

    tempC = F2C(tempF)
    print(f"{tempC    = } °C")

    tempFnew = C2F(tempC)
    print(f"{tempFnew = } °F")
    
Save the script and run it. You should see this output:

    tempF    = 68.0 °F
    tempC    = 20.0 °C
    tempFnew = 68.0 °F

### So what? Is this supposed to be something special?
We have just installed and used a package, which did not come from PyPi. The package was not even built in advance. 

The package came from our own GitHub repository as pure python code, and it was built on the fly when we installed it.

The package is in Git version control. We can use the latest version across all of our projects. Or we can pin an old version in some of our projects if we have made changes in the package, which break the functionality in those projects.

Do you have python modules, which you use across several projects? Do you miss a way to manage them? Do you miss a way to install them without messing with your path or copying them into each of your projects?

If yes, yes and yes, this is for you!

## Explanation
### What happened here?
The URL in the pip command above points to the repository for this package project on Github.

By using the `git+https://...` syntax in the pip command, we asked pip to `git clone` this project to a local folder (using the installed Git client), build the package and install it as if it was a normal package.

After the package was installed, it could be imported in our Python code like any other installed packages. So we imported the package's two functions, `F2C` and `C2F`, into our Python script, wrote some code making use of those two functions, and ran that code.

In this case, the package contained functions. It could also have contained classes or variables or constants, and we would have imported them the same way.

### What is in this package?
Let us take a look. 

`cd` to a suitable folder and clone the full package project into a subfolder:

    git clone https://github.com/PackagesForDummies/StarterPack
    cd StarterPack

Now you can view the contents of the files in your preferred Python editor.

There are two files in the root of StarterPack. These are not part of the package itself and will not be installed with the package. But they are necessary for *creating* the package:

 - `README.md`: The file you are reading now
 - `pyproject.toml`: The configuration file for the package

In the subfolder `src`, we find the actual package. It consists of a folder named `starterpack`, which contains two files:
 - `__init__.py`: The file, which tells Python, that this folder is a package
 - `tempconvert.py`: The file, which contains the actual code of the package

### So how does the package work...?
This package shows the required minimum (almost) for a package:
 - A subfolder, which contains the package - or rather *is* the package
 - An `__init__.py` file
 - A `*.py` module file which contains the actual code of the package

**The module file**, `tempconvert.py`, is just an ordinary Python file. It contains two functions,`C2F` `F2C`, which converts between °C and °F.

In this case, there is only one module file, but there could have been more of them if needed.

**The `__init__.py` file** *could* have been an empty file. It just needs to be in the folder to tell Python that the folder is a package. However, I have put two non-necessary lines of code / documentation into the file:

    """A simple demo of package design"""
    from .tempconvert import C2F, F2C

The first line is a docstring. If you don't know docstrings, think of it as a tooltip on steroids. In most Python editors, the docstring for a package, a class, a function, etc. will be shown if you hover the mouse cursor over that object's name in the code. So this is information to the users of the package.

The second line is there to make imports a little easier for users of a package. Without this line, our import statements will need to include the name of the module file, so Python knows where to look for them:

    from starterpack.tempconvert import C2F, F2C

But objects, which are defined in `__init__.py` can be imported with this simpler syntax:

    from starterpack import C2F, F2C

Technically, you could put any Python code in `__init__.py`. The file will run when you import a package. You could put the full module in there and throw away`tempconvert.py´ (I think). But nobody does that.

### ...and how is the package being built from our package project?
If you have been looking for recommendations on building packages, you may have seen a lot of recipes pointing in all directions, using files and tools such as `setup.py`, `requirements.txt`, `distutils`, `setuptools`, etc. A lot of this is today either outdated or unnecessary to know about because it happens automatically in the background.

The status today (March 2024) is:
 - You can usually handle all your configuration in one file, `pyproject.toml`, including selection of the packaging tool, which is going to use that configuration.
 - To build a package, you just need to run the `build` module. `build` will then look in the `pyproject.toml`, identify your choice of packaging tool, download this tool and run it. But let us forget all that, because...:
 - `pip` will automatically use `build` to build the package when installing an unbuilt package from source.
 
 The `pyproject.toml` for our project contains this configuration at the top (but could be anywhere in the file):

    [build-system]
    requires = ["setuptools >= 61.0"]
    build-backend = "setuptools.build_meta"

    [tool.setuptools.packages.find]
    where = ["src"]

The first section says that we will be using `setuptools` for the build process.

The second section says that the package folder can be found in the `src` subfolder.

The rest of the file, not listed here, is:
 - Project metadata
 - Name of the readme file (also needed by he build process!)
 - Dependencies (none for this project)

A few links on package creation and the contents of a pyproject.toml:

[Setuptools quickstart guide](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)  
[Setuptools configuration guide](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)  
[Python.org packaging guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)


## Other topics
### What if I want to be able to edit my package while it is installed?
You can install the package with the --editable option in your virtual environment. I usually do.

    python -m pip install --editable git+https://github.com/PackagesForDummies/StarterPack#egg=starterpack

(This can be a little quirky. Notice the addition of `#egg=starterpack` at the end of the URL. This is necessary to avoid an error during installation. It seems redundant, but I have not found a way around it. [This Issue at PyPa's GitHub repository](https://github.com/pypa/setuptools/issues/3606) perhaps gives some of the explanation.)

When the package is installed as editable in your virtual environment, it will be installed in a separate subfolder, together with all the project files and Git information. You can edit the package in this folder, and you will often see the changed behaviour immediately after a new import. If you think your changes are worth keeping, you can commit them locally to Git and push your commit back to GitHub. 

### Is there anything in this package, which didn't need to be there?
Docstrings are already mentioned. You don't need them. But they are nice.

I have also included type hints in the functions (the `:float` after argument names). Again, you don't need them, but they are nice. They tell your IDE and some code checking tools what type of variable to expect as input and output to/from a function.

Having the package folder in a `src` folder is not needed either. A lot of packages have the package folder as a subfolder directly under the package project's root folder. But the use of a `src` folder can prevent some future problems. As an example, a broken, uninstallable package can falsely appear to work okay in tests if the `src` folder is omitted. By having the package folder in a `src` folder, there is a higher chance of failure during test, which is what we want, rather than failure during installation later.

## What's next
This package did not have any dependencies to other packages. Next time let us look at a package with dependencies. Stay tuned for the next package project.
