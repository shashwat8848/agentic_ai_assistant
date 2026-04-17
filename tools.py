"""
tools.py - Tool functions available to the Agentic AI Assistant

These are callable functions the agent can use to extend its capabilities
beyond its built-in language model knowledge.
"""

import datetime
import math


def search_web(query: str) -> str:
    """
    Simulates a web search. In production, integrate with
    a real search API (e.g., Google Custom Search, Serper, Tavily).
    
    Args:
        query: Search query string
    Returns:
        Search result summary string
    """
    # In production, replace with real API call:
    # import requests
    # response = requests.get("https://api.search.com", params={"q": query, "key": API_KEY})
    # return response.json()["results"][0]["snippet"]
    
    # Simulated responses for demo purposes
    simulated_results = {
        "python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "ai": "Artificial Intelligence (AI) is the simulation of human intelligence by computer systems.",
        "machine learning": "Machine Learning is a subset of AI that enables systems to learn from data.",
        "gemini": "Google Gemini is a family of large language models developed by Google DeepMind.",
    }
    
    query_lower = query.lower()
    for key, result in simulated_results.items():
        if key in query_lower:
            return result
    
    return f"Search results for '{query}': For real-time search, integrate a Search API like Google Custom Search or Serper.dev."


def get_current_time() -> str:
    """
    Returns the current date and time.
    
    Returns:
        Formatted date and time string
    """
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y at %I:%M %p")


def calculate(expression: str) -> str:
    """
    Safely evaluates a mathematical expression.
    
    Args:
        expression: Mathematical expression as string (e.g., "2 + 3 * 4")
    Returns:
        Result of the calculation or error message
    """
    # Safe evaluation using restricted built-ins
    allowed_names = {
        "abs": abs, "round": round, "min": min, "max": max,
        "pow": pow, "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "log": math.log, "floor": math.floor, "ceil": math.ceil
    }
    
    try:
        # Remove any dangerous characters
        safe_expr = expression.replace("__", "").replace("import", "")
        result = eval(safe_expr, {"__builtins__": {}}, allowed_names)
        return str(round(result, 6))
    except Exception as e:
        return f"Could not calculate: {e}"


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Provides a basic extractive summary by selecting key sentences.
    For production, use an LLM API or NLP library for better results.
    
    Args:
        text: Long text to summarize
        max_sentences: Maximum number of sentences in summary
    Returns:
        Summarized text
    """
    if not text or len(text.strip()) == 0:
        return "No text provided to summarize."
    
    # Split into sentences
    import re
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    
    if len(sentences) <= max_sentences:
        return text  # Already short enough
    
    # Pick first, middle, and last sentences as key points
    key_sentences = []
    key_sentences.append(sentences[0])  # Introduction
    
    if max_sentences >= 2:
        mid = len(sentences) // 2
        key_sentences.append(sentences[mid])  # Middle key point
    
    if max_sentences >= 3:
        key_sentences.append(sentences[-1])  # Conclusion
    
    return " ".join(key_sentences)


def break_down_task(task: str) -> list:
    """
    Breaks a high-level task into smaller actionable steps.
    
    Args:
        task: Description of the task
    Returns:
        List of step strings
    """
    # This is a simplified heuristic-based breakdown
    # In production, this would call an LLM
    steps = [
        f"Step 1: Understand and define the goal — '{task}'",
        "Step 2: Research and gather required information or resources",
        "Step 3: Create a plan with milestones and deadlines",
        "Step 4: Execute the plan step by step",
        "Step 5: Review, test, and validate the outcome",
        "Step 6: Document findings and present results"
    ]
    return steps


def get_task_plan(task: str) -> str:
    """
    Returns a formatted task plan for the given task.
    
    Args:
        task: Task description
    Returns:
        Formatted plan as string
    """
    steps = break_down_task(task)
    plan = f"📋 Task Plan for: {task}\n" + "─" * 40 + "\n"
    for step in steps:
        plan += f"  ✅ {step}\n"
    return plan
