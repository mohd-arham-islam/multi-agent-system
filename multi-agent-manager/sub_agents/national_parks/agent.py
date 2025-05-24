import os
from typing import Optional
import requests
from google.adk.agents import Agent

from dotenv import load_dotenv

load_dotenv()
NPS_API_KEY = os.getenv("NATIONAL_PARK_SERVICES_API")


def get_things_to_do(
    park_code: Optional[str] = None,
    state_code: Optional[str] = None,
    q: Optional[str] = None,
    limit: int = 10,
    sort: Optional[str] = None
) -> dict:
    """
    Get suggested things to do in national parks.
    
    Args:
        park_code (str): Optional 4-letter park code (e.g., "yose").
        state_code (str): Optional 2-letter state code (e.g., "CA").
        q (str): Optional search term (e.g., "camping").
        limit (int): Number of results to return. Default is 10.
        sort (str): Optional sort key (e.g., "-relevanceScore").
    
    Returns:
        dict: List of things to do or error message.
    """
    if not NPS_API_KEY:
        return {"status": "error", "error": "Missing NPS API key"}

    base_url = "https://developer.nps.gov/api/v1/thingstodo"
    params = {
        "limit": limit,
        "api_key": NPS_API_KEY
    }

    if park_code:
        params["parkCode"] = park_code
    if state_code:
        params["stateCode"] = state_code
    if q:
        params["q"] = q


    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "status": "success",
            "things_to_do": data.get("data", []),
            "total": data.get("total", 0)
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}
    
def get_alerts(
    park_code: Optional[str] = None,
    state_code: Optional[str] = None,
    limit: int = 10
) -> dict:
    """
    Get alerts for specific parks or states (closures, cautions, etc.).
    
    Args:
        park_code (str): Optional NPS park code (e.g., "yose", "grca").
        state_code (str): Optional 2-letter state code (e.g., "CA").
        limit (int): Number of results to return.
    
    Returns:
        dict: Alerts or error message.
    """
    if not NPS_API_KEY:
        return {"status": "error", "error": "Missing NPS API key"}

    base_url = "https://developer.nps.gov/api/v1/alerts"
    params = {
        "limit": limit,
        "api_key": NPS_API_KEY
    }

    if park_code:
        params["parkCode"] = park_code
    if state_code:
        params["stateCode"] = state_code

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "status": "success",
            "alerts": data.get("data", []),
            "total": data.get("total", 0)
        }

    except Exception as e:
        return {"status": "error", "error": str(e)}
    
national_parks = Agent(
    name="national_parks",
    model="gemini-2.0-flash",
    description="Provides information about things to do and safety alerts in U.S. national parks.",
    instruction="""
You are a National Parks expert assisting travelers with park-specific insights. 
Your responsibilities include:
- Listing things to do in a national park.
- Checking for safety alerts like closures, fire warnings, or weather cautions.
Always convert the park name or the state into its respective 4 and 2 digits code.
If the information is not present, then ask the user to specify the same.
If either one is present, then use it to call the tools.

When a user asks about things to do, call the `get_things_to_do` tool.
When a user asks about risks, alerts, closures, or travel safety in a specific park or state, call `get_alerts`.

Keep answers concise and useful for someone planning a trip. Mention the park name when relevant.
""",
    tools=[get_things_to_do, get_alerts]
)