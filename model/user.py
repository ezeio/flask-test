class User:
    
    
    def __init__(self, name):
        self.name = name
        
    def __init__(self, name, list_of_songs):
        self.name = name
        self.list_of_songs = list_of_songs
        
    def get_name(self):
        return self.name
    
    def get_list_of_songs(self):
        return self.list_of_songs
        