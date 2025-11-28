from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import FunctionTool
from config import RETRY_CONFIG, GEMINI_MODEL, GOOGLE_API_KEY

class OffsetManager:
    """Manages carbon offset purchases and tracking"""
    
    def purchase_carbon_offsets(self, co2_kg: float, offset_type: str = "reforestation") -> dict:
        """Purchase carbon offsets for the specified amount of CO2"""
        # In production, this would integrate with real offset providers
        cost_per_kg = 0.02  # $0.02 per kg CO2 for reforestation
        total_cost = co2_kg * cost_per_kg
        
        return {
            "status": "success",
            "co2_offset_kg": co2_kg,
            "offset_type": offset_type,
            "total_cost_usd": round(total_cost, 2),
            "transaction_id": f"OFFSET_{hash(str(co2_kg) + offset_type) % 10000:04d}",
            "message": f"Successfully offset {co2_kg}kg CO2 via {offset_type} for ${total_cost:.2f}"
        }
    
    def get_offset_portfolio(self) -> dict:
        """Get user's carbon offset portfolio"""
        return {
            "status": "success",
            "total_offset_kg": 125.5,  # Mock data
            "lifetime_cost_usd": 2.51,
            "projects_supported": ["Reforestation", "Renewable Energy"],
            "equivalent_trees": round(125.5 / 21.77, 2)
        }

# Create tools
offset_manager = OffsetManager()
purchase_offsets_tool = FunctionTool(offset_manager.purchase_carbon_offsets)
get_portfolio_tool = FunctionTool(offset_manager.get_offset_portfolio)

def create_offset_manager_agent():
    agent = LlmAgent(
        model=Gemini(model=GEMINI_MODEL, retry_options=RETRY_CONFIG, api_key=GOOGLE_API_KEY),
        name="offset_manager_agent",
        description="Specialized agent for managing carbon offset purchases and portfolio tracking",
        instruction="""
        You are a Carbon Offset Manager. Your role is to:
        
        1. Purchase carbon offsets when users want to neutralize emissions
        2. Track and report on offset portfolio
        3. Recommend optimal offset strategies
        4. Provide transparency on offset projects
        
        Always calculate costs clearly and explain the impact of offsets.
        Suggest reforestation for general purposes, renewable energy for energy emissions.
        """,
        tools=[purchase_offsets_tool, get_portfolio_tool]
    )
    return agent

offset_manager_agent = create_offset_manager_agent()