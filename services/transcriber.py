import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

#the url parser
def get_youtube_id(url):
    try:
        parsed_url = urlparse(url) #this handles all the standard urls, shortened ones, allat

        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        # this handles all the different formats
        if parsed_url.hostname in ('www.youtube.com', 'youtube.com', 'm.youtube.com'):
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query).get('v', [None])[0]        
            if parsed_url.path.startswith(('/embed/', '/v/', '/shorts/')):
                return parsed_url.path.split('/')[2] 
    except Exception as e:
        print(f"Error parsing the youtube url : {e}")
        return None

ytt_api = YouTubeTranscriptApi()

class Transcriber():
    def __init__(self, video_id):
        self.video_id = video_id
    #this gets the transcript. you can add a language parameter asw to select the language, but i'll work on that later 
    def get_transcript(self):
        transcript = ytt_api.fetch(self.video_id)
        return transcript
    #prints the whole transript 
    def disp_transcript(self):
        for snippet in self.get_transcript():
            print(snippet.text)


