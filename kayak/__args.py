import numpy as np

from qpid.args import DYNAMIC, STATIC, TEMPORARY, EmptyArgs


class KayakArgs(EmptyArgs):

    @property
    def generation_num(self) -> int:
        """
        Number of multi-style generation.
        """
        return self._arg('generation_num', 20, argtype=STATIC)
    