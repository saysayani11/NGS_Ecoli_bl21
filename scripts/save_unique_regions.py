import os
import pandas as pd
from Bio import SeqIO

def extract_specific_regions(genome_file, regions):
    """
    Extract specific regions from a genome file.
    """
    seq_record = SeqIO.read(genome_file, "fasta")
    sequences = []
    for start, end in regions:
        if start <= end:
            region_seq = seq_record.seq[start-1:end]
        else:  # Circular genome case
            region_seq = seq_record.seq[start-1:] + seq_record.seq[:end]
        sequences.append(region_seq)
    return sequences

def save_sequences_to_fasta(sequences, output_dir, genome_name):
    """
    Save sequences to separate FASTA files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i, seq in enumerate(sequences):
        output_file = os.path.join(output_dir, f"{genome_name}_unique_region_{i+1}.fasta")
        with open(output_file, "w") as f:
            f.write(f">{genome_name}_unique_region_{i+1}\n")
            f.write(str(seq) + "\n")

# Example usage
base_dir = '/home/sayantoni/Downloads/Ecoli_BL21/sequences/mauve-results-3'
genome_files = {
    'OSB-1': os.path.join(base_dir, 'OSB-1.fasta'),
    'OSB-2': os.path.join(base_dir, 'OSB-2.fasta'),
    'ecoli_bl21_full_genome': os.path.join(base_dir, 'ecoli_bl21_full_genome.fasta')
}
unique_regions = {
    'OSB-1': [(4529415, 4607825)],
    'OSB-2': [(4165079, 4178667), (4580219, 4669924)],
    'ecoli_bl21_full_genome': [(3724394, 3737981)]
}

output_dir = os.path.join(base_dir, 'unique_regions_sequences')

for genome, regions in unique_regions.items():
    genome_file = genome_files[genome]
    sequences = extract_specific_regions(genome_file, regions)
    save_sequences_to_fasta(sequences, output_dir, genome)

print(f"Sequences saved to {output_dir}")
