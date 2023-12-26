import setuptools


with open('README.md','r',encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "end-to-end-machine-learning-with-mlflow"
AUTHOR_USERNAME = "AbdulAlim8660"
SRC_REPO = "krishnaikproject"
AUTHOR_EMAIL ="aabaig14@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for ml app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)