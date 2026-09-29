
from unittest import TestCase
from video import Video

class VideoTest(TestCase):
    def setUp(self):
       self.video = Video()
       
    def test_that_title_is_empty(self):
        self.assertTrue(self.video.get_title() =="")
        
    def test_that_minutes_duration_is_zreo(self):
        self.assertEqual(0,self.video.get_minutes_duration())
        
    def test_that_current_playback_is_zero(self):
        self.assertEqual(0,self.video.get_current_playback_position())
        
    def test_that_a_movie_is_playing(self):
        self.video.play()
        self.assertTrue(self.video.is_playing()) 
         
    def test_that_advance_minutes(self):
        self.video.play()
        self.video.advance(30.25)
        self.assertEqual( 30.25, self.video.get_current_playback_position())
        
    def test_that_a_movie_is_finished(self):
        self.video.play()
        self.video.is_finished()
        self.assertFalse(self.video.is_playing())
        
    def test_that_a_movie_restart(self):
        self.video.play()
        self.video.is_finished()
        self.video.restart()
        self.assertTrue(self.video.is_playing())
        
    def test_that_a_movie_restart(self):
        self.video.play()
        self.assertTrue(self.video.is_playing()) 
        self.video.set_minutes_duration(2.30)
        self.video.set_current_playback_position(1.30)
        self.assertAlmostEqual(1.00, self.video.time_remaining())



