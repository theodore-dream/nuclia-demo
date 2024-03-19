from flask import Flask, request, jsonify
from flask_cors import CORS
from nucliadb_sdk import NucliaDB, Region  # Assuming this is the correct import for your SDK
from sentence_transformers import SentenceTransformer

import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

CORS(app)
sdk = NucliaDB(region=Region.ON_PREM, url="http://localhost:8080/api")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

slug="Nuclia_Information_1"

def get_nucliadb_kb(slug):
    try:
        # Attempt to retrieve the specific knowledge box by slug
        kb = sdk.get_knowledge_box(kbid='f73ad734de1d4bd3be3011f0b22dab90', slug=slug)
        # If the knowledge box with the given slug doesn't exist, create it
    except Exception as e:
        print(f"Error accessing NucliaDB: {e}")
        return None

@app.route('/')
def home():
    app.logger.debug("Serving the home page")
    return app.send_static_file('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Retrieve knowledge box by slug
    kb = sdk.get_resource_by_slug(kbid='5100e3cd-c5fa-4f1b-b7a2-a9ad03eed233', slug=slug)
    if not kb:
        return jsonify({"error": "Knowledge Box could not be accessed or created"}), 500

    # Get the search query from the request
    data = request.json
    query = data['query']
    query_vectors = encoder.encode([query])[0].tolist()

    # Perform the search
    results = sdk.search(kbid='5100e3cd-c5fa-4f1b-b7a2-a9ad03eed233', vector=query_vectors, vectorset="base", min_score=0.25)
    
    # Log the type of results for debugging purposes
    app.logger.debug(f"Search results type: {type(results)}")

    # Manual conversion of results to a JSON serializable format
    results_data = {'items': []}
    if hasattr(results, 'items'):
        for item in results.items:
            # Assuming 'item' can be converted to a dictionary or has attributes that you want to include
            # You may need to adjust the following line to match the actual structure of your items
            results_data['items'].append(item.to_dict() if hasattr(item, 'to_dict') else item.__dict__)

    return jsonify(results_data)

if __name__ == "__main__":
    app.run(debug=True)

#nucliadb_sdk.v2.exceptions.NotFoundError: Resource not found at url http://localhost:8080/api/v1/kb/fbbcca549e8d4acfbceaea573aae907a/resource/Nuclia_Information_1: {"detail":"Resource does not exist"}
    
