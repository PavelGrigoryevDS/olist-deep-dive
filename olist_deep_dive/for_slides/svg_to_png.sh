#!/bin/bash

# Navigate to script's directory
cd "$(dirname "$0")"

# Create png directory if it doesn't exist
mkdir -p png

# Get SVG files from svg directory sorted by modification time (oldest first)
readarray -t sorted_files < <(ls -tr svg/*.svg)

# Convert files in modification order
for svg_file in "${sorted_files[@]}"; do
    if [ -f "$svg_file" ]; then
        base_name=$(basename "$svg_file")
        png_file="png/${base_name%.svg}.png"
        echo "Converting $svg_file to $png_file..."
        inkscape "$svg_file" --export-filename="$png_file" --export-dpi=600 --export-width=1600 --export-background=white
    fi
done

echo "Done! SVG files converted in modification-time order."
