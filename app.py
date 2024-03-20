from flask import Flask, request, jsonify
from flask_cors import CORS
from nucliadb_sdk import NucliaDB, Region  # Assuming this is the correct import for your SDK
from sentence_transformers import SentenceTransformer

import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

CORS(app)
sdk = NucliaDB(region=Region.ON_PREM, url="http://localhost:8080/api", api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im51YSJ9.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzEwODk2NDQ0LCJzdWIiOiJiZWE2NWIyZC04NzA2LTQ2MzItYmVmYi03NDc2MDAwMjI1MWEiLCJqdGkiOiI3M2I5ZmJhOC0yMTQwLTRlMTAtODUxOS1iZjliODdhNDk5MTQiLCJleHAiOjI1MzM3MDc2NDgwMCwia2V5IjoiMTVkZWM2ZTgtMjlkNC00OTdhLWE1MDItMGJmOWFjNjc4MjFjIiwiYWxsb3dfa2JfbWFuYWdlbWVudCI6ZmFsc2V9.cPKOpyblK1zVdt5Ati19tJYU93HevVnzqXTI2vK_yaw4GxacbBmIGRmNZd88OJLWFbHpfL1NKwG5AyT2ugZkHRKuSOpge5nopoqre8yyAZtJnPVGEg4BvViOTX-PpLsXeaHhbfs_WcjNpIQEAXWiAzwo_PzcK4Rh9J5UZTmRFxQlzGfHXcH6XEYrmZy-ic69rbmVmqmh-dmGW2jvNdD6wy5GA81-XL96vtgH1AYzgW05iwaFE_FYWuzCJlOIgycxZBe80KJLEdE-CXlpW6d4TQmsAfayj9G-6t9B_vzNIC8TBVstwq6UHB5PSXYo1xxSuEVouUn399MSuMADTkwWhdEujn6x8mC484cqCDFnxgfEEoe9aeEYIUL-bBIilQz2mpQgQVHgx0hPpTbspc0mlKfWOzxj1JSKs8n649NWwccmym8vwriDvZTfONNjJq3MFG9G26clY6utTkPQSugUj_HJ_AoqAUzd6tEOvf0lBt7OoHQRqG13BrZT-TqxdaJem35pFrMC1x8-B11ZpkrquN8ZH07qPScn0nKcrc138f--abIS6XeqlqDw5R-B14SCDPiy76s8ZMHHGL4A99WMYAdzlSQsHqe-sRI0rZUsTWRDySaqc1r_wXj6CWPTHm7OAgZli60m--8dBNIjLHN3G843bNljpRy_dcTq5tNdLd0")
encoder = SentenceTransformer("all-MiniLM-L6-v2")

slug="Nuclia_Information_1"
kbid="c8648aa8-895a-4c09-920a-2ff19cb245a3"

#def get_nucliadb_kb(slug):
#    try:
#        # Attempt to retrieve the specific knowledge box by slug
#        kb = sdk.get_knowledge_box(kbid='6f51012d893140519af7f8718d8e6d13', slug=slug)
#        # If the knowledge box with the given slug doesn't exist, create it
#    except Exception as e:
#        print(f"Error accessing NucliaDB: {e}")
#        return None

@app.route('/')
def home():
    app.logger.debug("Serving the home page")
    return app.send_static_file('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Retrieve knowledge box by slug
    kb = sdk.get_resource_by_slug(kbid=kbid, slug=slug)
    if not kb:
        return jsonify({"error": "Knowledge Box could not be accessed or created"}), 500

    # Get the search query from the request
    data = request.json
    query = data['query']
    query_vectors = encoder.encode([query])[0].tolist()

    # Perform the search
    results = sdk.search(kbid=kbid, vector=query_vectors, vectorset="base", min_score=0.25)
    
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
    
