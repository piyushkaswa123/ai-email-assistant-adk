import requests
from .auth import get_access_token


def get_emails(sender_filter: str = None) -> dict:
    """
    Fetch latest emails from Outlook.

    Optional:
    - sender_filter: filter emails by sender name
    """

    access_token = get_access_token()

    url = "https://graph.microsoft.com/v1.0/me/messages?$top=5"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"status": "error", "message": response.text}

    data = response.json()

    emails = []

    for mail in data.get('value', []):
        sender_name = mail['from']['emailAddress']['name']

        # 🔍 Filter by sender if provided
        if sender_filter and sender_filter.lower() not in sender_name.lower():
            continue

        emails.append({
            "sender": sender_name,
            "subject": mail.get('subject', ''),
            "body": mail.get('bodyPreview', ''),
            "date": mail.get('receivedDateTime', '')
        })

    return {
        "status": "success",
        "count": len(emails),
        "emails": emails
    }


def send_email(to_email: str, subject: str, body: str) -> dict:
    """
    Send an email using Outlook
    """

    access_token = get_access_token()

    url = "https://graph.microsoft.com/v1.0/me/sendMail"

    email_data = {
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

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=email_data)

    if response.status_code == 202:
        return {
            "status": "success",
            "message": f"Email sent to {to_email}"
        }
    else:
        return {
            "status": "error",
            "message": response.text
        }

# def summarize_emails(emails: list) -> dict:
#     """Summarizes list of emails"""
    
#     if not emails:
#         return {"status": "success", "summary": "No emails found."}

#     summary = []
#     for email in emails:
#         summary.append(f"{email['sender']}: {email['subject']}")

#     return {
#         "status": "success",
#         "summary": "\n".join(summary)
#     }