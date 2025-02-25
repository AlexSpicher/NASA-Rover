import requests
from PIL import Image
from io import BytesIO

api_key = 'tdIKyXDUAEZaN4Ch8TmmI10RJBkRnG6OYpzsCbNg'
rover = 'curiosity'
sol = 1000
camera = 'fhaz'

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
params = {
    'sol' : sol,
    'camera': camera,
    'api_key': api_key
    }
response = requests.get(url, params=params)
data = response.json()

if data['photos']:
    photo_url = data['photos'][0]['img_src']
    response = requests.get(photo_url)
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print('No photos found with the given parameters')
