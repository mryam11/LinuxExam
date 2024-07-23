#!/bin/bash

# Check if all three parameters are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 virus nukloids db"
    exit 1
fi

# Assign parameters to variables
virus="$1"
nukloids="$2"
db="$3"

# Run the Python script with the parameters
python3 SequenceAnalysis.py "$virus" "$nukloids" "$db"

