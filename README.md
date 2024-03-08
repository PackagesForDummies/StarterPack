# PackagesForDummies Starter Pack
## Introduction
Writing a Python package and installing it in your Python environment can't be easy, right?

*Right?*

Wrong.

To see how easy it is, let us first install this StarterPack package in a Python environment and use it in our code.

After that, we can look into what the package consists of, and how it was created.

## Installing the package
Obs! This requires that the [Git command line client](https://git-scm.com/downloads)is already installed in your system. 

If you are already working in an activated virtual environment (venv), install the package into that environment with this command:

    python -m pip install git+https://github.com/PackagesForDummies/StarterPack

You will notice that the syntax is different from a normal installation of a pre-built package where you just write the name of the package. More on this later. 

If you are **not** working in a virtual environment, you should. Please read [this guy's recommendations](https://www.bitecode.dev/p/relieving-your-python-packaging-pain), especially point 4, 5, 6 and 6 (yes, there are two).

## Using the package in a python script.
The package only contains two functions for converting back and forth between °C and °F.

To test it, fire up your preferred editor and create a new python script with these contents:

    from starterpack import C2F, F2C
    
    tempF = 50
    print("{tempF = } °F")
 
    tempC = F2C(tempF)
    print("{tempC = } °C")
 
    tempFnew = C2F(tempC)
    print("{tempFnew = } °F")

Save the script and run it. You should see this output:

TODO: To be continued
