import requests

# Vervang dit met je echte bearer token, opgevraagd via Postman of MSAL
access_token = "Bearer YOUR_ACCESS_TOKEN_HERE"

# Microsoft Graph API endpoint om je eigen profielgegevens op te vragen
url = "https://graph.microsoft.com/v1.0/me"

# HTTP headers
headers = {
    "Authorization": access_token,
    "Accept": "application/json"
}

# API request uitvoeren
response = requests.get(url, headers=headers)

# Antwoord verwerken
if response.status_code == 200:
    print("✅ Succesvolle verbinding met Microsoft Graph!")
    print(response.json())
else:
    print(f"❌ Fout: {response.status_code}")
    print(response.text)