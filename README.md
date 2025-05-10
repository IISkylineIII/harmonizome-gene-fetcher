# Harmonizome Gene Data Fetcher

This Python script allows users to query gene-related data from the [Harmonizome API](https://maayanlab.cloud/Harmonizome/) — a collection of processed datasets about genes and proteins.

The script fetches data for a given gene name and prints the associated information returned from Harmonizome.

### API Used

- **Harmonizome API**: Developed by the Ma'ayan Lab, it provides gene and protein functional association data aggregated from multiple resources.

### Features

- Sends HTTP requests to the Harmonizome REST API.
- Retrieves gene data in JSON format.
- Handles HTTP errors gracefully.

### How It Works

The script contains two main functions:

- `read_from_url(url)`: Makes a GET request and returns parsed JSON data.
- `fetch_gene_by_name(gene_name)`: Constructs the appropriate URL using the gene name and calls `read_from_url`.

### Example Input

```python
gene_name = 'nanog'
gene_data = fetch_gene_by_name(gene_name)
print(gene_data)
