import sys
import os
import numpy as np
from PIL import Image
import pandas as pd

finger_positions = [
    {
        "x1": 0,
        "y1": 0,
        "x2": 128,
        "y2": 24
    },
    {
        "x1": 0,
        "y1": 48,
        "x2": 128,
        "y2": 72
    },
    {
        "x1": 0,
        "y1": 80,
        "x2": 128,
        "y2": 104
    },
    {
        "x1": 0,
        "y1": 120,
        "x2": 128,
        "y2": 144
    },
    {
        "x1": 200,
        "y1": 128,
        "x2": 232,
        "y2": 256
    }
]

def checkPressure(finger_region):
    try:
        threshold = 130
        pressure = 0
        for arr in finger_region:
            if pressure == 1:
                break
            else:
                pressure = 1 if np.max(arr) > threshold else 0
        return pressure
    except Exception as e:
        return f"An error occurred: {e}"

def sliceImage(image_path):
    try:
        img = Image.open(image_path) 
        img = img.convert('RGB')        
        img_np = np.array(img)
        height, width, _ = img_np.shape
        pressure_data = img_np[:, width//2:]
        pressure_data_gs_arr = np.dot(pressure_data[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
        pressure_data_gs_img = Image.fromarray(pressure_data_gs_arr)

        return pressure_data_gs_img
    except Exception as e:
        return f"An error occured: {e}"

def sliceFingers(image_path):
    try:
        sliced_image = sliceImage(image_path)
        img_np = np.array(sliced_image)
        data = []
        
        for pos in finger_positions:
            x1, y1, x2, y2 = pos["x1"], pos["y1"], pos["x2"], pos["y2"]
            finger_region = img_np[y1:y2, x1:x2] 
            pressure = checkPressure(finger_region)
            data.append(pressure)
        return data
    except Exception as e:
        return f"An error occured: {e}"
    
def processImagesInFolder(folder_path):
    try:
        results = []
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            pressures = sliceFingers(image_path)
            results.append({'image': filename, 'finger 1': pressures[0], 'finger 2': pressures[1], 'finger 3': pressures[2], 'finger 4': pressures[3], 'finger 5': pressures[4]})
        df = pd.DataFrame(results)

        df.to_excel('C://Users/fdt/OneDrive/Desktop/JoVision AI/results.xlsx')
        print("excel sheet made")
    except Exception as e:
        return f"An error occurred: {e}"
    
if len(sys.argv) != 2:
    print("Usage: python text_extraction.py <image_path>")
else:
    image_folder = sys.argv[1]
    print(processImagesInFolder(image_folder))