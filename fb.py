import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

image_url = sys.argv[1] #we pass the url as an argument

cred = credentials.Certificate('path/to/certificate.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': '<mysuperstorage>.appspot.com'
})
bucket = storage.bucket()

image_data = requests.get(image_url).content
blob = bucket.blob('new_cool_image.jpg')
blob.upload_from_string(
        image_data,
        content_type='image/jpg'
    )
print(blob.public_url)