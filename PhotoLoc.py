#!/usr/bin/python3

import os
import csv
from exif import Image
import argparse

### Add argument parser ###
parser = argparse.ArgumentParser(description='collect GPS data from jpg files')
parser.add_argument('-d', '--directory', metavar="<directory>", type=str, required=True,
                    help='directory of jpg images')
args = parser.parse_args()
dir_path = args.directory


#write heads for csv file
header = ['filename','Date','lat','long','dir']
with open(dir_path + 'photoindex.csv', 'w',newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header)

#define functions
def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):
    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                                     img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                                     img.gps_longitude_ref))
            output = [x, img.datetime_original, coords[0], coords[1], img.gps_img_direction]
            print(x)
            with open('S:\\CLIENTS\\FDACS\\065 Adams Osceola ESA BDR\\Photos\\photoindex.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(output)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')

#loop through files and get information
files_in_dir = os.listdir(dir_path)
for x in files_in_dir:
    image_path = x
    image_coordinates(dir_path + x)


