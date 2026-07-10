from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools import tool
from playwright.sync_api import sync_playwright

load_dotenv()


@tool

def scrape_website(url: str) -> str:

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )
        text = page.locator("body").inner_text()
        browser.close()
    return text[:5000]


agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    tools=[scrape_website],
    instructions=[
        "Use the scraping tool when a URL is provided.",
        "Summarize the webpage content."
    ],
    markdown=True
)


agent.print_response(
    "Summarize this website: https://www.python.org",
    markdown=True
)