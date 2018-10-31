from setuptools import setup

setup(
 name="valerius",
 version="0.2.0",
 description="Biological sequence analysis tools.",
 url="https://valerius.samireland.com",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Topic :: Scientific/Engineering :: Bio-Informatics",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.5",
  "Programming Language :: Python :: 3.6",
  "Programming Language :: Python :: 3.7",
 ],
 keywords="biology bioinformatics genomes sequence",
 packages=["valerius"],
 install_requires=["requests"]
)
