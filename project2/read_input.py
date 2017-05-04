def read_google(filename):
    data = dict()


    with open(filename, "r") as fin:
        # What is this line doing? Reading the first line? 
        system_desc = next(fin)
        number_of_videos, number_of_endpoints, number_of_requests, number_of_caches, cache_size= system_desc.split(" ")
        number_of_videos = int(number_of_videos)
        number_of_endpoints = int(number_of_endpoints)
        number_of_requests = int(number_of_requests)
        number_of_caches = int(number_of_caches)
        cache_size = int(cache_size)        
        video_ed_request = dict()
        
        video_size_desc = next(fin).strip().split(" ") # Gives us the video sizes as strings
        for i in range(len(video_size_desc)):
            # Converts those sizes to ints
            video_size_desc[i] = int(video_size_desc[i])
            
        ed_cache_list = [] # storing a list of caches for each endpoint

        ### CACHE SECTION
        
        ep_to_dc_latency = []

        ep_to_cache_latency = [] 

        # ep_to_dc_latency = [] Doesn't need to be an array - just a single integer
        for i in range(number_of_endpoints):
            
            ep_to_dc_latency.append([]) # appending an empty list
                
            ep_to_cache_latency.append([]) # appending an empty list

            dc_latency, number_of_cache_conns = next(fin).strip().split(" ")
            dc_latency = int(dc_latency)
            number_of_cache_conns = int(number_of_cache_conns)

            ep_to_dc_latency[i] = dc_latency # dc latency for the first endpoint - goes into the first element of the array
            
            for j in range(number_of_caches): # for the number of caches that exist
                ep_to_cache_latency[i].append(0) #creating an array for the next ep in ep_to_cache_late
                
                
            cache_list = [] # List of caches
            for j in range(number_of_cache_conns):
                cache_id, latency = next(fin).strip().split(" ")
                cache_id = int(cache_id)
                cache_list.append(cache_id)
                latency = int(latency)
                ep_to_cache_latency[i][cache_id] = latency # i is the endpoint, cache_id is the cache_id - 0 to 100 
            ed_cache_list.append(cache_list)

        video_ids = []
        endpoint_ids = []
        
        for i in range(number_of_videos):
            video_ids.append(i)
        
        for i in range(number_of_endpoints):
            endpoint_ids.append(i)
        
        ### REQUEST SECTION
        for i in range(number_of_requests):
            video_id, ed_id, requests = next(fin).strip().split(" ")
            video_id = int(video_id)
            ed_id = int(ed_id)
            requests = int(requests)
            video_ed_request[(video_id,ed_id)] = requests
            
        # FOR MY CLASS SYSTEM I need video ids and endpoint ids to be more easily accessible that in a dictionary. 


    data["number_of_videos"] = number_of_videos
    data["number_of_endpoints"] = number_of_endpoints
    data["number_of_requests"] = number_of_requests
    data["number_of_caches"] = number_of_caches
    data["cache_size"] = cache_size
    data["video_size_desc"] = video_size_desc
    data["ep_to_dc_latency"] = ep_to_dc_latency
    data["ep_to_cache_latency"] = ep_to_cache_latency
    data["ed_cache_list"] = ed_cache_list
    data["video_ed_request"] = video_ed_request
    data["video_ids"] = video_ids
    data["endpoint_ids"] = endpoint_ids

    return data


"""
data = read_google("input/me_at_the_zoo.in")
print("number of request...", data["number_of_requests"])
sum = 0
for i in data["video_ed_request"]:
    sum += int(data["video_ed_request"][i])
print("number of individual requests=", sum, " which is different from the number of request descriptions ", data["number_of_requests"])

print("video sizes...", data["video_size_desc"])
print("Cache size...", data["cache_size"])
print("number of caches... ", data["number_of_caches"])
print("number of videos...", data["number_of_videos"])"""
