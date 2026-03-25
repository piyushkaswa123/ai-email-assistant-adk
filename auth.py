import os
from msal import PublicClientApplication
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

# IMPORTANT for personal account
AUTHORITY = "https://login.microsoftonline.com/common"

SCOPES = ["Mail.Read", "Mail.Send", "User.Read"]


def get_access_token():
    app = PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY
    )

    accounts = app.get_accounts()

    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        result = app.acquire_token_interactive(scopes=SCOPES)

    if "access_token" in result:
        print("✅ Token ready")
        return result["access_token"]
    else:
        print("❌ Error:", result)
        return None