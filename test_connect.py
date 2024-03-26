import requests
from nuclia import sdk


my_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE2NTk2LCJzdWIiOiJmMWQ2MTM1NC01MDJjLTQwMzItODFjYy02MzE5OTBiZjQwYmUiLCJqdGkiOiI5ZmY0OWQ3NS00YTI4LTQ1ZWUtODY1NS1hY2RjM2VlNmNiMTkiLCJleHAiOjE3NDI5NTI1OTYsImtleSI6ImM5NmE2YWRlLWY4OWEtNDFlOS1iMDMzLTBmM2ZlYTE0MGM0ZiIsImtpZCI6IjgxMWRmMDhkLThjMTctNDgyOS1hZTA1LTc3NzVjNWViNWMwOSJ9.CkEoKCXjJi54xAaoKPWsQgwVxnYFqhSCMN2YPBewomv2l4PD2XpH9OB1BPe-m2muymTCBNdvvculNdzarVpUnOaE2zprvOdYofSWWv29-12KHNdt1N1dJvBcl7cFumZKvrx3Qkbl2l37-cGFzkwVKMkHjM1yoTjnW4FCVt0wreHL3cjZcI-bhRIawTFkqh9k-L3BheSB-_im0uiMllJeUMIfGf4JHRE69MaYFenDteGIIFXKG_L_w50rnk8_rySSU305dESi7WY9EQS0Sm-_bA1ezpq41NBVk1I9qEFvgWL0ARZFMGXSYVC6532i1zircr0SA-DrcyXAXsmO2Qffm_mGaU1_2-NJLTIEImN4jwRu_swzeOKin3jocW5npeHyBIWEyqJkqBjnqZjsACG84fvHCUyfvAkhVr5HxBYOvR1EdBgEHpXuGs-o2pm8rdP_BPvkdd1pkOY8zXdJp_U1MifvVxpGPhXQT5E2dyao-OWaMX_pnRsvAiRMIpjuHQHw6cF_V4hssVsAQqJKRBlB4OW6pe_elwSXd5aNn2oYl7DmeTS4TpTCAtFRQ1mAZbFhUeFb9kKqVPtDzbR0C8hucclS_d6WX8PJJQ2Khm45dPm0j1DRaehlThs4dPAXUMPQQx0P55wuDaQUbRK4yGxzpN2woSplUP7Sbd0PpX7dXnY"
def test_nuclia_connectivity():
    base_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1"
    kbid = "6fd0e260-56f2-4269-ae4a-f944bc8df706"
    api_key = my_api_key # Replace 'your_api_key' with your actual API key
    headers = {'X-NUCLIA-SERVICEACCOUNT': f'Bearer {api_key}'}

    response = requests.get(f"{base_url}/kb/{kbid}", headers=headers)

    assert response.status_code == 200, "Failed to connect or access the knowledge box"
    print(f"Connection successful, status code: {response.status_code}")

# Run the test
test_nuclia_connectivity()

cloud_url = "https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/6fd0e260-56f2-4269-ae4a-f944bc8df706"
#my_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im51YSJ9.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE1MDM4LCJzdWIiOiIwZTVjYmFkMC05MTNhLTRmYmYtYTExYi1iZTEwYjQ3ZjA4MzciLCJqdGkiOiI2MGMwYTcxZS0xNjZjLTQ3NTAtYjA2ZS0wNzJkNGM4MTQ4MmUiLCJleHAiOjI1MzM3MDc2NDgwMCwia2V5IjoiNzkyYmRhOTktNGNhMy00YmZjLTlhZGEtYWU2MjlhNmY1NjIwIiwiYWxsb3dfa2JfbWFuYWdlbWVudCI6dHJ1ZX0.JXe1wNVJOgZ8-lTwYbGHG1iSxDWDrT6dYXXOIWE-NBP9e6DeVFUUkUxC7V_zXdINMbaL8WV89EgiDO4zR9RfxPIs_MMJK-QE21ZgrLLUUxHFOdMc62JD_ObxXPKi1U67vjNI-d0dGFqxOqESejTsI30uhgLYKTRado6IRs9EZYkXNk2bCr3FDGaK2XayoEoweIO8T7kGBXSqoZedsPkRmD1iHgM8I5GFXJefnoxAEDqh_FtnGbg6J5X7ONSF4IoOXQJrNE32dHPai1seLycdhXTHuTgSrnrmmHN8HXz8CQqxx7uAkvRPjvNlwATFbqLfO7tm3aqAvGGRnMOdaJjofNe5l9TcEyx-duFlV4d5PpmENPoR34c0y1SMQPdvmHAZfo0NR3VAuPv5vMYnqQajo2mhAbNuEQUmSpFHUeN2w_3mTYWrqkiE2rQ4GhgiqUukWF_MVziTyTxV2b9kGfD7Y3goieKGYS8pckA0B_Ep9ULViz1Kh5Ky2sDcIfyERN9riR1pmtYhFRwA16e1ycTOWkyUtXtxqwtF6zoT_Aehuq4a5aFC7JAZ1JkimAAbGVCxHNTdGOsmyF8YHkHQgHi702SxA3ToGJLdf1ga3aN96Floo8D8KxmmAgpa23EVZH2Gj3T0EIcA35QnobS5devjjpKpwfiMqvE3s1GwMh1IWj8"

def test_sdk_nuclia_connectivity():
    api_key = my_api_key  # Replace with your actual API key
    #sdk.NucliaAuth().set_user_token(USER_TOKEN)
    sdk.NucliaAuth().kb(url=cloud_url, token=my_api_key)

    try:
        print(f"sdk Connection successful")
    except Exception as e:
        print(f"sdk Failed to connect or access the knowledge box: {e}")

# Run the test
test_sdk_nuclia_connectivity()