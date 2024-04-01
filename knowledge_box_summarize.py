import requests
from nuclia import sdk
import urllib3
urllib3.disable_warnings()

# Ignored files
IGNORE = [".DS_Store", "Thumbs.db"]

# Initialize SDK connection
cloud_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706"
writer_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE2NTk2LCJzdWIiOiJmMWQ2MTM1NC01MDJjLTQwMzItODFjYy02MzE5OTBiZjQwYmUiLCJqdGkiOiI5ZmY0OWQ3NS00YTI4LTQ1ZWUtODY1NS1hY2RjM2VlNmNiMTkiLCJleHAiOjE3NDI5NTI1OTYsImtleSI6ImM5NmE2YWRlLWY4OWEtNDFlOS1iMDMzLTBmM2ZlYTE0MGM0ZiIsImtpZCI6IjgxMWRmMDhkLThjMTctNDgyOS1hZTA1LTc3NzVjNWViNWMwOSJ9.CkEoKCXjJi54xAaoKPWsQgwVxnYFqhSCMN2YPBewomv2l4PD2XpH9OB1BPe-m2muymTCBNdvvculNdzarVpUnOaE2zprvOdYofSWWv29-12KHNdt1N1dJvBcl7cFumZKvrx3Qkbl2l37-cGFzkwVKMkHjM1yoTjnW4FCVt0wreHL3cjZcI-bhRIawTFkqh9k-L3BheSB-_im0uiMllJeUMIfGf4JHRE69MaYFenDteGIIFXKG_L_w50rnk8_rySSU305dESi7WY9EQS0Sm-_bA1ezpq41NBVk1I9qEFvgWL0ARZFMGXSYVC6532i1zircr0SA-DrcyXAXsmO2Qffm_mGaU1_2-NJLTIEImN4jwRu_swzeOKin3jocW5npeHyBIWEyqJkqBjnqZjsACG84fvHCUyfvAkhVr5HxBYOvR1EdBgEHpXuGs-o2pm8rdP_BPvkdd1pkOY8zXdJp_U1MifvVxpGPhXQT5E2dyao-OWaMX_pnRsvAiRMIpjuHQHw6cF_V4hssVsAQqJKRBlB4OW6pe_elwSXd5aNn2oYl7DmeTS4TpTCAtFRQ1mAZbFhUeFb9kKqVPtDzbR0C8hucclS_d6WX8PJJQ2Khm45dPm0j1DRaehlThs4dPAXUMPQQx0P55wuDaQUbRK4yGxzpN2woSplUP7Sbd0PpX7dXnY"
reader_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE4MzI1LCJzdWIiOiJmNGExODNkMC1mYWIzLTQwNjYtYmZhZS03YmE1OTRjMzhkMDgiLCJqdGkiOiIwZTc4Y2M0My1kNWY2LTRmYTQtODBlMS04NWMzODA3YTIyMWMiLCJleHAiOjE3NDI5NTQzMjQsImtleSI6Ijc4NDc5MGIyLTI5NmYtNDAzOS1hMzJlLTM4MjI3NjdiOTg3MCIsImtpZCI6ImM2ZTZkYjZjLTZkMzQtNGExYS1iNzA5LTJhMWZlMjQ5YWRkYyJ9.Bd3GJfdVKpheiXWfIBpZO9R3SlRwuOtegz8nPK5CEjEEodA3MZMejb-GRsk2gk8aNPUXTu5yAIXMx_x8fM4CW0h_TXqPTyLUqbLvytBJHH61ynY0WWEj32J2t8vuCxks5qnZLS-2noVum2GRREt-IDzJ78a3SHsm-v019OpH7sIbR0tZT2PAyZrz50tscEUpeF9buhDncK5rwPQoyFFLjzwFbosZOdZmtKn8pix4odRJLlCDKd-J7O5rfHkrLx7k4NktBwyRtNm1qWAGAD1l_xYUMKQMnflS_I3pw2mT7CHPQF5AB05oyTA4BkgLGph3zyfF7W8C5Vtnn4_PvhX-dTpQZUccHt1WJ6db7V9V0p-GBDftqAA3cHKY37dHQBZJMUauVKmd5KFOvNc6bS-4TjZ9XqTufZgB-A39dmJtjxRegLPX3HmtkDsYIcKy5VVS2fg6YmTmSJBHzKYPb5jK8su2iGaQHWVzb763qEkAa8zQpGx1ylmzbuQBT2SQovr1sY7Z4OBSU2iWiCf6UAH6VmrIfvG4k1jTYcxQ6R5mSCZC8foxb_RNM5Wd0C8JtQJC3UkIpbmfGmWtK0TGCSJTx0WgjnJJmuK2t1xFjDgQwSv893vfxRDEvmzONmmzcMNvMg39iu8iQ5i-naC42qi3g_e-n0OUFtXuFJ_INSTm_74"
sdk.NucliaAuth().kb(url=cloud_url, token=reader_api_key)

#kbid already in cloud url
#kbid = '6fd0e260-56f2-4269-ae4a-f944bc8df706'  # Your Knowledge Box ID

def list_resources(cloud_url, reader_api_key):
    resources_url = f"{cloud_url}/resources"
    headers = {
        "X-NUCLIA-SERVICEACCOUNT": f"Bearer {reader_api_key}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(resources_url, headers=headers, verify=False)
        if response.status_code == 200:
            resources_data = response.json()
            print("successfully ran list_resources")
            return resources_data.get('resources', [])
        else:
            print(f'Error {response.status_code}: {response.text}')
            return []
    except requests.RequestException as e:
        print(f'Error making request: {e}')
        return []

def summarize_file(resource_uuid, cloud_url, reader_api_key):
    api_endpoint = f"{cloud_url}/summarize"
    headers = {
        "X-NUCLIA-SERVICEACCOUNT": f"Bearer {reader_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "user_prompt": "Create a brief summary of the following content provided: {text}",
        "resources": [resource_uuid],
        "summary_kind": "simple"
    }

    print(f"Sending request to {api_endpoint} with payload:")
    print(payload)  # Print the entire payload for debugging

    response = requests.post(api_endpoint, json=payload, headers=headers, verify=False)
    if response.status_code == 200:
        summary_data = response.json()
        print("Summary for resource", resource_uuid, ":", summary_data)
        return summary_data
    else:
        print(f'Error {response.status_code} summarizing resource {resource_uuid}: {response.text}')
        return None

def process_resources(cloud_url, reader_api_key):
    resources = list_resources(cloud_url, reader_api_key)
    for resource in resources:
        resource_uuid = resource.get('id')
        print(f"Processing resource ID: {resource_uuid}")  # Print the resource UUID
        if resource_uuid:
            summarize_file(resource_uuid, cloud_url, reader_api_key)

process_resources(cloud_url, reader_api_key)