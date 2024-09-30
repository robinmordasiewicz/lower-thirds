#!/bin/bash

# Image parameters
width=400
height=160
columns=11
rows=5
dot_size=4  # Size of each square (4x4 pixels)
dot_color="gray"
background="none"  # Transparent background

# Calculate spacing between dots, accounting for dot size
col_spacing=$(((width - dot_size) / (columns - 1)))
row_spacing=$(((height - dot_size) / (rows - 1)))

# Create a new transparent image
convert -size ${width}x${height} xc:$background png:grid.png

# Add the squares to the image
for row in $(seq 0 $((rows - 1))); do
  for col in $(seq 0 $((columns - 1))); do
    x=$((col * col_spacing))
    y=$((row * row_spacing))
    convert grid.png -fill $dot_color -draw "rectangle $x,$y $((x + dot_size)),$((y + dot_size))" grid.png
  done
done

