# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:07:42 2021

@author: AKayal
"""
from functools import lru_cache
import math


class Polygon:
    """
    this class has following logic
    where initializer takes in:
        number of edges/vertices
        circumradius
        that can provide these properties:
            # edges
            # vertices
            interior angle
            edge length
            apothem
            area
            perimeter
            that has these functionalities:
                a proper __repr__ function
                implements equality (==) based on # vertices and circumradius (__eq__)
                implements > based on number of vertices only (__gt__) FUNCTION
    """
    
    def __init__(self, n, R):
        self.edges = n
        self.circumradius = R
        self.interiorAngle = (self.edges-2)*(180/self.edges)
        self.edgeLength = (2*self.circumradius)*math.sin(math.pi/self.edges)
        self.apothem = self.circumradius*(math.cos(math.pi/self.edges))
        self.area = (1/2)*(self.edges*self.edgeLength*self.apothem )
        self.perimeter =self.edges*self.edgeLength
        self.max_efficiency = self.area/self.perimeter

    
    def __len__(self):
        return self.edges
    
    def __getitem__(self, n, R):
        if isinstance(n, int):
            if n < 0 :
                raise IndexError
            else:
                return Polygon._polygon(self.edges,self.circumradius)
    
    @staticmethod #Static methods are methods that are bound to a class rather than its object.
    def _polygon(n, R):
        return Polygon(n, R)
    
    def __repr__(self):
        rep = 'Polygon(' + str(self.edges) + str(self.circumradius) + str(self.interiorAngle) + str(self.edgeLength) + str(self.apothem) + str(self.area) +  str(self.perimeter) + ')'
        return rep
    
    def __eq__(self, other):
       return self.edges == other.edges and self.circumradius == other.circumradius

    def __gt__(self, other):
       return self.edges > other.edges
   

        
        