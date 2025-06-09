import msal
import base64

def get_graph_token():
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    tenant_id = "YOUR_TENANT_ID"

    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

    scope = ["https://graph.microsoft.com/.default"]

    token_response = app.acquire_token_for_client(scopes=scope)

    return token_response['access_token']

def get_azure_pat_token():
    pat = "YOUR_PERSONAL_ACCESS_TOKEN"
    pat_bytes = f":{pat}".encode("ascii")
    pat_base64 = base64.b64encode(pat_bytes).decode("ascii")
    return pat_base64
