'''
TPRG 2131 Fall 2024 Assignment 1, Test file template.
Sept, 2024
Chamath Kulathilaka 100889193


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

import pytest
from A_V_calc import (cylinder_cal, circle_cal, sphere_cal, cuboid_cal, prism_cal, decision)

# Test the cylinder volume calculation
def test_cylinder_cal():
    assert cylinder_cal(10, 5) == 785.4  # π * 5^2 * 10
    assert cylinder_cal(7, 2.5) == 137.44  # π * 2.5^2 * 7

# Test the circle area calculation
def test_circle_cal():
    assert circle_cal(5) == 78.54  # π * 5^2
    assert circle_cal(2.5) == 19.63  # π * 2.5^2

# Test the sphere volume calculation
def test_sphere_cal():
    assert sphere_cal(3) == 113.1  # (4/3) * π * 3^3
    assert sphere_cal(1.5) == 14.14  # (4/3) * π * 1.5^3

# Test the cuboid area calculation
def test_cuboid_cal():
    assert cuboid_cal(2, 3, 4) == 52  # 2 * (2*3 + 2*4 + 3*4)
    assert cuboid_cal(5, 5, 5) == 150  # 2 * (5*5 + 5*5 + 5*5)

# Test the prism volume calculation
def test_prism_cal():
    assert prism_cal(3, 4, 5) == 30.0  # ((1/2) * 3 * 4) * 5
    assert prism_cal(6, 7, 8) == 168.0  # ((1/2) * 6 * 7) * 8

# Test the decision function for different views
#def test_decision():
#    equation = "π * 5^2 * 10"
#    result = 785.4
 #   assert decision(equation, result, 'D') == f"Equation: {equation}\nAnswer: {result}\n"
 #   assert decision(equation, result, 'V') == f"Answer: {result}\n"
