from project2 import read_input
from project2 import cache_system
from project2.cache_system import cache_server, video, endpoint
from project2.main import cache_manager
from project2.fitness_function import *
import copy 

data = read_input.read_google("input/test.in")

current_cache_manager = cache_manager(data)
current_cache_manager.cache_manager_basic()

def create_all_neighbours(data, current_cache_manager):
    current_fitness = fitness_test(current_cache_manager)
    cache_objs = current_cache_manager.get_cache_objs()
    for cache in cache_objs: # for each cache
        videos_stored_here = cache.get_videos()
        for video in videos_stored_here: # signifies every instance where a change can be made
            neighbour_object = cache_manager(data)
            neighbour = neighbour_object.cache_manager_basic()
            # make one change to make it a 'neighbour' solution
            n_cache_objs = neighbour.get_cache_objs()
            if video.get_assigned_to_cache() == True: # can only unassign videos because caches are almost full 
                cache_id = cache.get_cache_id()
                n_cache = n_cache_objs[cache_id] # need to update the change in the neighbour cache manager not current cache manager
                n_cache.remove_video(video)
                neighbour_fitness = fitness_test(neighbour)
                if neighbour_fitness > current_fitness:
                    current_cache_manager = neighbour
            else:
                continue # onto the next video
            
    return current_cache_manager


    
