from setuptools import setup, find_packages

setup(
    name="lavai-ui",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "lavai"
    ],
    entry_points={
        'console_scripts': [
            'lavai-ui=lavai_ui.cli:main',
        ],
    },
    author="Heron4gf",
    author_email="aldo@giambuzzi.it",
    description="A UI for managing AI provider credentials stored by the lavai library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Heron4gf/lavai-gui",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
