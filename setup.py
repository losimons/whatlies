from setuptools import setup, find_packages

base_packages = [
    "numpy>=1.16.0",
    "scipy>=1.2.0",
    "scikit-learn>=0.20.2",
    "umap-learn>=0.3.10",
    "altair>=4.0.1",
    "matplotlib>=3.2.0",
    "spacy>=2.2.3",
    "networkx>=2.4",
    "sense2vec>=1.0.2",
]

docs_packages = [
    "mkdocs==1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings==0.8.0",
    "jupyterlab>=0.35.4",
    "nbstripout>=0.3.7",
    "nbval>=0.9.5",
]

test_packages = [
    "flake8>=3.6.0",
    "nbval>=0.9.1",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "pytest-cov>=2.6.1",
    "nbval>=0.9.5",
    "pre-commit>=2.2.0"
]

dev_packages = docs_packages + test_packages

setup(
    name='whatlies',
    version="0.2.5",
    author="Vincent D. Warmerdam",
    packages=find_packages(exclude=['notebooks', 'docs']),
    description="Make visualisations to learn `what lies` in word embeddings.",
    install_requires=base_packages,
    extras_require={"docs": docs_packages, "dev": dev_packages, "test": test_packages},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
