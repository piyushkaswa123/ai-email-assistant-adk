# 📧 AI Email Assistant using Google ADK

## 🚀 Overview

This project is an AI-powered Email Assistant built using **Google Agent Development Kit (ADK)** and **Gemini LLM**.
The agent can interact with a user's Outlook inbox using the **Microsoft Graph API**.

It can:

* 📥 Read emails
* ❓ Answer questions about emails
* ✉️ Send emails automatically
* 🧠 Summarize emails

---

## 🧠 Architecture

```
User → ADK Agent (Gemini LLM) → Tools → Microsoft Graph API → Response
```

* **Gemini LLM** → Understands user intent
* **ADK Agent** → Decides which tool to call
* **Tools** → Perform actions (read/send emails)
* **Microsoft Graph API** → Real email data

---

## 🛠️ Tech Stack

* Python
* Google ADK
* Gemini API
* Microsoft Graph API
* MSAL (Authentication)

---

## 🔐 Authentication

* Uses **OAuth 2.0 (Delegated Flow)**
* User logs in via browser
* Access token is used to call Microsoft Graph API

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd email_assistant
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create `.env` file

Add the following:

```env
GOOGLE_API_KEY=your_gemini_api_key
CLIENT_ID=your_azure_app_client_id
```

---

### 4. Run the Agent

#### ▶️ CLI Mode

```bash
adk run email_assistant
```

#### 🌐 Web UI

```bash
adk web --port 8000
```

Open in browser:

```
http://localhost:8000
```

---

## 💬 Example Prompts

Try these in CLI or UI:

* `show my emails`
* `who sent the latest email`
* `summarize my latest email`
* `show emails from Microsoft`
* `send email to xyz@gmail.com saying hello`

---

## ✨ Features

* ✅ Natural language understanding using Gemini
* ✅ Tool-based architecture (ADK)
* ✅ Real-time Outlook email integration
* ✅ Email filtering and summarization
* ✅ Email sending capability

---

## 🎯 Key Learnings

* Building AI agents using ADK
* Integrating LLMs with external APIs
* Implementing OAuth authentication
* Designing tool-based architectures

---

## 📌 Future Improvements

* Add memory (conversation context)
* Smart email replies
* Email categorization
* Deployment as a web app

---

## 👨‍💻 Author

**Piyush Kaswa**

---

## 📽️ Demo

(Attach demo video link here)
