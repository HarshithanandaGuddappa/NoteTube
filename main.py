from services.transcriber import Transcriber
from services.transcriber import get_youtube_id

url_input = input("Enter your video URL:")
video_id = get_youtube_id(url_input)

bhideo = Transcriber(video_id)
bhideo.get_transcript()
bhideo.disp_transcript()