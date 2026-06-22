import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-ML-Flow"
AUTHOR_USER_NAME = "PrajnaShe"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "prajna.shetty2006@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="PrajnaShe",
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)