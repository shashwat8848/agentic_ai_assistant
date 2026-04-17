"""
Agentic AI Personal Assistant
Capstone Project - Agentic AI Track

A conversational AI agent powered by Google Gemini that can:
- Answer questions intelligently
- Break down tasks step-by-step
- Maintain conversation history
- Perform web searches
- Summarize information
"""

import google.generativeai as genai
import os
import datetime
from tools import search_web, get_current_time, calculate, summarize_text

# ─── Configuration ───────────────────────────────────────────────────────────

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GOOGLE_API_KEY)

# ─── System Prompt (defines agent personality & capabilities) ─────────────────

SYSTEM_PROMPT = """You are an intelligent Agentic AI Assistant. Your role is to:

1. Answer user questions clearly and helpfully.
2. Break down complex tasks into step-by-step plans.
3. Use available tools when needed (search, calculate, time, summarize).
4. Remember the conversation context and refer back to it when useful.
5. Be proactive — if a task has multiple steps, guide the user through each one.

Available tools you can reference:
- search_web(query): Search for information
- get_current_time(): Get current date and time
- calculate(expression): Evaluate math expressions
- summarize_text(text): Summarize long text

Always be clear, concise, and helpful. If you use a tool, explain what you found."""

# ─── Agent Class ──────────────────────────────────────────────────────────────

class AgenticAssistant:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        self.chat = self.model.start_chat(history=[])
        self.conversation_log = []

    def process_tool_calls(self, user_input: str) -> str:
        """Detect and handle tool calls from user input."""
        tool_result = ""

        # Auto-detect tool needs based on keywords
        lower_input = user_input.lower()

        if any(word in lower_input for word in ["what time", "current time", "today's date", "what date"]):
            tool_result = f"\n[Tool: get_current_time] → {get_current_time()}"

        elif any(word in lower_input for word in ["calculate", "what is", "how much is", "compute"]):
            # Try to find a math expression
            import re
            expr = re.findall(r'[\d\+\-\*\/\(\)\.\s]+', user_input)
            expr = [e.strip() for e in expr if any(c.isdigit() for c in e)]
            if expr:
                result = calculate(expr[0].strip())
                tool_result = f"\n[Tool: calculate('{expr[0].strip()}')] → {result}"

        elif any(word in lower_input for word in ["search", "find", "look up", "who is", "what is"]):
            query = user_input.replace("search", "").replace("find", "").replace("look up", "").strip()
            search_result = search_web(query)
            tool_result = f"\n[Tool: search_web] → {search_result}"

        elif any(word in lower_input for word in ["summarize", "summary", "shorten"]):
            tool_result = "\n[Tool: summarize_text] → Please paste the text you'd like summarized."

        return tool_result

    def chat_with_agent(self, user_input: str) -> str:
        """Send message to agent and get response."""
        tool_context = self.process_tool_calls(user_input)

        # Build enriched message with tool context if any
        enriched_input = user_input
        if tool_context:
            enriched_input = f"{user_input}\n\nTool Output:{tool_context}"

        # Send to Gemini
        response = self.chat.send_message(enriched_input)
        answer = response.text

        # Log the conversation
        self.conversation_log.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_input,
            "assistant": answer
        })

        return answer

    def save_conversation(self, filename: str = "conversation_history.txt"):
        """Save conversation log to file."""
        with open(filename, "w") as f:
            f.write("=== Agentic AI Assistant - Conversation Log ===\n\n")
            for entry in self.conversation_log:
                f.write(f"[{entry['timestamp']}]\n")
                f.write(f"User: {entry['user']}\n")
                f.write(f"Assistant: {entry['assistant']}\n")
                f.write("-" * 60 + "\n\n")
        print(f"\n✅ Conversation saved to {filename}")

    def display_welcome(self):
        print("=" * 60)
        print("       🤖  AGENTIC AI PERSONAL ASSISTANT  🤖")
        print("=" * 60)
        print("Powered by Google Gemini | Capstone Project")
        print("-" * 60)
        print("Commands:")
        print("  'quit' or 'exit'  → End session")
        print("  'save'            → Save conversation log")
        print("  'clear'           → Start a new conversation")
        print("  'history'         → Show conversation count")
        print("-" * 60)
        print("Ask me anything! I can search, calculate, plan tasks,")
        print("answer questions, and more.\n")


# ─── Main Loop ────────────────────────────────────────────────────────────────

def main():
    if GOOGLE_API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️  ERROR: Please set your GOOGLE_API_KEY in the .env file or environment.")
        print("   Get a free key at: https://aistudio.google.com/app/apikey")
        return

    assistant = AgenticAssistant()
    assistant.display_welcome()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit"]:
                print("\n👋 Goodbye! Saving your conversation...")
                assistant.save_conversation()
                break

            elif user_input.lower() == "save":
                assistant.save_conversation()
                continue

            elif user_input.lower() == "clear":
                assistant = AgenticAssistant()
                print("🔄 Conversation cleared. Starting fresh!\n")
                continue

            elif user_input.lower() == "history":
                print(f"📜 {len(assistant.conversation_log)} messages in this session.\n")
                continue

            print("\n🤖 Assistant: ", end="", flush=True)
            response = assistant.chat_with_agent(user_input)
            print(response)
            print()

        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please check your API key and internet connection.\n")


if __name__ == "__main__":
    main()
