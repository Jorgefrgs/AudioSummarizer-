from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import os
from dotenv import load_dotenv
import openai
import time
from openai.error import RateLimitError, OpenAIError

load_dotenv()

api_key = os.getenv('API_KEY')
if api_key is None:
    raise ValueError("API_KEY não está definida no arquivo .env")

openai.api_key = api_key

print("Insert the url")
url = input()

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Title: {yt.title}")

ys = yt.streams.get_audio_only()
audio_path = ys.download(mp3=True)

print(f"Audio file path: {audio_path}")

model = whisper.load_model("base")
result = model.transcribe(audio_path)

text_file_name = f"{yt.title}.txt"

with open(text_file_name, "w") as f:
    f.write(result["text"])

def get_response(message):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature=1,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0]['message']['content']


with open(text_file_name, 'r') as file:
    text = file.read()

instructions = "Analise o seguinte texto e forneça um resumo detalhado:"
prompt = f"{instructions}\n\n{text}"

response = get_response(prompt)

if response:
    print(response)
else:
    print("Não foi possível obter uma resposta.")
