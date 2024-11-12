# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:45:00 2020

@author: Estavillo
"""

from typing import List
from fintools.utils import get_logger
from fintools.utils import method_caching
from fintools.utils import timeit
logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @method_caching
    def element(self, position: int) -> int:
        if position <= 0:
            return 0
        elif position == 1:
            return 1
        else:
            return self.element(position - 1) + self.element(position - 2)

    @timeit
    def sequence(self, length: int) -> List[int]:
        seq = [self.element(i) for i in length]
        return seq
