# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:28:35 2021

@author: AKayal
"""
from functools import lru_cache
import math
import session10_Polygon
from session10_Polygon import *

class PolygonSequence:
    """
    this custom sequence class has following logic
    where initializer takes in:
        number of vertices for largest polygon in the sequence
        common circumradius for all polygons
        that can provide these properties:
            max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
            that has these functionalities:
                functions as a sequence type (__getitem__)
                supports the len() function (__len__)
                has a proper representation (__repr__)
    """
    def __init__(self, polygon_vertices = [10,50,30,40,20],
                 circumradius = 30):
        self.polygon_vertices = polygon_vertices
        self.circumradius = circumradius
        
    def callc_max_effcncy(self):
        self.max_efficiency_list =  [Polygon(x, self.circumradius).__getattribute__("max_efficiency")
                                     for x in self.polygon_vertices
                                     if x > 0 ]
        
        self.max_efficiency_max = max(self.max_efficiency_list)
        self.max_efficiency_index = self.max_efficiency_list.index(self.max_efficiency_max)
        self.max_efficiency_vertices = self.polygon_vertices[self.max_efficiency_index]
        return self.max_efficiency_vertices

    # def __getattribute__(self, item):
    #     return self.item
        
    def __repr__(self):
        rep = 'PolygonSequence(' + str(self.max_efficiency_list) + str(self.max_efficiency_max) + str(self.max_efficiency_vertices) + ')'
        return rep
    
    def __len__(self):
        return len(self.polygon_vertices)
    
    # For getting the value from our custom_list

    def __getitem__(self, index):
        # print(f"value:{index}")
        if index > 0 and index < len(self.polygon_vertices):
            return self.polygon_vertices[index]
        else:
            return IndexError       


# xx = PolygonSequence()
# print(xx.callc_max_effcncy())
# print(type(xx[3]))