""" Test Class for Fitness Function"""

import unittest
from project2.fitness_function import fitness_test

from project2 import read_input
from project2 import cache_system
from project2.cache_system import cache_server, video, endpoint
from project2.main import cache_manager

data = read_input.read_google("../input/test.in")
   
cache_manager_object = cache_manager(data)
cache_manager_object.cache_manager_basic()

fitness_check = fitness_test(cache_manager_object)

if fitness_check.check_overflow() == 0:
    print("Check Overflow Test Passed")
else:
    print("Check Overflow Test Failed")
    
print("score...", fitness_check.calculate_score())

  

        
        
    
    