import requests
import re
from email.mime.text import MIMEText
import base64

from .auth import get_access_token

# ---------------- MEMORY ----------------
contacts = {}

# ---------------- HELPERS ----------------
def extract_name_email(from_field):
    """
    Extract name and email from Graph API format
    """
    name = from_field.get("emailAddress", {}).get("name", "").lower()
    email = from_field.get("emailAddress", {}).get("address", "")
    return name, email


# ---------------- GET LAST RECEIVED EMAIL ----------------
def get_last_received_email(sender_name: str = None):
    token = get_access_token()

    url = "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages?$top=10"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "value" not in data or len(data["value"]) == 0:
        return "No emails found."

    messages = data["value"]

    #  If sender_name provided → filter
    if sender_name:
        sender_name = sender_name.lower()

        for msg in messages:
            sender_info = msg.get("from", {})
            name, email = extract_name_email(sender_info)

            if sender_name in name:
                contacts[name] = email
                subject = msg.get("subject", "")
                body = msg.get("body", {}).get("content", "")

                return f"""
Sender: {name.title()} ({email})
Subject: {subject}

Body:
{body[:1000]}
"""
        return f"No emails found from {sender_name.title()}."

    #  Default → latest email
    msg = messages[0]

    sender_info = msg.get("from", {})
    subject = msg.get("subject", "")
    body = msg.get("body", {}).get("content", "")

    name, email = extract_name_email(sender_info)
    contacts[name] = email

    return f"""
Sender: {name.title()} ({email})
Subject: {subject}

Body:
{body[:1000]}
"""

# ---------------- GET LAST SENT EMAIL ----------------
def get_last_sent_email():
    token = get_access_token()

    url = "https://graph.microsoft.com/v1.0/me/mailFolders/sentitems/messages?$top=1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "value" not in data or len(data["value"]) == 0:
        return "No sent emails found."

    msg = data["value"][0]

    to_list = msg.get("toRecipients", [])
    subject = msg.get("subject", "")
    body = msg.get("body", {}).get("content", "")

    if to_list:
        to_info = to_list[0]
        name, email = extract_name_email(to_info)
    else:
        name, email = "unknown", ""

    return f"""
To: {name.title()} ({email})
Subject: {subject}

Body:
{body[:1000]}
"""


# ---------------- SEND EMAIL ----------------
def send_email(to, subject, body):
    token = get_access_token()

    to = to.lower()

    #  If input is email → use directly
    if "@" in to:
        to_email = to
        to_name = to.split("@")[0]
    else:
        #  Otherwise use contacts
        if to not in contacts:
            return f"I don’t have {to}'s email yet. Ask me to fetch their email first."

        to_email = contacts[to]
        to_name = to

    url = "https://graph.microsoft.com/v1.0/me/sendMail"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": to_email
                    }
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 202:
        return f"Email sent to {to_name.title()} ({to_email})"
    else:
        return f"Failed to send email: {response.text}"