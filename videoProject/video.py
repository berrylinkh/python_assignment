
class Video:
    def __init__(self):
        self.title =""
        self.minutes_duration =0
        self.current_playback_position =0
        self.playing = False
        
   
        
    def get_title(self):
        return self.title
        
    def get_minutes_duration(self):
        return self.minutes_duration
        
    def get_current_playback_position(self):
        return self.current_playback_position
        
    def set_title (self,title):
        self.title  = title
        
    def set_minutes_duration (self, duration_of_minutes):
        self.minutes_duration  =  duration_of_minutes
        
    def set_current_playback_position(self, playback_position):
        self.current_playback_position =  playback_position
        
    def play(self):
        self.playing = True
        
    def is_playing(self):
        return self.playing
    
    def advance(self, minutes):
        self.current_playback_position +=minutes
       
    def is_finished(self):
        self.playing = False
        
    def restart(self):
        self.playing = True
        
    def time_remaining(self):
        return self.minutes_duration - self.current_playback_position
        
 
