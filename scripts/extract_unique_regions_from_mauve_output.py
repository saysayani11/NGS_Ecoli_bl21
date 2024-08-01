import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from Bio import SeqIO

def read_backbone(file_path):
    """
    Read the backbone file and return a dictionary of conserved regions.
    """
    conserved_regions = {'OSB-1': [], 'OSB-2': [], 'ecoli_bl21_full_genome': []}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            conserved_regions['OSB-1'].append((abs(int(parts[0])), abs(int(parts[1]))))
            conserved_regions['OSB-2'].append((abs(int(parts[2])), abs(int(parts[3]))))
            conserved_regions['ecoli_bl21_full_genome'].append((abs(int(parts[4])), abs(int(parts[5]))))
    return conserved_regions

def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    """
    if not intervals:
        return []
    # Sort intervals based on the start position
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:  # Overlapping or contiguous intervals
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

def find_gaps(merged_intervals, genome_length):
    """
    Find gaps between merged intervals, which represent unique regions.
    """
    unique_regions = []
    current_end = 0
    for start, end in merged_intervals:
        if start > current_end + 1:
            unique_regions.append((current_end + 1, start - 1))
        current_end = end
    if current_end < genome_length:
        unique_regions.append((current_end + 1, genome_length))
    return unique_regions

def analyze_genomes(conserved_regions, genome_lengths):
    """
    Analyze each genome to find unique regions.
    """
    unique_regions = {}
    for genome, intervals in conserved_regions.items():
        merged = merge_intervals(intervals)
        gaps = find_gaps(merged, genome_lengths[genome])
        unique_regions[genome] = gaps
    return unique_regions

def plot_genome(unique_regions, genome_lengths, reference_length):
    """
    Plot the genomes highlighting the unique regions.
    """
    fig, ax = plt.subplots(figsize=(20, 10), dpi=300)

    y_pos = {
        'ecoli_bl21_full_genome': 0,
        'OSB-1': 1,
        'OSB-2': 2
    }
    colors = {
        'ecoli_bl21_full_genome': 'blue',
        'OSB-1': 'green',
        'OSB-2': 'red'
    }

    # Plot the reference genome
    ax.add_patch(patches.Rectangle((0, y_pos['ecoli_bl21_full_genome'] - 0.2), reference_length, 0.4, edgecolor='black', facecolor='lightblue', label='Reference Genome'))

    # Plot the unique regions and annotate them
    for genome, regions in unique_regions.items():
        for start, end in regions:
            width = 0.4
            label = f'{genome} Unique Region'
            if start > end:
                rect1 = patches.Rectangle((start, y_pos[genome] - width/2), reference_length - start, width, edgecolor='none', facecolor=colors[genome], alpha=0.6, label=label)
                rect2 = patches.Rectangle((0, y_pos[genome] - width/2), end, width, edgecolor='none', facecolor=colors[genome], alpha=0.6)
                ax.add_patch(rect1)
                ax.add_patch(rect2)
                ax.annotate(f'{start}-{reference_length}', (start, y_pos[genome]), xytext=(3, 3), textcoords='offset points', fontsize=6, color=colors[genome])
                ax.annotate(f'1-{end}', (0, y_pos[genome]), xytext=(3, 3), textcoords='offset points', fontsize=6, color=colors[genome])
            else:
                rect = patches.Rectangle((start, y_pos[genome] - width/2), end - start, width, edgecolor='none', facecolor=colors[genome], alpha=0.6, label=label)
                ax.add_patch(rect)
                ax.annotate(f'{start}-{end}', (start, y_pos[genome]), xytext=(3, 3), textcoords='offset points', fontsize=6, color=colors[genome])

    # Labels and formatting
    ax.set_yticks([y_pos['ecoli_bl21_full_genome'], y_pos['OSB-1'], y_pos['OSB-2']])
    ax.set_yticklabels(['E. coli BL21', 'OSB-1', 'OSB-2'])
    ax.set_xlim(0, reference_length)
    ax.set_xlabel('Genome position (bp)')
    ax.set_title('Unique Regions in Genomes')

    # Remove duplicate labels in the legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    plt.tight_layout()
    plt.show()

def create_summary_df(unique_regions):
    """
    Create a dataframe summarizing the unique regions.
    """
    data = []
    for genome, regions in unique_regions.items():
        for start, end in regions:
            data.append([genome, start, end, end - start + 1])
    df = pd.DataFrame(data, columns=['Genome', 'Start (bp)', 'End (bp)', 'Length (bp)'])
    return df

def extract_sequences(unique_regions, genome_files):
    """
    Extract sequences for the unique regions from the genome files.
    """
    sequences = {}
    for genome, regions in unique_regions.items():
        genome_file = genome_files[genome]
        seq_record = SeqIO.read(genome_file, "fasta")
        seq_dict = seq_record.seq
        sequences[genome] = []
        for start, end in regions:
            if start <= end:
                region_seq = seq_dict[start-1:end]
            else:  # Circular genome case
                region_seq = seq_dict[start-1:] + seq_dict[:end]
            sequences[genome].append(str(region_seq))
    return sequences

# Example usage
base_dir = '/home/sayantoni/Downloads/Ecoli_BL21/sequences/mauve-results-3'
backbone_file = os.path.join(base_dir, 'test3.backbone')
genome_lengths = {'OSB-1': 4607825, 'OSB-2': 4669924, 'ecoli_bl21_full_genome': 4529413}
genome_files = {
    'OSB-1': os.path.join(base_dir, 'OSB-1.fasta'),
    'OSB-2': os.path.join(base_dir, 'OSB-2.fasta'),
    'ecoli_bl21_full_genome': os.path.join(base_dir, 'ecoli_bl21_full_genome.fasta')
}

# Read the backbone file to get conserved regions
conserved_regions = read_backbone(backbone_file)

# Analyze the genomes to find unique regions
unique_regions = analyze_genomes(conserved_regions, genome_lengths)

# Plot the genomes
plot_genome(unique_regions, genome_lengths, genome_lengths['ecoli_bl21_full_genome'])

# Create and display a summary dataframe of unique regions
summary_df = create_summary_df(unique_regions)
print(summary_df)

# Save the summary dataframe to a CSV file
summary_df.to_csv(os.path.join(base_dir, 'unique_regions_summary.csv'), index=False)

# Extract sequences for the unique regions
unique_sequences = extract_sequences(unique_regions, genome_files)

# Display unique sequences for verification
for genome, seqs in unique_sequences.items():
    print(f"\nUnique sequences in {genome}:")
    for i, seq in enumerate(seqs):
        print(f"Region {i+1}: {seq[:50]}...{seq[-50:]}")  # Displaying first and last 50 bp for brevity
