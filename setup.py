import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

repo_name = 'Chicken-Disease-Classification'
author_user_name = "Crackedwarrior"
src_repo = "cnnClassifier"
author_email = "ujwalshettyr@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description="A small python package for CNNwr app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author_user_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
