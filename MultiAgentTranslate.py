from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

model = Groq(id='qwen/qwen3-32b')

eng_agent = Agent(
    name='english agent',
    role="translate or answer in English",
    model=model
)

hindi_agent = Agent(
    name='hindi agent',
    role="translate or answer in Hindi",
    model=model
)

chinese_agent = Agent(
    name='chinese agent',
    role="translate or answer in Chinese",
    model=model
)

team = Team(
    name='translation team',
    members=[eng_agent, hindi_agent, chinese_agent],
    model=model,
    markdown=True,
    show_members_responses=True
)

team.print_response("ap kaise ho?")