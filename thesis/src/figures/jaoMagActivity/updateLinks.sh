#!/bin/bash

# Directory containing the symbolic links
# Replace with your directory path
link_dir="."

# Check if the directory exists
if [ ! -d "$link_dir" ]; then
    echo "Directory does not exist: $link_dir"
    exit 1
fi

# Find all symbolic links in the directory and replace them with actual files
find "$link_dir" -type l -print0 | while IFS= read -r -d '' link; do
    # Resolve the symbolic link
    real_file=$(readlink "$link")

    # Check if the file exists
    if [ ! -f "$real_file" ]; then
        echo "Error: Target file does not exist for $link"
        continue
    fi

    # Replace the symbolic link with the actual file
    cp --remove-destination "$real_file" "$link"
done

echo "All symbolic links in $link_dir have been updated to actual files."

