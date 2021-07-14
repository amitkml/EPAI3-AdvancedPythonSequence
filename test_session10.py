# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:11:54 2021

@author: AKayal
"""
import session10
import session10_CustomPolygonSeq
from session10 import *
from session10_CustomPolygonSeq import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

def test_readme_exists():
    assert os.path.isfile("README.md"), "SESSION10_README.md file missing!"
    
def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your SESSION10_README.md file interesting! Add atleast 100 words"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        #print(f"Name:{function}")
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        

def validate_polygon_class():
    
    """
    This function will have test case to validate polygon class

    Returns
    -------
    assert error or success.

    """
    polygon_vertices = 10
    circumradius = 20
    polygon_vertices_big = 15
    
    custom_polygon = Polygon(polygon_vertices,
                             circumradius)

    custom_polygon_2nd = Polygon(polygon_vertices,
                             circumradius)
    
    custom_polygon_big = Polygon(polygon_vertices_big,
                             circumradius)
    
    assert len(custom_polygon.__repr__()) > 0  ## test case to validate it returns proper value
    assert (custom_polygon.perimeter > 0)
    assert (custom_polygon.circumradius > 0)
    assert (custom_polygon.interiorAngle > 0)
    assert (custom_polygon.edgeLength > 0)
    assert (custom_polygon.apothem > 0)
    assert (custom_polygon.area > 0)
    assert (custom_polygon.perimeter > 0)
    assert (custom_polygon.max_efficiency > 0)
    assert (custom_polygon_big > custom_polygon)
    assert (custom_polygon == custom_polygon_2nd)


def validate_polygon_seq():
    
    """
    This function will have test case to validate polygon class

    Returns
    -------
    assert error or success.

    """
    polygon_vertices = [10,50,30,40,20]
    polygon_vertices_25 = [k for k in range(1,26)]
    circumradius = 30
    polygonsequencecustom = PolygonSequence()
    polygon_vertices_25Custom = PolygonSequence(polygon_vertices_25,
                                                circumradius)
    
    assert (polygonsequencecustom.callc_max_effcncy() == 50)
    assert (polygon_vertices_25Custom.callc_max_effcncy() == 25)
    assert (polygon_vertices_25Custom.__len__() == 25)
    assert len(polygon_vertices_25Custom.__repr__()) > 0  ## test case to validate it returns proper value
    assert (polygonsequencecustom[3] == 40)


    #print(polygon_vertices_25Custom.__getitem__("max_efficiency_list"))

validate_polygon_class()

validate_polygon_seq()

