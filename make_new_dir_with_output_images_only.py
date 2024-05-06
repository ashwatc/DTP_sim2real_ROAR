import os
import shutil
import cv2
import tqdm

def copy_png_files(source_folder, destination_folder, iteration_to_copy = 750, video_with_triple_frame=True):

    # Create the destination folders if they don't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    combined_sim2real_frame_destination_subfolder = os.path.join(destination_folder, "0_sim2real_combined_frames")
    if not os.path.exists(combined_sim2real_frame_destination_subfolder):
        os.makedirs(combined_sim2real_frame_destination_subfolder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        # print(source_folder)

        if os.path.isdir(os.path.join(source_folder, filename)):
            sim_img_filename = source_folder.split("/")[-1]
            # print(filename)
            # print(sim_img_filename, "\n")

            # iterate over subfolders inside current directory (all output directories covering all iterations)
            next_folder_inside = os.path.join(source_folder, filename)
            for subfolder in os.listdir(next_folder_inside):

                if not subfolder.lower().endswith(".png"): # --> this means it is one of the sub-directories that represents each checkpointed/saved iteration from the model
                    folder_iteration = subfolder.split("_")[1].split("iter")[1]
                    if int(folder_iteration) == int(iteration_to_copy - 1): # find the folder which matches the iteration we want to save
                        final_folder = os.path.join(next_folder_inside, subfolder)
                        return_filename_value = None

                        for img in os.listdir(final_folder):
                            
                            if img == "result.png": # copy the file to the destination folder
                                # copy the file to the destination folder
                                # sim_img_filename += ".png"
                                source_path = os.path.join(final_folder, "result.png")
                                shutil.copy2(source_path, os.path.join(destination_folder, sim_img_filename))
                                # print(f"Copied {sim_img_filename} to {destination_folder}\n")
                                if not video_with_triple_frame: return_filename_value = source_path

                            if "result_bundle.png" in img: # copy the result bundle (triple-image) to the destination folder
                                # copy the file to the destination folder
                                sim_img_filename += ".png"
                                source_path = os.path.join(final_folder, img)
                                shutil.copy2(source_path, os.path.join(destination_folder, combined_sim2real_frame_destination_subfolder))
                                # print(f"Copied {sim_img_filename} to {destination_folder}\n")
                                if video_with_triple_frame: return_filename_value = source_path
                        
                        return return_filename_value
                                

            # print(os.path.join(source_folder, filename))
            # return os.path.join(source_folder, filename)
        # else:
        #     return os.path.join(source_folder, filename)
    

def images_to_video(image_filenames, output_file, fps=24):

    # Sort the image files to maintain order
    image_files = sorted(image_filenames, key=lambda filename: int(filename.split("/")[-1].split("_")[1]))

    # Get the first image to get dimensions
    first_image = cv2.imread(image_files[0])
    height, width, layers = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for AVI format
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Iterate through each image and write to the video
    for image_file in tqdm.tqdm(image_files):
        image_path = image_file
        frame = cv2.imread(image_path)
        video.write(frame)

    # Release the VideoWriter object
    video.release()

    print(f"Video saved to: {output_file}")


ITERATION_TO_COPY = 400
ROOT_DIR = "/home/ashwatc/Desktop/sim2real/DTP_sim2real_ROAR/results/03_18-22_50_35_OUTPUTS"
OUTPUT_DIR = "/home/ashwatc/Desktop/sim2real/DATA_INPUTS_FOR_YOLO/" + ROOT_DIR.split("/")[-1] + "_ITER_" + str(ITERATION_TO_COPY) + "_YOLO_INPUTS"

images_array = []
count = 0
print("\nSaving Images Progress:")
for folder in tqdm.tqdm(os.listdir(ROOT_DIR)):
    folder = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(folder):
        count += 1
        output_filename = copy_png_files(folder, OUTPUT_DIR, ITERATION_TO_COPY)
        if output_filename:
            images_array.append(output_filename)

# print(images_array)
print("\nCreating Video Progress:")
images_to_video(images_array, os.path.join(OUTPUT_DIR, "video.mp4"))

print()













      # if copy_triple_frame:
        #     '''copying over the sim/real/sim2real triple-frame images only'''
        #     if filename.lower().endswith(".png"): # is PNG file
        #         sim_img_filename = ("_").join((filename.split("_"))[:5])
        #         sim_img_filename = sim_img_filename.split(".png")[0]
        #         # print(sim_img_filename)

        #         # Create the source and destination paths
        #         source_path = os.path.join(source_folder, filename)

        #         # print(source_path, destination_folder)

        #         # Copy the file to the destination folder
        #         shutil.copy2(source_path, destination_folder)
        #         print(f"Copied {filename} to {destination_folder}")

        # else: 
        #     '''copying over the result.png sim2real-converted images only'''
        #     if os.path.isdir(os.path.join(source_folder, filename)): # is directory
        #         sim_img_filename = source_folder.split("/")[-1]
        #         print(sim_img_filename)

        #         next_folder_inside = os.path.join(source_folder, filename)
        #         for subfolder in os.listdir(next_folder_inside):

        #             if subfolder.lower().endswith(".png"):
        #                 # Create the source and destination paths
        #                 source_path = os.path.join(source_folder, filename)

        #                 # Copy the file to the destination folder
        #                 shutil.copy2(source_path, destination_folder)
        #                 print(f"Copied {filename} to {destination_folder}")

        #             else:
        #                 folder_iteration = subfolder.split("_")[1].split("iter")[1]
        #                 if int(folder_iteration) == int(iteration_to_copy - 1):
        #                     final_folder = os.path.join(next_folder_inside, subfolder)
        #                     for img in os.listdir(final_folder):
        #                         if img == "result.png":
        #                             # Copy the file to the destination folder
        #                             shutil.copy2(os.path.join(final_folder, img), destination_folder)
        #                             print(f"Copied {filename} to {destination_folder}")
                    
