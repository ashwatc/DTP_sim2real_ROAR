import os
import shutil

def copy_png_files(source_folder, destination_folder, iteration_to_copy = 750):

    # Create the destination folders if they don't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    combined_sim2real_frame_destination_subfolder = os.path.join(destination_folder, "0_sim2real_combined_frames")
    if not os.path.exists(combined_sim2real_frame_destination_subfolder):
        os.makedirs(combined_sim2real_frame_destination_subfolder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):

        if os.path.isdir(os.path.join(source_folder, filename)):
                sim_img_filename = source_folder.split("/")[-1]
                # print(sim_img_filename)

                # iterate over subfolders inside current directory (all output directories covering all iterations)
                next_folder_inside = os.path.join(source_folder, filename)
                for subfolder in os.listdir(next_folder_inside):

                    if subfolder.lower().endswith(".png"): # --> this means it is the final combined triple-frame output of the largest iteration (NOTE: DOES NOT CHANGE BASED ON 'ITERATION_TO_COPY' INPUT VALUE!!)
                        # copy the file to the destination folder
                        source_path = os.path.join(next_folder_inside, subfolder)
                        shutil.copy2(source_path, combined_sim2real_frame_destination_subfolder)
                        print(f"Copied {subfolder} to {combined_sim2real_frame_destination_subfolder}\n")

                    else: # --> this means it is one of the sub-directories that represents each checkpointed/saved iteration from the model
                        folder_iteration = subfolder.split("_")[1].split("iter")[1]
                        if int(folder_iteration) == int(iteration_to_copy - 1): # find the folder which matches the iteration we want to save
                            final_folder = os.path.join(next_folder_inside, subfolder)
                            for img in os.listdir(final_folder):
                                if img == "result.png": # copy the file to the destination folder
                                    # copy the file to the destination folder
                                    sim_img_filename += ".png"
                                    source_path = os.path.join(final_folder, "result.png")
                                    shutil.copy2(source_path, os.path.join(destination_folder, sim_img_filename))
                                    print(f"Copied {sim_img_filename} to {destination_folder}\n")



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
                    


ITERATION_TO_COPY = 750
ROOT_DIR = "/home/ashwatc/Desktop/sim2real/Deep_Translation_Prior/results/results_2_19_24_full_sim_run_CSW_04"
OUTPUT_DIR = "/home/ashwatc/Desktop/sim2real/DATA_INPUTS_FOR_YOLO/" + ROOT_DIR.split("/")[-1] + "_YOLO_INPUTS"
for folder in os.listdir(ROOT_DIR):
    folder = os.path.join(ROOT_DIR, folder)
    if os.path.isdir(folder):
        copy_png_files(folder, OUTPUT_DIR, ITERATION_TO_COPY)
