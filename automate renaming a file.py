import os

# Set the directory you want to rename files in
directory = '/Users/mrgab/OneDrive/Desktop/New folder'

# Set the prefix for the new filenames
prefix = 'new_filename_prefix_'

# Set the starting number for the new filenames
start_number = 1

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate over the files in the directory
for file in files:
  # Get the file's current filename
  old_filename = file
  # Construct the new filename
  new_filename = prefix + str(start_number)
  # Use the os.rename() function to rename the file
  os.rename(os.path.join(directory, old_filename), os.path.join(directory, new_filename))
  # Increment the start number for the next file
  start_number += 1
