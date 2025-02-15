from setuptools import setup, find_packages

setup(
    name = "pyPhysumber",
    version = "2025.0.0a1",
    packages = find_packages(),
    include_package_data = True,
    install_requires=[],
    python_requires= ">=3.9" ,
    author = "Aitzaz Imtiaz",
    author_email = "aitzazimtiaz.ai@gmail.com",
    description = "Python library in computing Mathematics and Physics expressions",
    license = "AGPL-3.0-or-later",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=["Physics", "Mathematics", "Computation"],
)
