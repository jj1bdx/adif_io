import setuptools

with open("README.md", "r", encoding="utf_8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adif_io",
    version="0.0.3",
    author="Andreas Krüger (DJ3EI)",
    author_email="dj3ei@famsik.de",
    description="Basic input of ADIF radio amateur log files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/andreas_krueger_py/adif_io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Communications :: Ham Radio"
    ],
    python_requires='>=3.5',
)
