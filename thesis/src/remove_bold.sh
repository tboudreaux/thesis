#!/bin/bash

# Function to process a single file
process_file() {
    local file="$1"
    local temp_file="$(mktemp)"

    # Ensure temporary file removal on script exit
    trap "rm -f $temp_file" EXIT

    # Process each line that matches the patterns
    while IFS= read -r line; do
        # Extract matching text without the bold formatting
        local clean_line=$(echo "$line" | sed -E 's/\\textbf\{([^}]*)\}|\{\\bf ([^}]*)\}/\1\2/g')

        echo "Found: $line"
        echo "Without bold: $clean_line"
        read -p "Remove bold formatting? [Y/n]: " choice
        choice=${choice:-Y} # Default choice is Y

        if [[ $choice =~ ^[Yy] ]]; then
            # Replace the original line with the clean line in the file
            sed -i "s|${line}|${clean_line}|g" "$file"
        fi
    done < <(grep -E '\\textbf\{[^}]*\}|\{\\bf [^}]*\}' "$file")

    # Cleanup
    rm -f "$temp_file"
}

export -f process_file

# Find all .tex files and process them
find . -type f -name "*.tex" -exec bash -c 'process_file "$0"' {} \;

