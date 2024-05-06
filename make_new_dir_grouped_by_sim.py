import os
import shutil

def copy_png_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is a PNG file
        if filename.lower().endswith(".png"):
            sim_img_filename = ("_").join((filename.split("_"))[5:-2])
            sim_img_filename = sim_img_filename.split(".png")[0]
            print(sim_img_filename)
            
            # Create the destination folder if it doesn't exist
            output_dir = os.path.join(destination_folder, sim_img_filename)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Create the source and destination paths
            source_path = os.path.join(source_folder, filename)
            destination_path = output_dir

            # print(source_path, destination_path)

            # Copy the file to the destination folder
            shutil.copy2(source_path, destination_path)
            print(f"Copied {filename} to {destination_folder}")



ROOT_DIR = "/home/ashwatc/Desktop/sim2real/DTP_sim2real_ROAR/results/for_the_paper_results/CSW_08_results"
OUTPUT_DIR = "/home/ashwatc/Desktop/sim2real/DTP_sim2real_ROAR/results_by_sim_img/for_the_paper/" + ROOT_DIR.split("/")[-1] + "_simdir"
for folder in os.listdir(ROOT_DIR):
    folder = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(folder):
        copy_png_files(folder, OUTPUT_DIR)
