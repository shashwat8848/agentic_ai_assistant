#  Agentic AI Personal Assistant

**Capstone Project | Agentic AI Track**

A conversational AI agent powered by **Google Gemini** that can understand context, use tools, break down tasks, and hold multi-turn conversations — all from your terminal.

---

##  Problem Statement

People often need a smart assistant that can do more than just answer questions — they need something that can plan tasks, perform calculations, recall conversation context, and act like a real agent. Standard chatbots lack this agentic capability.

##  Features

| Feature | Description |
|--------|-------------|
|  Multi-turn Conversation | Remembers full chat history in a session |
|  Tool Use | Auto-detects when to use tools (search, calculate, time) |
|  Task Planner | Breaks complex tasks into actionable steps |
|  Calculator | Evaluates math expressions safely |
|  Time Awareness | Fetches current date and time |
|  Web Search | Integrates with search tools (configurable) |
|  Conversation Save | Exports full chat log to a text file |
|  Session Reset | Clear history and start fresh anytime |

---

##  Tech Stack

- **Language**: Python 3.10+
- **AI Model**: Google Gemini 1.5 Flash (via `google-generativeai`)
- **Tools**: Custom Python tool functions
- **Environment**: `python-dotenv`

---

##  Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-assistant.git
cd agentic-ai-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a FREE Google Gemini API Key
- Go to: https://aistudio.google.com/app/apikey
- Sign in with your Google account
- Click **"Create API Key"**
- Copy the key

### 4. Set your API Key
```bash
# Copy the example env file
cp .env.example .env

# Open .env and replace YOUR_API_KEY_HERE with your actual key
```

### 5. Run the assistant
```bash
python agent.py
```

---

##  Example Usage

```
You: What time is it?
 Assistant: [Uses get_current_time tool] It's Friday, April 17, 2026 at 10:30 AM.

You: Plan a project for me to build a todo app
 Assistant: Here's a step-by-step plan:
   Step 1: Define requirements...
   Step 2: Design the UI...
  ...

You: Calculate 15% of 4500
 Assistant: [Uses calculate tool] 15% of 4500 = 675.0
```

---

##  Project Structure

```
agentic-ai-assistant/
│
├── agent.py           # Main agent with conversation loop
├── tools.py           # Tool functions (search, calc, time, summarize)
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template
└── README.md          # Project documentation
```

---

##  Future Improvements

- Integrate real-time web search (Serper, Tavily API)
- Add a web-based UI using Streamlit or Flask
- Add memory persistence across sessions (database)
- Voice input/output support
- Multi-agent collaboration (planner + executor agents)

---

##  Author

- **Name**: Shashwat Singh
- **Roll Number**: 23051053
- **Batch/Program**: 2023-27 | BTech CSE

---

##  License

This project is submitted as part of the Capstone Project requirement.
