import PIL
from PIL import Image
import os
import sys

directory = '03_18-22_50_35'
out_directory = '03_18-22_50_35_CORRECT'
# Create the destination directory if it doesn't exist
if not os.path.exists(out_directory):
    os.makedirs(out_directory)

for file_name in os.listdir(directory):
    print("Processing %s" % file_name)
    image = Image.open(os.path.join(directory, file_name))

    x,y = image.size
    new_dimensions = (512, 384) #dimension set here
    output = image.resize(new_dimensions, PIL.Image.Resampling.LANCZOS)

    output_file_name = os.path.join(out_directory, file_name[:-4] + ".png")
    output.save(output_file_name, "PNG", quality = 95)

print("All done")