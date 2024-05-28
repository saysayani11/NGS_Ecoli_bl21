import json
import pandas as pd
import re

# Define paths to the files
alignment_file_path = "/home/sayantoni/Downloads/Ecoli_BL21/sequences/mauve-results-3/mauve_results_files/test3.alignment"
jsonl_file_path = "/home/sayantoni/Downloads/ncbi_dataset/ncbi_dataset/data/data_report.jsonl"
output_file_path = "mapped_genes.csv"

# Function to read and parse the alignment file
def parse_alignment_file(file_path):
    blocks = []
    current_block = None
    block_pattern = re.compile(r'^> (\d+):(\d+)-(\d+) ([+-]) (.+)$')
    
    with open(file_path, "r") as file:
        for line in file:
            match = block_pattern.match(line)
            if match:
                if current_block:
                    blocks.append(current_block)
                current_block = {
                    'Sequence_Num': int(match.group(1)),
                    'Start': int(match.group(2)),
                    'End': int(match.group(3)),
                    'Strand': match.group(4),
                    'Path': match.group(5).split('/')[-1].split('.')[0],  # Normalize the path to match seqname
                    'Sequence': ''
                }
            elif current_block:
                current_block['Sequence'] += line.strip()
    
    if current_block:
        blocks.append(current_block)
    
    return blocks

# Function to parse the JSONL file and extract gene coordinates
def parse_jsonl(file_path):
    genes = []
    with open(file_path, "r") as file:
        for line in file:
            gene_data = json.loads(line)
            for region in gene_data['genomicRegions']:
                gene_info = {
                    'seqname': region['geneRange']['accessionVersion'].split('.')[0],  # Normalize seqname
                    'start': int(region['geneRange']['range'][0]['begin']),
                    'end': int(region['geneRange']['range'][0]['end']),
                    'strand': region['geneRange']['range'][0]['orientation'],
                    'symbol': gene_data.get('symbol'),
                    'name': gene_data.get('name')
                }
                genes.append(gene_info)
    return genes

# Function to map alignment blocks to genes
def map_blocks_to_genes(blocks, genes_df):
    mapped_genes = []
    for block in blocks:
        block_genes = genes_df[ 
                               (genes_df['start'] <= block['End']) & 
                               (genes_df['end'] >= block['Start'])]
        block_genes = block_genes[['seqname', 'start', 'end', 'strand', 'symbol', 'name']]
        mapped_genes.append({
            'block': block,
            'genes': block_genes
        })
    return mapped_genes

# Parse the alignment file
alignment_blocks = parse_alignment_file(alignment_file_path)
print(f"Parsed {len(alignment_blocks)} alignment blocks")

# Parse the JSONL file
genes_data = parse_jsonl(jsonl_file_path)
print(f"Parsed {len(genes_data)} genes")

# Convert genes data to a DataFrame
genes_df = pd.DataFrame(genes_data)
print(f"Genes DataFrame:\n{genes_df.head()}")

# Map alignment blocks to genes
mapped_genes = map_blocks_to_genes(alignment_blocks, genes_df)
print(f"Mapped {len(mapped_genes)} blocks to genes")

# Save the results to a CSV file
mapped_genes_list = []
for item in mapped_genes:
    block = item['block']
    for _, gene in item['genes'].iterrows():
        mapped_genes_list.append({
            'Sequence_Num': block['Sequence_Num'],
            'Block_Start': block['Start'],
            'Block_End': block['End'],
            'Block_Strand': block['Strand'],
            'Block_Path': block['Path'],
            'Gene_Seqname': gene['seqname'],
            'Gene_Start': gene['start'],
            'Gene_End': gene['end'],
            'Gene_Strand': gene['strand'],
            'Gene_Symbol': gene['symbol'],
            'Gene_Name': gene['name']
        })

mapped_genes_df = pd.DataFrame(mapped_genes_list)
print(f"Mapped Genes DataFrame:\n{mapped_genes_df.head()}")
mapped_genes_df.to_csv(output_file_path, index=False)

print(f"Results saved to {output_file_path}")


# Group by sequence and identify unique genes
unique_genes = mapped_genes_df.groupby('Gene_Seqname')['Gene_Symbol'].apply(lambda x: x.unique()).reset_index()

# Save the unique genes for each sequence
unique_genes_output_file_path = "unique_genes_per_sequence.csv"
unique_genes.to_csv(unique_genes_output_file_path, index=False)

print(f"Unique genes for each sequence saved to {unique_genes_output_file_path}")
