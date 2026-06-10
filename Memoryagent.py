from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

load_dotenv()
db=SqliteDb(db_file='agno.db')
#db.clear_memories()
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
        db=db,
        add_history_to_context=True,
        enable_agentic_memory=True,
        markdown=True,
    )

stock_agent = build_agent()
user_id="aayan"
stock_agent.print_response("Give me analyst recommendations about Tata Steel stocks.",user_id=user_id)
stock_agent.print_response("is it a big company",user_id=user_id)