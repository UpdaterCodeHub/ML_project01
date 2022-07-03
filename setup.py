from setuptools import setup, find_packages
from typing import List

# Ceclaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION="0.0.2"
AUTHOR="Updater ML"
DESCRIPTION="Learning project from iNeuron FSDS November batch machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file


    return this function is going to return a list which containt name of 
    libraries mentioned in requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name="PROJECT_NAME",
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    #packages=find_packages() #["housing"],
    install_requires=get_requirements_list()

)


if __name__=="__main__":
    print(get_requirements_list())