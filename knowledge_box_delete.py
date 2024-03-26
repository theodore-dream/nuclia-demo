from nucliadb_sdk import NucliaDB, Region
from nuclia import sdk

# Initialize SDK
sdk = NucliaDB(region=Region.AWS_US_EAST_2_1, url="https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706")

def delete_resource(slug):
    sdk.delete_resource_by_slug(kbid='fbbcca549e8d4acfbceaea573aae907a', rslug=slug)  # Similarly, ensure parameter names match the SDK's expectations

# Usage example
slug = 'Nuclia_Information_1'  # Replace with the actual knowledge box ID
delete_resource(slug)
