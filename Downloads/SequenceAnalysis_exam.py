
import sys
import matplotlib.pyplot as plt
from collections import defaultdict

def count_subseq_in_sequences(subseq, fasta_file):
    counts = defaultdict(int)
    current_seq_id = None
    current_seq = ""
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if current_seq_id:
                    counts[current_seq_id] = current_seq.count(subseq)
                current_seq_id = line.strip()
                current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq_id:
            counts[current_seq_id] = current_seq.count(subseq)
    return counts

# Check if the correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: python3 virus_sequence_analyzer.py <nameofvirus> <subseq> <fastafile>")
    sys.exit(1)

# Read parameters from command line
nameofvirus = sys.argv[1]
subseq = sys.argv[2]
fasta_file = sys.argv[3]

# Count how many times the subseq appears in each sequence
subseq_counts = count_subseq_in_sequences(subseq, fasta_file)

# Prepare data for plotting
sequence_ids = list(subseq_counts.keys())
subseq_appearances = list(subseq_counts.values())

# Find the maximum count
max_count = max(subseq_appearances)
max_index = subseq_appearances.index(max_count)

# Plotting the histogram
fig, ax = plt.subplots(figsize=(12, 6))
bar_colors = ['b' if i != max_index else 'r' for i in range(len(subseq_appearances))]

ax.bar(sequence_ids, subseq_appearances, color=bar_colors)
ax.set_title(f'Subsequence Appearances in Each Sequence of {nameofvirus}')
ax.set_xlabel('Sequence ID')
ax.set_ylabel('Occurrences in Sequence')
ax.tick_params(axis='x', rotation=90)

# Save the figure to a file
output_file = f'{nameofvirus}_sequence_analysis_histogram.png'
plt.tight_layout()
plt.savefig(output_file)

print(f"Histogram saved to {output_file}")
