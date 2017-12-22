# jupyter-radare2

[![GitHub tag](https://img.shields.io/github/tag/guedou/jupyter-radare2.svg)](https://github.com/guedou/r2m2/releases)
[![Twitter Follow](https://img.shields.io/twitter/follow/guedou.svg?style=social)](https://twitter.com/intent/follow?screen_name=guedou)

This is a simple [radare2](https://github.com/radare/radare2)
[Jupyter](http://jupyter.org/) kernel, that can be used to make interactive
radare2 tutorials, or take advanced notes.

## Demos

The kernel can be used either from a notebook or a console:

[![notebook](https://github.com/guedou/jupyter-radare2/blob/master/examples/radare2_kernel_test.png)](https://github.com/guedou/jupyter-radare2/tree/master/examples/radare2_kernel_test.ipynb)

```
jupyter console --kernel radare2
Jupyter console 5.2.0

radare2 Jupyter kernel


In [1]: o /bin/ls
9
In [2]: afl

In [3]: afl~main

In [4]: pd 5
;-- entry0:
            0x00005430      31ed           xor ebp, ebp
            0x00005432      4989d1         mov r9, rdx
            0x00005435      5e             pop rsi
            0x00005436      4889e2         mov rdx, rsp
            0x00005439      4883e4f0       and rsp, 0xfffffffffffffff0
In [5]:                                                                                                                                               
Do you really want to exit ([y]/n)? y
Shutting down kernel
```


## Installing the kernel

Check that `radare2` is present in your $PATH, then type:
```
virtualenv ve_r2_kernel
source ve_r2_kernel/bin/activate
pip install jupyter r2pipe
python setup.py install
```

## De-installing the kernel

Simply type:
```
deactivate
rm -rf ve_r2_kernel
rm -rf $HOME/.local/share/jupyter/kernels/radare2
```
