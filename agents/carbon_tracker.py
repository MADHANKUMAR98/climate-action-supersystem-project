from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from config import RETRY_CONFIG, GEMINI_MODEL, GOOGLE_API_KEY
from tools.carbon_calculator import carbon_calculator_transportation, carbon_calculator_energy

def create_carbon_tracker_agent():
    # ADD API KEY to Gemini configuration
    agent = LlmAgent(
        model=Gemini(
            model=GEMINI_MODEL, 
            retry_options=RETRY_CONFIG,
            api_key=GOOGLE_API_KEY  # ADD THIS LINE
        ),
        name="carbon_tracker_agent",
        description="Specialized agent for precise carbon footprint calculation and tracking",
        instruction="""
        You are a Carbon Footprint Analyst. Calculate emissions and suggest reductions.
        
        PROCESS:
        1. Identify carbon activities from user input
        2. Calculate emissions using tools
        3. Provide specific reduction suggestions
        
        Always use calculation tools. Be data-driven and practical.
        """,
        tools=[carbon_calculator_transportation, carbon_calculator_energy]
    )
    return agent

carbon_tracker_agent = create_carbon_tracker_agent()