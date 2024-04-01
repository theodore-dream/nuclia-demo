import os
import requests
import sys
import mimetypes
import urllib3
from nuclia import sdk
urllib3.disable_warnings()

# Initialize SDK connection
cloud_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706"
reader_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE2NTk2LCJzdWIiOiJmMWQ2MTM1NC01MDJjLTQwMzItODFjYy02MzE5OTBiZjQwYmUiLCJqdGkiOiI5ZmY0OWQ3NS00YTI4LTQ1ZWUtODY1NS1hY2RjM2VlNmNiMTkiLCJleHAiOjE3NDI5NTI1OTYsImtleSI6ImM5NmE2YWRlLWY4OWEtNDFlOS1iMDMzLTBmM2ZlYTE0MGM0ZiIsImtpZCI6IjgxMWRmMDhkLThjMTctNDgyOS1hZTA1LTc3NzVjNWViNWMwOSJ9.CkEoKCXjJi54xAaoKPWsQgwVxnYFqhSCMN2YPBewomv2l4PD2XpH9OB1BPe-m2muymTCBNdvvculNdzarVpUnOaE2zprvOdYofSWWv29-12KHNdt1N1dJvBcl7cFumZKvrx3Qkbl2l37-cGFzkwVKMkHjM1yoTjnW4FCVt0wreHL3cjZcI-bhRIawTFkqh9k-L3BheSB-_im0uiMllJeUMIfGf4JHRE69MaYFenDteGIIFXKG_L_w50rnk8_rySSU305dESi7WY9EQS0Sm-_bA1ezpq41NBVk1I9qEFvgWL0ARZFMGXSYVC6532i1zircr0SA-DrcyXAXsmO2Qffm_mGaU1_2-NJLTIEImN4jwRu_swzeOKin3jocW5npeHyBIWEyqJkqBjnqZjsACG84fvHCUyfvAkhVr5HxBYOvR1EdBgEHpXuGs-o2pm8rdP_BPvkdd1pkOY8zXdJp_U1MifvVxpGPhXQT5E2dyao-OWaMX_pnRsvAiRMIpjuHQHw6cF_V4hssVsAQqJKRBlB4OW6pe_elwSXd5aNn2oYl7DmeTS4TpTCAtFRQ1mAZbFhUeFb9kKqVPtDzbR0C8hucclS_d6WX8PJJQ2Khm45dPm0j1DRaehlThs4dPAXUMPQQx0P55wuDaQUbRK4yGxzpN2woSplUP7Sbd0PpX7dXnY"
sdk.NucliaAuth().kb(url=cloud_url, token=reader_api_key)

# kbid is already in cloud URL
#kbid = "6fd0e260-56f2-4269-ae4a-f944bc8df706"

def list_resources(cloud_url, reader_api_key):
    # Endpoint to list resources in the knowledge box
    resources_url = f"{cloud_url}/resources"

    # Header with the READER API key
    headers = {
        "X-NUCLIA-SERVICEACCOUNT": f"Bearer {reader_api_key}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(resources_url, headers=headers, verify=False)
        if response.status_code == 200:
            resources_data = response.json()
            for resource in resources_data.get('resources', []):
                print_resource_details(resource)
            return resources_data
        else:
            return f'Error {response.status_code}: {response.text}'
    except requests.RequestException as e:
        return f'Error making request: {e}'

def print_resource_details(resource):
    print(f"ID: {resource.get('id')}")
    print(f"Title: {resource.get('title')}")
    print(f"Summary: {resource.get('summary')}")
    print(f"Created: {resource.get('created')}")
    print(f"Modified: {resource.get('modified')}")
    print(f"Status: {resource.get('metadata', {}).get('status')}")
    print("...")  # Add more fields as needed

list_resources(cloud_url, reader_api_key)