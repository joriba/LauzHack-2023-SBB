from dotenv import load_dotenv
import os
import requests
from journey_maps_tiles_client.client import RemoteCaller

load_dotenv()
JMT_URL=os.getenv("JMT_URL")
JMT_API_KEY=os.getenv("JMT_API_KEY")
if JMT_URL[-1] == '/':
    JMT_URL = JMT_URL[:-1]

sess = requests.Session()
sess.params = {"api_key": JMT_API_KEY}

caller = RemoteCaller(JMT_URL, session=sess)

# print(caller.get_styles()) # DOES NOT WORK

