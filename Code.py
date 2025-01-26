!pip install -q transformers

!pip install -q youtube_transcript_api

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi


youtube_video = "https://youtu.be/3Ao33js8LK8?si=peQx92CcXxtisjPG"

video_id = youtube_video.split("=")[1]

video_id

from IPython.display import YouTubeVideo
YouTubeVideo(video_id)

youtube_video = "https://youtu.be/GxWx22J0vZs?si=NIow4rk3hw11BP2o"
# Split on '?' to seperate video id from other parameters
video_id = youtube_video.split("?")[0].split("/")[-1]

!pip install youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi

# Attempt to fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Print the transcript
print(transcript)

transcript[0:5]


result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))

summarizer = pipeline('summarization')

num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("input text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  print("Summarized text\n"+out)
  summarized_text.append(out)

#print(summarized_text)

len(str(summarized_text))

str(summarized_text)
