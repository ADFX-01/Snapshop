from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import os
import io

#find current directory
cwd = os.getcwd()
api_key = cwd + "\quikShop.json"
image = cwd + "\image1.jpg"

#set api_key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_key

global tags
tags = ''

def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision_v1

    client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    global tags

    for logo in logos:
        tags = tags + logo.description + ', ' 

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision_v1
    
    client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    global tags

    for label in labels:
        tags = tags + label.description + ', ' 

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision_v1
    
    
    client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Labels:')

    global tags

    for text in texts:
        tags = tags + text.description + ', ' 

detect_labels(image)
detect_logos(image)
detect_text(image)



print(tags)

file = open("tags.txt", "w+")
file. write(tags)
file.close()