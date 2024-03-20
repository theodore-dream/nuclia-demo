
from nucliadb_sdk import NucliaDB, Region
from nuclia import sdk

# Initialize SDK
sdk = NucliaDB(region=Region.ON_PREM, url="http://0.0.0.0:8080/api")


def list_resources(kb_id):
    resources= sdk.list_resources(kbid=kb_id)  # Ensure the parameter name matches what the SDK expects
    print(resources)
    return resources

kb_id = 'c8648aa8-895a-4c09-920a-2ff19cb245a3'  # Replace with the actual knowledge box ID
list_resources(kb_id)

