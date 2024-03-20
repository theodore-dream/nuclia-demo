import os
import base64
from nucliadb_sdk import NucliaDB, Region
from sentence_transformers import SentenceTransformer

API_KEY="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzEwODExNjQ5LCJzdWIiOiI1N2Y1ZGM0NS1jYmE1LTQ0ODgtOTU1MS01ZjlmOGM1Y2ExOGQiLCJqdGkiOiI0ZmVjYTc0YS0yYzY3LTRkYmMtOTMwNy0wMGQxMDA4OWNjYjgiLCJleHAiOjE3NDIzNDc2NDgsImtleSI6IjY3OTI1YzBjLTk3YzItNDIwZC04ZGJiLTk4YmRmMDhlMDcwMCIsImtpZCI6IjgyOWE4NGQ4LWQ1NDUtNGNjZS05ODJjLWFmMTI1ZGYyMTU0ZCJ9.kKGNd0he1quk5EAgCth3MPICxfl-4aWzWOAUGKTccx7KcT4TFjIo-4D0Jsej4uCHNEI8PNXiFkSIm6TOwnGExioHm1pukaIa2nE0qTXx4TSV0IQ7hC6aeZ6_x6BEvEkD3YnuMUi4sKgOqoNwhjRuQjiairC7VfozFgUlHI91HACOlxNgjgOYiiqM786osfDS0LBud5ZhdZYEPmPW7HsBwYnPYVie99ccoWUlFHc3uNxGkTNXsgLT_A_Zj-nsPqEvkyvUZ0pB-TV3_ZoLOiS_o6fQ7Mz9wgxI2--qzJj_ZXZcCu9to95-70dVbN31gYAWn7VANX26kkcwEQvJOnyn0at0OzdKoIHalcttdAHzBJtaNpHrF-dz_et_VxgH7WXomUcy84ozm5UoHph55iJ1qeH3_GI19IT8UnN4HSGhmWTcplyzL5Il0olrx31dQqgI2X_JOOwP5T7JCNFjVl9MXd8GiUD1jodKF2Z9O6gDqpOPPXEgISlXvF_GTAvP_m3ZJsb4WuJAdioP-t8QS8BFYwjunxLBoLN-JWKMF6MQUgOaUwUYQtEB56K9M7cWkhzuX_sz266dKxjk39alppgBt_XFLQN5B-L4aSMF_kaPTD82eukt9sQ70TAKytbE4B8xOKIhsj3kQyO8eZI8Z9iGyKjk_A1uZ3vZjQ9mjStIS18"

# Initialize SDK and Encoder
sdk = NucliaDB(region=Region.ON_PREM, url="http://0.0.0.0:8080/api")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

# Create a new Knowledge Box named "Nuclia_Information" here
kb = sdk.create_knowledge_box(slug="nuclia_info")

# Function to encode files to base64
def encode_file(file_path):
    with open(file_path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

# Upload PDF files to the Knowledge Box
pdf_directory = '/Users/rhyman/Coding/nuclia-demo/pdf_folder_nuclia'
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)
    encoded_pdf = encode_file(pdf_path)
    sdk.create_resource(
        kbid=kb.uuid,
        texts={"text": {"body": f"Content of {pdf_file}"}},
        slug=pdf_file.replace('.pdf', ''),
        files={
            "file": {
                "file": {
                    "filename": pdf_file,
                    "payload": encoded_pdf,
                }
            }
        }
    )

# Example search
query = "what are the risks and challenges that Nuclia may face in regards to management of Enterprise clients"
query_vectors = encoder.encode([query])[0].tolist()
results = sdk.search(kbid=kb.uuid, vector=query_vectors, vectorset="base", min_score=0.25)

# Print the search results
print("Search results for query:", query)
print(results)
