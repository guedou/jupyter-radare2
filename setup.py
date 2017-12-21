# Copyright (C) 2017 Guillaume Valadon <guillaume@valadon.net>


import os
import json
from setuptools import setup

from jupyter_client.kernelspec import install_kernel_spec
from IPython.utils.tempdir import TemporaryDirectory


setup(name="jupyter_radare2",
      description="A Jupyter radare2 kernel",
      author="Guillaume Valadon",
      author_email="guillaume@valadon.net",
      version="0.1",
      url="https://github.com/guedou/jupyter_radare2",
      py_modules=["radare2"],
      )


install_directory = install_kernel_spec("./kernel_spec", "radare2", user=True,
                                        replace=True)
