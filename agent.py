from google.adk.agents.llm_agent import Agent
from .tools import get_emails, send_email

root_agent = Agent(
    model="gemini-2.5-flash",
    name="email_agent",
    description="AI email assistant that can read and send emails",

    instruction="""
        You are an intelligent email assistant.

        You can:
        - Fetch emails using get_emails
        - Send emails using send_email

        IMPORTANT RULES:
        - If user asks anything about emails (summary, sender, content, etc.), ALWAYS call get_emails first.
        - Then use the fetched data to answer.

        Examples:
        - "Show my emails" → call get_emails
        - "Summarize my last email" → call get_emails, then summarize
        - "Who sent the last email" → call get_emails, then answer

        Always think step-by-step:
        1. Fetch emails if needed
        2. Then answer using that data
        """,

    tools=[get_emails, send_email],
)