
from nucliadb_sdk import NucliaDB, Region
from nuclia import sdk

# Initialize SDK
sdk = NucliaDB(region=Region.ON_PREM, url="http://localhost:8080/api")


def list_resources(kb_id):
    resources= sdk.list_resources(kbid=kb_id)  # Ensure the parameter name matches what the SDK expects
    print(resources)
    return resources

kb_id = 'f73ad734de1d4bd3be3011f0b22dab90'  # Replace with the actual knowledge box ID
list_resources(kb_id)

