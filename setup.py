import os
import setuptools
#this somehow doesn work, import error
#from leaderboard import __version__
__version__ = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()


def requirements_from_txt(path_to_txt):
    path_to_reqs = os.path.join(os.path.dirname(__file__), "requirements")
    with open(os.path.join(path_to_reqs, path_to_txt), "r") as f:
        reqs = f.readlines()
    return [req for req in reqs if not req.startswith("#")]


setuptools.setup(
    name="pydata-leaderboard",
    author="Fabian Gebhart",
    version=__version__,
    setup_requires=["setuptools_scm"],
    install_requires=requirements_from_txt("requirements.txt"),
    include_package_data=True,
    description="Django App for visualizing the Ranking of the Bot Challenge during the PyData Global 2020",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fgebhart/pydata-leaderboard",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    extras_require={
        "testing": requirements_from_txt("dev-requirements.txt"),
    },
)
