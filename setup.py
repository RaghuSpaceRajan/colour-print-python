from setuptools import setup

packages = [
    "colour_print",
]

package_data = {"": ["*"]}


AUTHORS = (
    ", ".join(
        [
            "Raghu Rajan",
        ]
    ),
)

AUTHOR_EMAIL = "rajanr@cs.uni-freiburg.de"

LICENSE = "GNU GPL, Version 3.0"


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colour_print",
    py_modules=['colour_print.cp'],
    version="0.0.2",
    author=AUTHORS,
    author_email=AUTHOR_EMAIL,
    description="A python package to print coloured output, e.g., for debugging purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url="https://github.com/RaghuSpaceRajan/colour-print-python",
    project_urls={
        "Bug Tracker": "https://github.com/RaghuSpaceRajan/colour-print-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
    ],
    # package_dir={"": "src"},
    # python_requires=">=3.6",
    setup_requires=[],
    install_requires=[],
    extras_require={
    },
    entry_points={
    },
)
