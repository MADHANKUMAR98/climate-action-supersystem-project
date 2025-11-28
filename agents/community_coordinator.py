from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import FunctionTool
from config import RETRY_CONFIG, GEMINI_MODEL, GOOGLE_API_KEY

class CommunityManager:
    """Manages community coordination and collective impact"""
    
    def create_community_challenge(self, challenge_type: str, goal: str) -> dict:
        """Create a community climate challenge"""
        challenges = {
            "transportation": "Collective 1000km of car-free travel",
            "energy": "Reduce household energy use by 20%", 
            "diet": "30 plant-based meals this month",
            "advocacy": "50 policy letters to representatives"
        }
        
        return {
            "status": "success",
            "challenge_name": f"Community {challenge_type.title()} Challenge",
            "goal": challenges.get(challenge_type, goal),
            "duration_days": 30,
            "participants": 12,  # Mock data
            "collective_impact": "Estimated 500kg CO2 reduction",
            "join_code": f"CLIMATE_{challenge_type.upper()}_{hash(challenge_type) % 1000:03d}"
        }
    
    def get_community_impact(self) -> dict:
        """Get collective community impact metrics"""
        return {
            "status": "success",
            "total_members": 47,
            "collective_co2_reduced_kg": 1250,
            "active_challenges": 3,
            "trees_planted": 57,
            "policy_letters_sent": 28,
            "community_rank": "Carbon Champion"
        }

# Create tools
community_manager = CommunityManager()
create_challenge_tool = FunctionTool(community_manager.create_community_challenge)
get_impact_tool = FunctionTool(community_manager.get_community_impact)

def create_community_coordinator_agent():
    agent = LlmAgent(
        model=Gemini(model=GEMINI_MODEL, retry_options=RETRY_CONFIG, api_key=GOOGLE_API_KEY),
        name="community_coordinator_agent",
        description="Specialized agent for community coordination and collective climate action",
        instruction="""
        You are a Community Climate Coordinator. Your role is to:
        
        1. Create engaging community challenges
        2. Track collective impact metrics
        3. Foster collaboration and motivation
        4. Show how individual actions create collective change
        
        Be encouraging and community-focused. Show the power of collective action.
        Create challenges that are achievable but meaningful.
        """,
        tools=[create_challenge_tool, get_impact_tool]
    )
    return agent

community_coordinator_agent = create_community_coordinator_agent()