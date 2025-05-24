from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.web_search.agent import flight_search 
from .sub_agents.national_parks.agent import national_parks
from .sub_agents.weather.agent import weather_agent
from .tools.tools import get_current_time

root_agent = Agent(
    name="travel_manager",
    model="gemini-2.0-flash",
    description="Central travel coordinator agent that delegates tasks to specialized travel assistants.",
    instruction="""
You are a travel manager agent responsible for coordinating various aspects of trip planning.

Delegate tasks to the appropriate agents based on the nature of the user query:

- Use `weather_agent` to get current or forecasted weather information for a location.
- Use `national_parks` to get details about park alerts or available activities in U.S. national parks.

Additionally, use the following tools when needed:
- Use `flight_search` to look up flight options and pricing using Google Search.
- Use `get_current_time` if a user mentions a relative time (e.g., "next week", "in 3 days") or date (e.g. "this weekend")and you need to resolve it to an actual date.

Always respond based on the most relevant agent or tool for the user’s travel needs.
""",
    sub_agents=[
        weather_agent,
        national_parks
    ],
    tools=[
        get_current_time,
        AgentTool(flight_search)
    ]
)