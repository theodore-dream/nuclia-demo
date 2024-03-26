import requests
from nuclia import sdk


my_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InNhIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDEzMDI5LCJzdWIiOiI0OTVlY2E0Yi0yZmYzLTQ5OTMtYTdhNC0yOGRiNTQyNWZmMDQiLCJqdGkiOiJlYWVhNTI1OC05N2ViLTRmZDMtOTY2Mi05YWU2MmJhNzMyYmUiLCJleHAiOjE3NDI5NDkwMjksImtleSI6IjlkODRjZjdlLTFiNzctNDAyMi1iZTY4LWExMTcyMDFjODljMCIsImtpZCI6IjAxNGIxOGM2LTcxNjgtNDI1Yy1hZGZlLWUxN2EzMmI2NzU0ZSJ9.dd94cyKa0VOakxQdH3pm3TBqxVWWM4F3chGr4HIeRiqfRu5D_rf-Ifow2CoODBMfBcEf5VrN_qC8Bmlel5wu4Lg9FyxFp8j4fWKuWcRbEpJ_4SovHhmJXm0RmlFrZD-jnPcEFxfbiwKA99u8glipx2zNz6zHj-YhRN5zsYfgC_mD7duV9wQA9LlWov2keM_S8jnslaPN1hoZZG2rwT8AjicccjCIwRE_BPPW9-YA2fX90O1GXIutdgOpQiMCv_MdME-EqNKkK3qKqfiXs-6n8R0TTQDOyXI7JhI1quOqe7ETAPWtjIGOVoWMXbkkMTP-DTKopD-g_vewjd1tuURJpIBVbS9oLKg2XdR1rjzRPe0DVuHM7auD626EBXyD7JeI670HuxWxpERRk-7iL6r43nT-7ik7ACd255HlBh_PbVNOrnYEwUuZyHKE4Ap7z4TbtjvG-absSqNmzcLFHp5QqZzLYaYKihKuVYEeA6N3KE6h4j_I0ms51DENZisnzNaEijx7RXbOdeeZVsEQ-_gTdagsJBdYM_3nvOHL6seW1CWvCIUEsue521u4WYW6WxhVzynEBMm5DQlYAkIN3LRS0MeH2zsSABwujqYBuF_UevET35L4yxS_-ohRIZUSFkFraNdLNc68tvlGkRZ3nkoJdQh1bdSnQNyfDWN8V0MbVOY"

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
my_api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im51YSJ9.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzExNDE1MDM4LCJzdWIiOiIwZTVjYmFkMC05MTNhLTRmYmYtYTExYi1iZTEwYjQ3ZjA4MzciLCJqdGkiOiI2MGMwYTcxZS0xNjZjLTQ3NTAtYjA2ZS0wNzJkNGM4MTQ4MmUiLCJleHAiOjI1MzM3MDc2NDgwMCwia2V5IjoiNzkyYmRhOTktNGNhMy00YmZjLTlhZGEtYWU2MjlhNmY1NjIwIiwiYWxsb3dfa2JfbWFuYWdlbWVudCI6dHJ1ZX0.JXe1wNVJOgZ8-lTwYbGHG1iSxDWDrT6dYXXOIWE-NBP9e6DeVFUUkUxC7V_zXdINMbaL8WV89EgiDO4zR9RfxPIs_MMJK-QE21ZgrLLUUxHFOdMc62JD_ObxXPKi1U67vjNI-d0dGFqxOqESejTsI30uhgLYKTRado6IRs9EZYkXNk2bCr3FDGaK2XayoEoweIO8T7kGBXSqoZedsPkRmD1iHgM8I5GFXJefnoxAEDqh_FtnGbg6J5X7ONSF4IoOXQJrNE32dHPai1seLycdhXTHuTgSrnrmmHN8HXz8CQqxx7uAkvRPjvNlwATFbqLfO7tm3aqAvGGRnMOdaJjofNe5l9TcEyx-duFlV4d5PpmENPoR34c0y1SMQPdvmHAZfo0NR3VAuPv5vMYnqQajo2mhAbNuEQUmSpFHUeN2w_3mTYWrqkiE2rQ4GhgiqUukWF_MVziTyTxV2b9kGfD7Y3goieKGYS8pckA0B_Ep9ULViz1Kh5Ky2sDcIfyERN9riR1pmtYhFRwA16e1ycTOWkyUtXtxqwtF6zoT_Aehuq4a5aFC7JAZ1JkimAAbGVCxHNTdGOsmyF8YHkHQgHi702SxA3ToGJLdf1ga3aN96Floo8D8KxmmAgpa23EVZH2Gj3T0EIcA35QnobS5devjjpKpwfiMqvE3s1GwMh1IWj8"

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