# Photo-Loc-exporter usage
# Within a given directory retrieves file name, photo date, lat, long, and img direction and writes data to a given csv file
#run from terminal one argument -d dirrectory this argument is a str and as such must be in ""
# code saves file in directory

#required packages
os
csv
exif import Image
argparse

#example
python PhotoLoc.py -d 'your directory path'
