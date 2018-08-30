from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="broom",
    version="0.0.1",
    author="Luiz Lima",
    author_email="umluizlima@gmail.com",
    license="MIT License",
    description="Keep your desktop clutter-free.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umluizlima/broom",
    py_modules=['broom'],
    entry_points={
        'console_scripts': [
            'broom=broom:run',
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
