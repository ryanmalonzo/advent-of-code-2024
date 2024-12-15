#!/bin/zsh

if [ -z "$1" ]; then
  echo "Usage: $0 <day>."
  exit 1
fi

if [ -z "$SESSION_COOKIE" ]; then
  echo "Error: SESSION_COOKIE is not set."
  exit 1
fi

year=2024
day=$(printf "%02d" $1)  # Format day with leading zero if necessary
url="https://adventofcode.com/${year}/day/${day#0}/input"  # Remove leading zero in URL
output_dir="day_${day}"
output_file="${output_dir}/input.txt"
template_file="template.py"
target_file="${output_dir}/part_1.py"

mkdir "$output_dir"

curl -s --fail --cookie "session=$SESSION_COOKIE" "$url" -o "$output_file"

if [ $? -eq 0 ]; then
  echo "Input for day $day saved to $output_file."
else
  echo "Error: Failed to fetch input for day $day."
  rm -f "$output_file"
  exit 1
fi

if [ -f "$template_file" ]; then
  cp "$template_file" "$target_file"
  echo "Template copied to $target_file."
else
  echo "Warning: $template_file not found. Skipping template copy..."
fi

