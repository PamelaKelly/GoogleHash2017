from project2 import read_input
from project2 import cache_system
from project2.cache_system import cache_server, video, endpoint, solution
from project2.main import *

data = read_input.read_google("../input/me_at_the_zoo.in")

vid_size_desc = data["video_size_desc"]
cache_capacity = data["cache_size"]
number_of_caches = data["number_of_caches"]

results = system_setup(data)     
video_objs, cache_objs, endpoint_objs, basic_matrix = results[0], results[1], results[2], results[3]
cache_manager_basic(video_objs, cache_objs, endpoint_objs, basic_matrix)
print(basic_matrix.get_solution())
print("-----------------------------------------------------------------")  
count_not_assigned = 0
for video in video_objs:
    if video.get_assigned_to_cache() == False:
        count_not_assigned += 1
        
print("-----------------------------------------------------------------")       
print("Number of videos not assigned to caches", count_not_assigned)
print("\nState of Caches: ")
for cache in cache_objs:
    print("Cache: ", cache.get_cache_id(), "\nCurrent Load: ", cache.get_current_load())
    
print("Looks good, not much redundant space")

size_total = 0
for size in vid_size_desc:
    size_total += size
print("-----------------------------------------------------------------")    
print("Total Accumulative Size of videos: ", size_total)
print("Total Accumulative Capacity of caches: ", number_of_caches * cache_capacity)
print("Therefore we can see that there is not enough space in the caches to store all videos")
print("-----------------------------------------------------------------")   
print("So! We have to come up with a way to prioritise")
