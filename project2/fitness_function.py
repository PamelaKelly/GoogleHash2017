
class fitness_test():
    
    def __init__(self, cache_manager):
        self.__cache_objs = cache_manager.get_cache_objs()
        self.__endpoint_objs = cache_manager.get_endpoint_objs()
        self.__video_objs = cache_manager.get_video_objs()
        self.__total_num_requests = cache_manager.get_total_number_requests()
    
    def check_overflow(self):
        for cache in self.__cache_objs:
            if cache.get_current_load() > cache.get_max_cap():
                return -1
        return 0
    
    def calculate_cost_dc(self, ep):
        """ Cost for a particular video to a particular endpoint from the data centre"""
        return ep.get_latdc()
    
    def calculate_cost_cache(self, cache, ep):
        """ Cost for a particular video to a particular endpoint from a particular cache"""
        cache_conns = ep.get_cache_conns()
        cache_id = cache.get_cache_id()
        return cache_conns[cache_id]
        
    def gain(self, ep, cost_dc, cost_cache, num_reqs):
        difference = cost_dc - cost_cache
        return (difference * num_reqs)
        
    def calculate_score(self):
        cost_to_dc = 0
        cost_of_solution = 0
        gain = 0
        # calculate total cost to dc for all requests
        for ep in self.__endpoint_objs:
            requests = ep.get_video_requests()
            for vid_id in range(len(requests)):
                if vid_id in requests.keys():
                    temp_cost_dc = self.calculate_cost_dc(ep)
                    cost_to_dc += temp_cost_dc
                    video = self.__video_objs[vid_id]
                    if video.get_assigned_to_cache() == True:
                        cache_id = video.get_cache()
                        temp_cost_cache = (self.calculate_cost_cache(self.__cache_objs[cache_id], ep))
                        cost_of_solution += temp_cost_cache
                        num_requests = requests[vid_id]
                        temp_gain = self.gain(ep, temp_cost_dc, temp_cost_cache, num_requests)
                        if temp_gain < 0:
                            temp_gain = 0
                        gain += temp_gain
                    else:
                        cost_of_solution += self.calculate_cost_dc(ep)
                        
        score = gain / self.__total_num_requests
        return score            
    

                
            
                    
    