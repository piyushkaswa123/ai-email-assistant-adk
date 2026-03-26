import os
from msal import PublicClientApplication, SerializableTokenCache
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
AUTHORITY = "https://login.microsoftonline.com/common"
SCOPES = ["Mail.Read", "Mail.Send", "User.Read"]

# 🔥 Token cache file
CACHE_FILE = "token_cache.bin"

# 🔥 Create cache object
cache = SerializableTokenCache()

# 🔥 Load cache from file if exists
if os.path.exists(CACHE_FILE):
    cache.deserialize(open(CACHE_FILE, "r").read())


def get_access_token():
    app = PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        token_cache=cache  # ✅ attach cache
    )

    accounts = app.get_accounts()

    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        result = app.acquire_token_interactive(scopes=SCOPES)

    # 🔥 Save cache after login
    if cache.has_state_changed:
        with open(CACHE_FILE, "w") as f:
            f.write(cache.serialize())

    if "access_token" in result:
        print("✅ Token ready (cached)")
        return result["access_token"]
    else:
        print("❌ Error:", result)
        return None