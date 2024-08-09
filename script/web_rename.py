import os

# Path to the directory containing the files
directory = r'D:\Utkarsh\Web Devlopment'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an MP4 file
    if filename.endswith(".mp4"):
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        
        # Split the name into parts separated by parentheses
        parts = name.split("(")
        
        # Extract the number from the last part
        number_part = parts[-1]
        
        # If the last part contains a number
        if number_part.isdigit():
            # Remove the number part from the name
            name = name.replace("(" + number_part, "")
            
            # Rename the file with the number at the front
            new_filename = f"{number_part}{name}{extension}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")
