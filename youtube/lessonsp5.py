from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyC7i_TZapT8QeTwkp7DF5AMaXi1WH46LOo'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )

search_response = youtube.search().list(
  q='日本語',
  part='id,snippet',
).execute()

list = []
for sr in search_response.get("items", []):
  list.append(sr['snippet']['title'])
