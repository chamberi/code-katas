"""The setup for my code wars kotas."""

from setuptools import setup

setup(
    name="snow day kotas",
    description="Code Wars kotas for our snow day.",
    version=0.1,
    author="Colin Lamont",
    author_email="colinlamont@gmail.com",
    license="MIT",
    py_modules=['fizz_buzz', 'flatten_me', 'multiples_2nums', 'seasick_snorkelling', 'sum_up', 'string_reversing'],
    package_dir={'': 'src'},
    install_requires=['tox'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov"]
    },
)
