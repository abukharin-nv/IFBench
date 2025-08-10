#!/usr/bin/env python3
"""Setup script for IFBench package."""

from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    with open(req_path, 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return requirements

# Read README for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="ifbench",
    version="1.0.0",
    author="Allen Institute for AI",
    description="IFBench: Generalizing Verifiable Instruction Following",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/abukharin-nv/IFBench",
    packages=['ifbench'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        '': ['data/*.jsonl', 'LICENSE', 'README.md'],
    },
    entry_points={
        'console_scripts': [
            'ifbench-eval=run_eval:main',
        ],
    },
)
