#Install and import dependencies

!pip install --upgrade "ibm-watson>=5.2.0"

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup Speech to Text Service

apikey = 'AK-snL3zE7FCx8UigfLlKoYlgKcY3D4T_z5lsQACFqTG'
url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/391812f4-3d1c-4b31-9736-2320b561817b'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

#Perform conversion

file = '/Users/sabolaji/Downloads/yyyy.flac'
with open(file, 'rb') as f:
    rss = stt.recognize(audio=f, content_type='audio/flac', model='en-US_NarrowbandModel', continuous=True).get_result()

text = rss['results'][0]['alternatives'][0]['transcript']

with open('outputfile.txt', 'w') as out:
    out.writelines(text)
    