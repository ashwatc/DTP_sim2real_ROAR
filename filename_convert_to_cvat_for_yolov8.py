import os
import shutil

def copy_and_rename_files(source_dir, destination_dir):

    # Get a list of files in the source directory, sorted alphabeticaslly
    # files = sorted(os.listdir(source_dir), key = lambda fname: int(fname.split("_")[0]))
    files = sorted(os.listdir(source_dir), key = lambda fname: int(fname.split("_")[1]))

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate over each file and copy/rename it
    for i, file_name in enumerate(files):
        if not file_name.endswith(".jpg") and not file_name.endswith(".png"): continue

        img_num = int(file_name.split("_")[1])
        source_path = os.path.join(source_dir, file_name)
        destination_path = os.path.join(destination_dir, f'frame_{img_num:08d}.png')

        # Copy and rename the file
        shutil.copy2(source_path, destination_path)
        print(f'Copied and renamed: {file_name} -> {destination_path}')


source_directory = '03_18-22_50_35_OUTPUTS_ITER_800_YOLO_INPUTS'
destination_directory = os.path.join(source_directory, source_directory + "_CVAT_filenames")

copy_and_rename_files(source_directory, destination_directory)
