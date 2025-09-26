import ssl
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech4.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="nova",
  speed=0.8,
  input="... Get ready you filthy, fucking, degenerates... - On your mark - Get set -- Gameon!"
)

response.stream_to_file(speech_file_path)