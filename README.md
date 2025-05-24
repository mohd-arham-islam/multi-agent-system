# Travel Agent Setup

## 1. Clone the Repository

```bash
git clone https://github.com/mohd-arham-islam/multi-agent-system.git
```

## 2. Set Up API Keys

Create a `.env` file inside the `multi-agent-manager` folder with the following content:

```ini
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY="<YOUR_GOOGLE_API_KEY>"
WEATHER_API_KEY="<YOUR_WEATHER_API_KEY>"
NATIONAL_PARK_SERVICES_API="<YOUR_NPS_API_KEY>"
```
Replace the placeholders with your actual API keys.

## 3. Run the Agent
Navigate to the parent folder (which contains the multi-agent-manager sub folder) and run the following code:

```ini
adk web
```

Open the URL (usually http://localhost:8000) shown in the terminal in your browser to start chatting with your agent.
