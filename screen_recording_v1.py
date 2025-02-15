# .\astra_venv\Scripts\activate 

# Screen recording using OPENCV (GFG) 
# Needs to have following changes:-
#  1) In a new folder it needs to be created. If the folder doesn't exist, it will be created
#  2) Each recording needs to be new. WIth name recording_{count}.s_astra. 
#  3) In the final code, it will be in the folder -> program_files (windows) or in LINUX (wherever application files are)
#  4)Screen recording will start after the chrome is opened and a countdown will start

# ----------------------------------------------------------------------------------------------------------------------------------------------
# IMPORTING PACKAGES       IMPORTING PACKAGES       IMPORTING PACKAGES       IMPORTING PACKAGES       IMPORTING PACKAGES       IMPORTING PACKAGES       
# ----------------------------------------------------------------------------------------------------------------------------------------------
 
import pyautogui
import cv2
import numpy as np


from pathlib import Path
import os
import re

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Functions       Functions       Functions       Functions       Functions       Functions       Functions       Functions       Functions       
# ----------------------------------------------------------------------------------------------------------------------------------------------

def check_folder(folder_path):

    """
    This function checks if the specified folder exists and if not, creates it.
    It also writes the status of the folder check to a "requirements.txt" file.

    Args:
    folder_path (Path): The path to the folder to be checked and created.

    Returns:
    None: This function does not return any value. It only performs the folder check and creation operation.

    Raises:
    Exception: If an error occurs during the folder check or creation process.
    """
    try:
        # Define the path for the "requirements.txt" file
        # _________________________________________________
        # | Make the txt file have the status as FALSE    |
        # _________________________________________________
        status_file = Path("requirements.txt")

        # Check if the status is already TRUE in requirement.txt

        if status_file.exists():

            with status_file.open("r") as file:

                if "swachal_astra_recordings = True" in file.read():
                    print("Folder check already completed. Skipping...")
                    return

        # If FALSE, checks and creates the folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists at: {folder_path}")

        # Write the status to the "requirements.txt" file
        with status_file.open("w") as file:
            file.write("swachal_astra_recordings = True")

    except Exception as e:
        print("Error occurred in the function check_folder: ", e)
        raise

def file_check(folder_path):
    """
    This function checks if the specified folder exists and creates it if not.
    It then scans the folder for existing files with the naming pattern 
    'Swachal_Astra_Recording_<number>.mp4'. The function determines the next 
    available filename by incrementing the highest existing number.

    Args:
    folder_path (str): The path to the folder where the recordings are stored.

    Returns:
    str: The next available filename in the format 'Swachal_Astra_Recording_<number>.mp4',
         ensuring filenames are sequential.

    Raises:
    Exception: If an error occurs during the folder check or filename generation process.
    """
    try:
        check_folder(folder_path)                                                # Ensure the folder exists
        
        # List all files matching the pattern 'Swachal_Astra_Recording_<number>.mp4'
        existing_files = [f for f in os.listdir(folder_path) if re.match(r'Swachal_Astra_Recording_\d+\.mp4', f)]
        
        if not existing_files:
            return os.path.join(folder_path, "Swachal_Astra_Recording_1.mp4")
        

        numbers = [int(re.search(r'\d+', f).group()) for f in existing_files]    # Extract numbers from existing file names
        next_number = max(numbers) + 1

        return os.path.join(folder_path, f"Swachal_Astra_Recording_{next_number}.mp4")

    except Exception as e:
        print("Error occurred in the function file_check: ", e)
        raise

def screen_record():
    try:

        folder_path =Path(r'C:\Users\Aviral Tanwar\Desktop\MAJOR_PROJECT_1\Swachalan Astra\swachal astra recordings')

        check_folder(folder_path)
        
        resolution = (1920, 1080)                                            # Specify resolution & video codec
        codec = cv2.VideoWriter_fourcc(*"mp4v")                              # Use H.264 codec for MP4 (works better with modern players)

        filename = file_check(folder_path)                                   # Get unique filename

        fps = 30.0                                                           # Set frame rate & Keeping 30 FPS for better compatibility
        out = cv2.VideoWriter(filename, codec, fps, resolution)              # Create a VideoWriter object

        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)                           # Create an empty window
        cv2.resizeWindow("Live", 480, 270)

        while True:
            
            img = pyautogui.screenshot()                                     # Take screenshot using PyAutoGUI     

            frame = np.array(img)                                            # Convert the screenshot to a numpy array
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                   # Convert it from BGR to RGB

            out.write(frame)                                                 # Write frame to the output file
            
            cv2.imshow('Live', frame)                                        # Display the recording screen (optional)
            

        # Press q on the video recorder to stop the recording.
        # __________________________________________________________
        # | Change it to when chrome is closed or                   |
        # | something like this or when the quit option is choosen  |
        # __________________________________________________________            
            if cv2.waitKey(1) == ord('q'):                                   # Stop recording when 'q' is pressed
                break

        out.release()                                                       # Release resources
        cv2.destroyAllWindows()

        print(f"Recording stopped and saved as {filename}")

    except Exception as e:
        print("Error occurred in the function screen_record :- ", e)
        raise



# ----------------------------------------------------------------------------------------------------------------------------------------------
# MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       MAIN_CODE       
# ----------------------------------------------------------------------------------------------------------------------------------------------
 
def main():
    print("Iniating main code")

    screen_record()
    return "Swachalan Astra"


if __name__ == "__main__":
    main()
    exit()


# FLOW OF THIS PAGE
# main -> screen_record
#         screen_record  -> check_folder 
#         screen_record  -> file_check
# END FLOW OF THIS PAGE