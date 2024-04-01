import urllib3
from nuclia import sdk
urllib3.disable_warnings()

cloud_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706"
writer_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE2NTk2LCJzdWIiOiJmMWQ2MTM1NC01MDJjLTQwMzItODFjYy02MzE5OTBiZjQwYmUiLCJqdGkiOiI5ZmY0OWQ3NS00YTI4LTQ1ZWUtODY1NS1hY2RjM2VlNmNiMTkiLCJleHAiOjE3NDI5NTI1OTYsImtleSI6ImM5NmE2YWRlLWY4OWEtNDFlOS1iMDMzLTBmM2ZlYTE0MGM0ZiIsImtpZCI6IjgxMWRmMDhkLThjMTctNDgyOS1hZTA1LTc3NzVjNWViNWMwOSJ9.CkEoKCXjJi54xAaoKPWsQgwVxnYFqhSCMN2YPBewomv2l4PD2XpH9OB1BPe-m2muymTCBNdvvculNdzarVpUnOaE2zprvOdYofSWWv29-12KHNdt1N1dJvBcl7cFumZKvrx3Qkbl2l37-cGFzkwVKMkHjM1yoTjnW4FCVt0wreHL3cjZcI-bhRIawTFkqh9k-L3BheSB-_im0uiMllJeUMIfGf4JHRE69MaYFenDteGIIFXKG_L_w50rnk8_rySSU305dESi7WY9EQS0Sm-_bA1ezpq41NBVk1I9qEFvgWL0ARZFMGXSYVC6532i1zircr0SA-DrcyXAXsmO2Qffm_mGaU1_2-NJLTIEImN4jwRu_swzeOKin3jocW5npeHyBIWEyqJkqBjnqZjsACG84fvHCUyfvAkhVr5HxBYOvR1EdBgEHpXuGs-o2pm8rdP_BPvkdd1pkOY8zXdJp_U1MifvVxpGPhXQT5E2dyao-OWaMX_pnRsvAiRMIpjuHQHw6cF_V4hssVsAQqJKRBlB4OW6pe_elwSXd5aNn2oYl7DmeTS4TpTCAtFRQ1mAZbFhUeFb9kKqVPtDzbR0C8hucclS_d6WX8PJJQ2Khm45dPm0j1DRaehlThs4dPAXUMPQQx0P55wuDaQUbRK4yGxzpN2woSplUP7Sbd0PpX7dXnY"
sdk.NucliaAuth().kb(url=cloud_url, token=writer_api_key)

# init SDK
#kb = sdk.NucliaKB()

# Initialize the upload and summarize modules
upload = sdk.NucliaUpload()

# List of URLs
urls = [
    'https://en.wikipedia.org/wiki/Vector_database',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://en.wikipedia.org/wiki/Prompt_engineering',
    'https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence',
    'https://en.wikipedia.org/wiki/Large_language_model',
    'https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)',
    'https://en.wikipedia.org/wiki/Natural_language_processing',
    'https://en.wikipedia.org/wiki/OpenAI',
    'https://en.wikipedia.org/wiki/Microsoft_Azure',
    'https://en.wikipedia.org/wiki/Anthropic',
]


# Loop through the list of URLs

for url in urls:
    # Upload the URL
    resource_id = upload.link(uri=url)

