"""Import data form pdf pdf file"""
import pytesseract
from PIL import Image
import pdf2image
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os
from google.cloud import vision
import io
import csv
import os
import def_checking_value
import def_value

#path to the pdf file
pdf_folder_path = ""
#open all pdf files in the folder
for filename in os.listdir(pdf_folder_path):
    if filename.endswith(".pdf"):
        pdf_filepath = os.path.join(pdf_folder_path, filename)
        #opening pdf file as image
        pdf_1 = pdf2image.convert_from_path(pdf_filepath, dpi=600)

        single_pdf_1 = pdf_1[0]

        #performs OCR on the image, returning a dictionary with text location information
        text_pdf_1 = pytesseract.image_to_data(single_pdf_1, lang="pol", output_type=pytesseract.Output.DICT)

        #variable for save paint number
        paint_number = ""
        #variable for save production order
        production_order = ""
        #variable for save production date
        production_date = ""
        #list for gloss values
        gloss_values = []
        #list for delta values
        delta_values = []
        #list for psd10 values
        psd10_values = []
        #list for psdx50 values
        psdx50_values = []
        #list for fluidity values
        fluidity_values = []
        #value of factor which moved the are to next collumn for searching values
        factor = 0

        #searching "Produktu:" and taking text after this text, this is paint number
        found_keyword = False
        for i, text in enumerate(text_pdf_1["text"]):
            if found_keyword and text.strip() != '':
                paint_number = text
                break
            if "Produktu:" in text:
                found_keyword = True

        #searching "produkcyjny:" and taking text after this text, this is number of production order
        found_keyword = False
        for i, text in enumerate(text_pdf_1["text"]):
            if found_keyword and text.strip() != '':
                production_order = text
                break
            if "produkcyjny:" in text:
                found_keyword = True

        #searching "zakończenia:" and taking text after this text, this is date of production
        found_keyword = False
        for i, text in enumerate(text_pdf_1["text"]):
            if found_keyword and text.strip() != '':
                production_date = text
                break
            if "zakończenia:" in text:
                found_keyword = True

        #searching refrerence text "Uwaga!" and save text position
        #all other positions of values will be search based on reference text position
        x_reference_text = 0
        y_reference_text = 0
        for i, text in enumerate(text_pdf_1["text"]):
            if "Uwaga!" in text:
                x_reference_text, y_reference_text = int(text_pdf_1['left'][i]), int(text_pdf_1['top'][i])
                break


        #while loop for saving data from pdf file
        start_loop = True
        while start_loop:
            gloss = def_value.gloss_value(factor, single_pdf_1, x_reference_text, y_reference_text)
            delta = def_value.delta_value(factor, single_pdf_1, x_reference_text, y_reference_text)
            psd10 = def_value.psd10_value(factor, single_pdf_1, x_reference_text, y_reference_text)
            psdx50 = def_value.psdx50_value(factor, single_pdf_1, x_reference_text, y_reference_text)
            fluidity = def_value.fluidity_value(factor, single_pdf_1, x_reference_text, y_reference_text)

            #checking if colums where should be values are empty, if yes stop the loop
            if gloss == None and delta == None and psd10 == None and psdx50 == None and fluidity == None:
                start_loop = False
            else:
                #adding gloss value to list with gloss values
                gloss_values.append(gloss)
                #adding delta value to list with delta values
                delta_values.append(delta)
                #adding psd10 value to list with psd10 values
                psd10_values.append(psd10)
                #adding psdx50 value to list with psdx50 values
                psdx50_values.append(psdx50)
                #adding fluidity value to list with fluidity values
                fluidity_values.append(fluidity)

                #changing factor to move position for column for searching values
                factor = factor + 140

        #save qc values to the csv file
        #create list of new data
        new_data = [paint_number, production_order, production_date, gloss_values, delta_values, psd10_values, psdx50_values, fluidity_values]
        #save parameters in csv file
        csv_filepath = "D:/analiza_qc/data.csv"
        with open(csv_filepath, mode="a", newline="") as qc_values:
            new_qc_values = csv.writer(qc_values, delimiter=";")
            new_qc_values.writerow(new_data)


        # print("\npaint number: ", paint_number)
        # print("\nproduction order: ", production_order)
        # print("\nproduction date: ", production_date)
        # print("\ngloss values: ", gloss_values)
        # print("\ndelta values: ", delta_values)
        # print("\npsd10 values: ", psd10_values)
        # print("\npsdx50 values: ", psdx50_values)
        # print("\nfluidity values: ", fluidity_values)
        # print("\nfactor value: ", factor)