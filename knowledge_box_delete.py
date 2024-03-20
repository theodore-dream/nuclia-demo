from nucliadb_sdk import NucliaDB, Region
from nuclia import sdk

# Initialize SDK
sdk = NucliaDB(region=Region.ON_PREM, url="http://localhost:8080/api")

def delete_resource(slug):
    sdk.delete_resource_by_slug(kbid='fbbcca549e8d4acfbceaea573aae907a', rslug=slug)  # Similarly, ensure parameter names match the SDK's expectations

# Usage example
slug = 'Nuclia_Information_1'  # Replace with the actual knowledge box ID
delete_resource(slug)
