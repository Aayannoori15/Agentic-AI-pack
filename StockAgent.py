from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), YFinanceTools()],
        add_datetime_to_context=True,
        description=(
            "Analyse user input regarding stock prices "
            "and provide analysis with analyst recommendations."
        ),
        instructions=(
            "Use DuckDuckGo to scrape news about the user query "
            "and YFinance to find up-to-date stock information."
        ),
        markdown=True,
    )

stock_agent = build_agent()
stock_agent.print_response("Give me analyst recommendations about Tata Steel stocks.")