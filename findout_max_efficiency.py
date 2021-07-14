# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:02:46 2021

@author: AKayal
"""
from functools import lru_cache
import math
import session10_Polygon
from session10_Polygon import *

def findout_max_efficiency(polygon_vertices = [10,50,30,40,20],
                           circumradius = 30):
    polygon_vertices = polygon_vertices
    circumradius = circumradius
    
    custom_polygon = Polygon(max(polygon_vertices),
                             circumradius)
    
    def return_max():
        max_efficiency_list =  [Polygon(x, circumradius).__getattribute__("max_efficiency")
                                for x in polygon_vertices
                                if x > 0 ]
        print(f"Max max_efficiency from Polygon vetrices :{polygon_vertices} \
              Efficiency List:{max_efficiency_list} \
                  is :{max(max_efficiency_list)}")
        return max(max_efficiency_list)
    return return_max

polygon_verticesx = 10
circumradiusx = 20


#return_list = findout_max_efficiency()
#return_list()
custom_polygon = Polygon(polygon_verticesx, circumradiusx)
custom_polygon.__getattribute__("perimeter")     
#print(f"custom: {custom_polygon.__getattribute__(perimeter)}")