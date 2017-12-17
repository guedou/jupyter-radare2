# Copyright (C) 2017 Guillaume Valadon <guillaume@valadon.net>

"""
A Jupyter kernel for radare2
"""


import r2pipe

from ipykernel.kernelbase import Kernel
from ipykernel.kernelapp import IPKernelApp


class Radare2Kernel(Kernel):
    """radare2 Jupyter kernel"""

    # Kernel information
    implementation = "radare2"
    implementation_version = "0.1"
    banner = "radare2 Jupyter kernel"

    # Language information
    language_info = {
        "name": "radare2",
        "mimetype": "text/plain",
        "file_extension": ".r2",
    }



    def _get_r2pipe(self):
        """Get the r2pipe handle"""

        if not hasattr(self, "r2"):
            self.r2 = r2pipe.open("-")

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        """Execute a radare2 commmand using r2pipe"""

        self._get_r2pipe()

        if not silent:
            result = self.r2.cmd(code)
            print result
            stream = {"name": "stdout", "text": result}
            self.send_response(self.iopub_socket, "stream", stream)

        return {"status": "ok",
                "execution_count": self.execution_count,
                "payload": [],
                "user_expressions": {},
               }


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=Radare2Kernel)
