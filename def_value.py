import pytesseract
from PIL import Image
import pdf2image
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os
from google.cloud import vision
import io
import def_checking_value

#according to position reference text - calculate postion of gloss value place written by hand
#define area to cut
def gloss_value(factor, single_pdf_1, x_reference_text, y_reference_text):
    start_x_gloss_area = x_reference_text - 615 + factor
    start_y_gloss_area = y_reference_text - 2432
    end_x_gloss_area = start_x_gloss_area + 135
    end_y_gloss_area = start_y_gloss_area + 110

    #cutting area for searching gloss value written by hand
    gloss_cropped_image = single_pdf_1.crop((start_x_gloss_area, start_y_gloss_area, end_x_gloss_area, end_y_gloss_area))
    
    #function which checking the value on the cropped image by Google Cloud Vision API
    gloss = def_checking_value.checking_value(gloss_cropped_image)
    #checking if gloss is numeric value
    try:
        #if value is numeric function return this value as string
        numeric_gloss = float(gloss)
        return gloss
    except:
        #if value is not numeric function return None
        return None

#according to position reference text - calculate postion of delta value place written by hand
#define area to cut
def delta_value(factor, single_pdf_1, x_reference_text, y_reference_text):
    start_x_delta_area = x_reference_text - 615 + factor
    start_y_delta_area = y_reference_text - 1830
    end_x_delta_area = start_x_delta_area + 135
    end_y_delta_area = start_y_delta_area + 110

    #cutting area for searching gloss value written by hand
    delta_cropped_image = single_pdf_1.crop((start_x_delta_area, start_y_delta_area, end_x_delta_area, end_y_delta_area))
    #function which checking the value on the cropped image by Google Cloud Vision API
    delta = def_checking_value.checking_value(delta_cropped_image)
    #checking if delta is numeric value
    try:
        numeric_delta = float(delta)
        #if value is numeric function return this value as string
        return delta
    except:
        #if value is not numeric function return None
        return None


#according to position reference text - calculate postion of psd 10 value place written by hand
#define area to cut
def psd10_value(factor, single_pdf_1, x_reference_text, y_reference_text):
    start_x_psd10_area = x_reference_text - 615 + factor
    start_y_psd10_area = y_reference_text - 1590
    end_x_psd10_area = start_x_psd10_area + 135
    end_y_psd10_area = start_y_psd10_area + 110

    #cutting area for searching gloss value written by hand
    psd10_cropped_image = single_pdf_1.crop((start_x_psd10_area, start_y_psd10_area, end_x_psd10_area, end_y_psd10_area))
    #function which checking the value on the cropped image by Google Cloud Vision API
    psd10 = def_checking_value.checking_value(psd10_cropped_image)
    #checking if psd10 is numeric value
    try:
        numeric_psd10 = float(psd10)
        #if value is numeric function return this value as string
        return psd10
    except:
        #if value is not numeric function return None
        return None
    
def psdx50_value(factor, single_pdf_1, x_reference_text, y_reference_text):
    start_x_psdx50_area = x_reference_text - 615 + factor
    start_y_psdx50_area = y_reference_text - 1590
    end_x_psdx50_area = start_x_psdx50_area + 135
    end_y_psdx50_area = start_y_psdx50_area + 110

    #cutting area for searching gloss value written by hand
    psdx50_cropped_image = single_pdf_1.crop((start_x_psdx50_area, start_y_psdx50_area, end_x_psdx50_area, end_y_psdx50_area))
    #function which checking the value on the cropped image by Google Cloud Vision API
    psdx50 = def_checking_value.checking_value(psdx50_cropped_image)
    #checking if psdx50 is numeric value
    try:
        numeric_psdx50 = float(psdx50)
        #if value is numeric function return this value as string
        return psdx50
    except:
        #if value is not numeric function return None
        return None

def fluidity_value(factor, single_pdf_1, x_reference_text, y_reference_text):
    start_x_fluidity_area = x_reference_text - 615 + factor
    start_y_fluidity_area = y_reference_text - 1590
    end_x_fluidity_area = start_x_fluidity_area + 135
    end_y_fluidity_area = start_y_fluidity_area + 110

    #cutting area for searching gloss value written by hand
    fluidity_cropped_image = single_pdf_1.crop((start_x_fluidity_area, start_y_fluidity_area, end_x_fluidity_area, end_y_fluidity_area))
    #function which checking the value on the cropped image by Google Cloud Vision API
    fluidity = def_checking_value.checking_value(fluidity_cropped_image)
    #checking if fluidity is numeric value
    try:
        numeric_fluidity = float(fluidity)
        #if value is numeric function return this value as string
        return fluidity
    except:
        #if value is not numeric function return None
        return None