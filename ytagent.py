from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from agno.tools.youtube import YouTubeTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YouTubeTools()],
        add_datetime_to_context=True,
        description=(
            "Analyse user input regarding Youtube video links "
            "and provide analysis with respect to Content of the video and other insights ."
        ),
        instructions=(
            "use youtubetools for analysing video "
        ),
        markdown=True,
    )
agent=build_agent()

agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)