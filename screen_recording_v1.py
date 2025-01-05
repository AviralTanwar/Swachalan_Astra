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

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Functions       Functions       Functions       Functions       Functions       Functions       Functions       Functions       Functions       
# ----------------------------------------------------------------------------------------------------------------------------------------------

def check_folder():
    try:
        # Define the folder path
        # _______________________________________________________________________________________________________________________
        # | Make the folder path to Program files and then for other linux and everything according to that and then for MAC    |
        # _______________________________________________________________________________________________________________________
        folder_path =Path(r'C:\Users\Aviral Tanwar\Desktop\MAJOR_PROJECT_1\swachal astra recordings')    

        # Define the path for the "requirement.txt" file
        # _________________________________________________
        # | Make the txt file have the status as FALSE    |
        # _________________________________________________
        status_file = Path("requirements.txt")                                                             

        # Check if the status is already recorded in requirement.txt
        if status_file.exists():
            with status_file.open("r") as file:
                if "swachal_astra_recordings = True" in file.read():
                    print("Folder check already completed. Skipping...")
                    return

        # If not recorded, check and create the folder
        print("Checking if the folder exists, and if not, creating it...")
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Folder created at: {folder_path}")
        else:
            print(f"Folder already exists at: {folder_path}")

        # Write the status to the "requirement.txt" file
        with status_file.open("w") as file:
            file.write("swachal_astra_recordings = True")
            print(f"Status written to {status_file}")

    except Exception as e:
        print("Error occurred in the function check_folder: ", e)
        raise



def screen_record():
    try:
        check_folder()
        print("Recording started")
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


# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
