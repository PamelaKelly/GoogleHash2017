from project2 import read_input
from project2 import cache_system
from project2.cache_system import cache_server, video, endpoint, solution_matrix


class cache_manager:     
    
    def __init__(self, data):
        number_of_caches = data["number_of_caches"]
        number_of_videos = data["number_of_videos"]
        number_of_endpoints = data["number_of_endpoints"]
        cache_capacity = data["cache_size"]
        requests = data["video_ed_request"]
        vid_size_desc = data["video_size_desc"]
        ep_to_dc_latency = data["ep_to_dc_latency"]
        ep_to_cache_latency = data["ep_to_cache_latency"]
        video_ids = data["video_ids"]
        endpoint_ids = data["endpoint_ids"]
    
        self.__cache_objs = []
        self.__video_objs = []
        self.__endpoint_objs = []
        
        for i in range(number_of_caches):
            cache = cache_server(i, cache_capacity)
            self.__cache_objs.append(cache)
        
        for i in range(number_of_videos):
            video_id = video_ids[i]
            video_inst = video(video_id, vid_size_desc[i])
            self.__video_objs.append(video_inst)
            
        for i in range(number_of_endpoints):
            ep = endpoint(endpoint_ids[i], ep_to_dc_latency[i], ep_to_cache_latency[i])
            self.__endpoint_objs.append(ep)
            for j in range(len(video_ids)):
                if (endpoint_ids[i], video_ids[j]) in requests.keys():
                    ep.add_video_request(video_ids[j], requests[(endpoint_ids[i], video_ids[j])])
        
        self.__basic_matrix = solution_matrix(number_of_caches, number_of_videos) # just if you want a visual representation
        self.__total_number_requests = data["number_of_requests"]

    def cache_manager_basic(self):
        for video in self.__video_objs:
            for cache in self.__cache_objs:
                if video.get_assigned_to_cache() == False:
                    if cache.is_feasible(video) == False:
                        continue
                    else:
                        cache.add_video(video)
                        self.__basic_matrix.add_video_to_cache(video, cache)
                    
        #return self.__basic_matrix
    
    def get_video_objs(self):
        return self.__video_objs
    
    def get_cache_objs(self):
        return self.__cache_objs
    
    def get_endpoint_objs(self):
        return self.__endpoint_objs
    
    def get_total_number_requests(self):
        return self.__total_number_requests
    
    def get_matrix(self):
        return self.__basic_matrix