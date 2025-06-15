# Travel Agent Setup
This project demonstrates a Multi-Agent System (MAS) using the A2A protocol, where specialized agents collaborate to solve complex tasks through intelligent delegation.
In this example, we build a system of independent, focused agents that work together under a coordinating Root Agent. This design is ideal for scenarios where a single agent would be insufficient to handle multiple specialized requests.

## 👥 Agents in the System

### 🧱 Root AgentActs as the central coordinator. It receives user queries and delegates tasks to the most relevant specialized agent.

### 🌦️ Weather AgentProvides current and forecasted weather for any specified location.

### ✈️ Flight Finder AgentSearches for flight options using Google Search.

### 🏜️ National Park Service AgentFetches alerts, activities, and basic info about U.S. National Parks via the NPS API.

## 🔗 Powered by the A2A Protocol

Each agent runs as a separate service and communicates through the Agent-to-Agent (A2A) protocol, enabling plug-and-play interoperability without custom integration code.

## 1. Clone the Repository

```bash
git clone https://github.com/mohd-arham-islam/multi-agent-system.git
```

## 2. Install Python dependencies

```bash
pip install python-dotenv google-adk requests
```

## 3. Set Up API Keys

Create a `.env` file inside the `multi-agent-manager` folder with the following content:

```ini
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY="<YOUR_GOOGLE_API_KEY>"
WEATHER_API_KEY="<YOUR_WEATHER_API_KEY>"
NATIONAL_PARK_SERVICES_API="<YOUR_NPS_API_KEY>"
```
Replace the placeholders with your actual API keys.

## 4. Run the Agent
Navigate to the parent folder (which contains the multi-agent-manager sub folder) and run the following code:

```ini
adk web
```

Open the URL (usually http://localhost:8000) shown in the terminal in your browser to start chatting with your agent.
