from PIL import Image
import pdf2image
import logging
import os
from google.cloud import vision
import io

#function which checking the value on the cropped image by Google Cloud Vision API
def checking_value(cropped_image_for_api):
    #create new buffer in memory by io.BytesIO()
    buffer = io.BytesIO()
    #saving cropped_image_for_api which is PIL.Image.Image to buffor in JPEG format
    #and convert for bytes stream
    cropped_image_for_api.save(buffer, format='JPEG')
    #set a pointer in the buffer to the beginning of the stream
    buffer.seek(0)
    #read bytes from buffer and create Image obiect
    image_for_api_google = vision.Image(content=buffer.read())

    #sett the GOOGLE_APPLICATION_CREDENTIALS environment variable
    #to the path of the json file with Google Cloud authorization keys
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

    #configures the logging module to log all DEBUG level messages.
    #This is useful for tracking application performance and diagnosing problems.
    logging.basicConfig(level=logging.DEBUG)

    #create a new instance of ImageAnnotatorClient from the google.cloud.vision package.
    #This client is used to query the Google Cloud Vision API.
    client = vision.ImageAnnotatorClient()

    #use the ImageAnnotatorClient to query the Google Cloud Vision API to detect text in an image.
    #the image_for_api_google object contains the image data to be analyzed.
    response = client.text_detection(image=image_for_api_google)

    #get the text detection results from the API response and saves them to the texts variable.
    #text_annotations contains a list of all text fragments detected in the image.
    texts = response.text_annotations

    #saving value from text.description to gloss value
    for text in texts[1:2]:
        return text.description

    #reset buffer for saving next image
    buffer.seek(0)
    buffer.truncate()