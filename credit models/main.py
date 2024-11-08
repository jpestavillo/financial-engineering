# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:51:11 2020

@author: Esteban
"""

import json
from difflib import SequenceMatcher

class StringWrapper:
    """
    This is the string wrapper.
    """

    def __init__(self, value: str, case_sensitive: bool = False):
        self._value = value
        self.case_sensitive = case_sensitive

    def _sensitivity_matching(self, string: str) -> str:
        return string if self.case_sensitive else string.lower()

    @property
    def value(self) -> str:
        return self._sensitivity_matching(string=self._value)

    def contains(self, pattern: str, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return (pattern in self.value) if not reverse else (self.value in pattern)

    def similarity_ratio(self, pattern: str) -> float:
        pattern = self._sensitivity_matching(string=pattern)
        return SequenceMatcher(None, self.value, pattern).ratio()

    def similar_enough(self, pattern: str, threshold: float) -> bool:
        pattern = self._sensitivity_matching(string=pattern)
        return self.similarity_ratio(pattern) > threshold

    def boolean_search(self, pattern: str, exact: bool, threshold: float, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return self.contains(pattern, reverse=reverse) if exact \
            else self.similar_enough(pattern, threshold=threshold)

with open('industries.json', "r") as f:
    content = f.read()
dictionary = json.loads(content)

def last_level(dictionary):
    while dictionary['children'] != []:
        n = len(dictionary['children'])
        level = [dictionary['children'][i]['title'] 
                 for i in range(n)]
        dictionary = dictionary['children'][0]
    return  level

def search_industry(dictionary, last_level = [], route = []):
    if not dictionary['children'] == []:
        for i in range(len(dictionary['children'])):
            search_industry(dictionary['children'][i], last_level = last_level)
    else:
        title = dictionary['title']
        if StringWrapper(title).boolean_search(pattern = 'aquaculture', exact = True, threshold = 0.5):
            last_level.append(title)
    return last_level
