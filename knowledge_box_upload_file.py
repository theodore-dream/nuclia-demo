import os
import requests
import sys
import mimetypes
import urllib3
from nuclia import sdk
urllib3.disable_warnings()


IGNORE = [
    ".DS_Store",
    "Thumbs.db",
]

# Initialize SDK connection
cloud_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706"
my_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE2NTk2LCJzdWIiOiJmMWQ2MTM1NC01MDJjLTQwMzItODFjYy02MzE5OTBiZjQwYmUiLCJqdGkiOiI5ZmY0OWQ3NS00YTI4LTQ1ZWUtODY1NS1hY2RjM2VlNmNiMTkiLCJleHAiOjE3NDI5NTI1OTYsImtleSI6ImM5NmE2YWRlLWY4OWEtNDFlOS1iMDMzLTBmM2ZlYTE0MGM0ZiIsImtpZCI6IjgxMWRmMDhkLThjMTctNDgyOS1hZTA1LTc3NzVjNWViNWMwOSJ9.CkEoKCXjJi54xAaoKPWsQgwVxnYFqhSCMN2YPBewomv2l4PD2XpH9OB1BPe-m2muymTCBNdvvculNdzarVpUnOaE2zprvOdYofSWWv29-12KHNdt1N1dJvBcl7cFumZKvrx3Qkbl2l37-cGFzkwVKMkHjM1yoTjnW4FCVt0wreHL3cjZcI-bhRIawTFkqh9k-L3BheSB-_im0uiMllJeUMIfGf4JHRE69MaYFenDteGIIFXKG_L_w50rnk8_rySSU305dESi7WY9EQS0Sm-_bA1ezpq41NBVk1I9qEFvgWL0ARZFMGXSYVC6532i1zircr0SA-DrcyXAXsmO2Qffm_mGaU1_2-NJLTIEImN4jwRu_swzeOKin3jocW5npeHyBIWEyqJkqBjnqZjsACG84fvHCUyfvAkhVr5HxBYOvR1EdBgEHpXuGs-o2pm8rdP_BPvkdd1pkOY8zXdJp_U1MifvVxpGPhXQT5E2dyao-OWaMX_pnRsvAiRMIpjuHQHw6cF_V4hssVsAQqJKRBlB4OW6pe_elwSXd5aNn2oYl7DmeTS4TpTCAtFRQ1mAZbFhUeFb9kKqVPtDzbR0C8hucclS_d6WX8PJJQ2Khm45dPm0j1DRaehlThs4dPAXUMPQQx0P55wuDaQUbRK4yGxzpN2woSplUP7Sbd0PpX7dXnY"
sdk.NucliaAuth().kb(url=cloud_url, token=my_api_key)

# Upload PDF files to the Knowledge Box
path = '/Users/rhyman/Coding/nuclia-demo/pdf_folder_nuclia'

# List PDF files in the directory
#pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# Initialize a summarization pipeline
#summarizer = pipeline("summarization")

def upload_file(content_path):
    file_name = os.path.basename(content_path).encode('ascii')
    file_upload_path = f'{cloud_url}/upload'
    print(f'Importing {content_path} at {file_upload_path}')

    with open(content_path, "rb") as source_file:
        response = requests.post(
            file_upload_path,
            headers={
                "content-type": mimetypes.guess_type(content_path)[0] or "application/octet-stream",
                "x-filename": file_name,
                "X-NUCLIA-SERVICEACCOUNT": "Bearer " + my_api_key,
                "x-synchronous": "true",
            },
            data=source_file.read(),
            verify=False,
        )
        if response.status_code != 201:
            print(f'Error {response.status_code} importing {file_name}')


def upload_folder():
    all_files = os.listdir(path)
    for content in all_files:
        if content in IGNORE or content.startswith("."):
            continue
        content_path = os.path.join(path, content)
        if os.path.isdir(content_path):
            upload_folder(content_path)
        else:
            upload_file(content_path)

upload_folder()
 


# Example search
#query = "what are the risks and challenges that Nuclia may face in regards to management of Enterprise clients"
#query_vectors = encoder.encode([query])[0].tolist()
#results = sdk.search(kbid=kb.uuid, vector=query_vectors, vectorset="base", min_score=0.25)

# Print the search results
#print("Search results for query:", query)
#print(results)
