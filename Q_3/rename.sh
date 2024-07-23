#!/bin/bash

# Check if both parameters are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 folder_path file_extension"
    exit 1
fi

# Assign parameters to variables
folder_path="$1"
file_extension="$2"

# Check if the provided folder path exists
if [ ! -d "$folder_path" ]; then
    echo "The folder path $folder_path does not exist."
    exit 1
fi

# Iterate over all files in the specified folder
for file in "$folder_path"/*; do
    if [ -f "$file" ]; then
        # Get the file name without the extension
        filename=$(basename -- "$file")
        extension="${filename##*.}"
        filename="${filename%.*}"

        # Rename the file by adding the specified extension
        new_filename="${filename}${file_extension}.${extension}"
        mv "$file" "${folder_path}/${new_filename}"
        echo "Renamed $file to ${folder_path}/${new_filename}"
    fi
done

