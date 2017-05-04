import numpy as np

class video:
    """
    # If requests is more than just a number we will need to add an array
    # Data field to hold additional information - for the moment requests 
    # Is represented by an integer"""
    
    def __init__(self, vid_id, size):
        self.__size = size
        self.__video_id = vid_id
        self.__assigned_to_cache = False
        self.__cache = None
        # Need to figure out how to handle the relationship between ep and video / requests
    
    def get_video_id(self):
        return self.__video_id
        
    def get_size(self):
        return self.__size
    
    def get_num_requests(self):
        return self.__num_requests
    
    def get_assigned_to_cache(self):
        return self.__assigned_to_cache
    
    def set_assigned_to_cache(self, state):
        self.__assigned_to_cache = state
        
    def set_cache(self, cache_id):
        self.__cache = cache_id
        
    def get_cache(self):
        return self.__cache
    
    def add_request(self):
        self.__num_requests += 1
        
    def __str__(self):
        return "Video Size: " + str(self.__size)
        
        
class cache_server:
    
    def __init__(self, cache_id, capacity):
        self.__cache_id = cache_id
        self.__MAX_CAPACITY = capacity
        self.__current_load = 0
        self.__videos = dict() # dict - key is the video id
    
    def get_cache_id(self):
        return self.__cache_id
    
    def get_max_cap(self):
        return self.__MAX_CAPACITY
    
    def get_current_load(self):
        return self.__current_load
    
    def get_videos(self):
        return self.__videos
    
    def is_feasible(self, video):
        if self.__current_load + video.get_size() < self.__MAX_CAPACITY:
            return True
        else:
            return False
        
    def add_video(self, video):
        self.__current_load += video.get_size()
        video.set_assigned_to_cache(True)
        video.set_cache(self.get_cache_id())
        self.__videos[video.get_video_id()] = video
        
    def remove_video(self, video):
        self.__current_load -= video.get_size()
        video.set_assigned_to_cache(False)
        video.set_cache(None)
        self.__videos[video.get_video_id()] = video
        
    def __str__(self):
        return "Cache Id: " + str(self.__cache_id) + "\nCache Size: " + str(self.__MAX_CAPACITY) + "\nCurrent Load: " + str(self.__current_load)
        
class endpoint:
    
    def __init__(self, ep_id, lat_dc, cache_conns):
        """
        # cache_conns contains a list of lines which include the id of each cahce
        # and the latency from the ep to that cache server in milliseconds
        """
        self.__ep_id = ep_id
        self.__lat_dc = lat_dc
        self.__cache_conns = cache_conns
        self.__video_requests = dict()
        
    def __str__(self):
        return "Latency to Data Centre: " + str(self.__lat_dc) + "\nCache Connections: " + str(self.__cache_conns) + "\nVideo Requests: " + str(self.__video_requests)

    def get_latdc(self):
        return self.__lat_dc
    
    def get_cache_conns(self):
        return self.__cache_conns
    
    def add_video_request(self, video_id, num_requests):
        self.__video_requests[video_id] = num_requests
    
    def get_video_requests(self):
        return self.__video_requests
        
class solution_matrix:
    """ Can you have multiple constructors in python the way you can in java?
    Or a default value for num_caches and num_videos? """
    
    def __init__(self, num_caches, num_videos):
        """construct a two dimensional array to represent the solution"""
        cache_assignments = [[0] * num_videos for i in range(num_caches)]
        self.__matrix = np.array(cache_assignments)
    
    def get_solution(self):
        return self.__matrix
    
    def set_solution(self, matrix):
        self.__matrix = matrix
    
    def add_video_to_cache(self, video, cache_server):
        #cache_server.add_video(video)
        """Need to check that this video isn't already located in this cache"""
        self.__matrix[cache_server.get_cache_id()][video.get_video_id()] = 1
        
    def __str__(self):
        return self.__matrix
        
        
        
