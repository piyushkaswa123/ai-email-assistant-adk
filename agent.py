from google.adk.agents.llm_agent import Agent
from .tools import get_emails, send_email, summarize_emails

root_agent = Agent(
    model="gemini-2.5-flash",
    name="email_agent",
    description="AI email assistant that can read and send emails",

    instruction="""
    You are an intelligent email assistant.

    Your responsibilities:
    - Read and summarize user emails clearly
    - Send emails professionally when asked
    - Extract key details like sender, subject, and message

    Rules:
    - If user asks to read emails → use get_emails
    - If user asks to send email → use send_email
    - Always confirm before sending emails
    - Keep responses clean and structured
    """,

    tools=[get_emails, send_email, summarize_emails],
)