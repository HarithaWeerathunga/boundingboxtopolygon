import os 
import shutil
import glob 
import pickle
import json
import numpy as np
import cv2 

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

dirname = r"/Users/harithaweerathunga/Desktop/......."
destination_folder_name = r"/Users/harithaweerathunga/Desktop....../Results"


def fast_scandir(dirname):
    print("Initial Directory Scan")
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    return subfolders

def folder_scan(subfolder_directory):
    print("Subdirectory Scan")
    for dirname in list(subfolder_directory):
        print(dirname)
        dir_list = os.listdir(dirname)
        if 'annotations' in dir_list:
            json_file = open(dirname + "/annotations/instances_default.json")
            json_data = json.load(json_file)
            json_reader(json_data, dirname)
            
            

def json_reader(json_data, dir_name):
    print("Reading JSON File.....")
    for i in json_data["images"]:
        image_id = i["id"]
        image_path = i["file_name"]
        for j in json_data["annotations"]:
            if j["image_id"] == image_id:
                image_segmentation = j["segmentation"]
                category_id = j["category_id"]
        for k in json_data["categories"]:
            if k["id"] == category_id:
                barcode = k["name"]
        draw_polygon(image_id, image_path, image_segmentation, dir_name, barcode)

        
def draw_polygon(image_id, image_path, image_segmentation, dir_name, barcode):
    print("Drawing Polygons.......")
    print(image_id)
    print(barcode)

    full_image_path = dir_name + "/images/" + image_path
    img = cv2.imread(full_image_path)
    height = img.shape[0]
    width = img.shape[1]

    subList = [image_segmentation[0][n:n+2] for n in range(0, len(image_segmentation[0]), 2)]
    print(subList)
    

    mask = np.zeros((height, width), dtype=np.uint8)
    points = np.array(subList)
    points = np.int32([points])
    cv2.fillPoly(mask, points, (255))
    res = cv2.bitwise_and(img,img,mask = mask)

    rect = cv2.boundingRect(points)
    cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
    # cv2.imshow("cropped" , cropped )
    # cv2.waitKey(0)
    save_with_barcode(barcode, cropped, image_id)
    print("********************")


def save_with_barcode(barcode, cropped_image, image_id):
    if not os.path.exists(f'{destination_folder_name}'):
        os.makedirs(f'{destination_folder_name}')
    if not os.path.exists(f'{destination_folder_name}/{barcode}'):
        os.makedirs(f'{destination_folder_name}/{barcode}')
    print("Image Saving..............")
    cv2.imwrite(os.path.join(f'{destination_folder_name}/{barcode}', f'{image_id}.jpg'), cropped_image)


folders = fast_scandir(dirname)
folder_scan(folders)



