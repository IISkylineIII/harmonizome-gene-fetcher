mport requests

# Define the base URL for the Harmonizome API
HARMONIZOME_BASE_URL = "https://amp.pharm.mssm.edu/Harmonizome/api/"

def read_from_url(url):
    try:
        # Send an HTTP GET request to the provided URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return it as a Python dictionary
            data = response.json()
            return data
        else:
            
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        
        print("An error occurred:", e)

def fetch_gene_by_name(gene_name):
   
    gene_url = f"{HARMONIZOME_BASE_URL}1.0/gene/{gene_name}"

    
    gene_data = read_from_url(gene_url)

    return gene_data


gene_name = 'nanog'
gene_data = fetch_gene_by_name(gene_name)
print(gene_data)
