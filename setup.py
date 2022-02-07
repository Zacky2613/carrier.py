import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="carrier.py-Zacky2613",
    version="0.0.1",
    author="Zacky2613",
    author_email="author@example.com",
    description="A package used for minor annoyances that I experience throught coding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zacky2613/carrier.py",
    project_urls={
        "Bug Tracker": "https://github.com/Zacky2613/carrier.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)