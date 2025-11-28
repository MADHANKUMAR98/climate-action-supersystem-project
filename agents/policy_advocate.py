from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import FunctionTool
from config import RETRY_CONFIG, GEMINI_MODEL, GOOGLE_API_KEY

class PolicyEngine:
    """Generates policy advocacy content and manages campaigns"""
    
    def generate_policy_letter(self, issue: str, recipient_type: str = "representative") -> dict:
        """Generate a policy advocacy letter for climate issues"""
        templates = {
            "representative": """
            Dear [Representative],
            
            I'm writing to urge stronger action on {issue}. As your constituent concerned about climate change, I believe we need:
            
            1. Immediate emissions reduction targets
            2. Investment in renewable energy infrastructure  
            3. Support for sustainable transportation
            
            My personal carbon tracking shows I've emitted {emissions}kg CO2 this month. I'm taking individual action, but systemic change is essential.
            
            Sincerely,
            [Your Name]
            """,
            "company": """
            Dear [Company Leadership],
            
            As a customer concerned about climate change, I urge {company} to:
            
            - Set science-based emissions targets
            - Transition to 100% renewable energy
            - Provide transparent carbon reporting
            
            My consumer choices are increasingly influenced by corporate climate action.
            
            Regards,
            [Your Name]
            """
        }
        
        return {
            "status": "success",
            "letter_template": templates.get(recipient_type, templates["representative"]).format(issue=issue, emissions=45.0),
            "recipient_type": recipient_type,
            "issue": issue,
            "next_steps": ["Personalize template", "Add your address", "Send via email/post"]
        }
    
    def track_policy_campaign(self, campaign_name: str) -> dict:
        """Track progress of policy advocacy campaigns"""
        return {
            "status": "success", 
            "campaign_name": campaign_name,
            "letters_sent": 3,  # Mock data
            "responses_received": 1,
            "impact_score": 75,
            "next_milestone": "Follow up in 2 weeks"
        }

# Create tools
policy_engine = PolicyEngine()
generate_letter_tool = FunctionTool(policy_engine.generate_policy_letter)
track_campaign_tool = FunctionTool(policy_engine.track_policy_campaign)

def create_policy_advocate_agent():
    agent = LlmAgent(
        model=Gemini(model=GEMINI_MODEL, retry_options=RETRY_CONFIG, api_key=GOOGLE_API_KEY),
        name="policy_advocate_agent", 
        description="Specialized agent for climate policy advocacy and campaign management",
        instruction="""
        You are a Climate Policy Advocate. Your role is to:
        
        1. Generate personalized policy advocacy letters
        2. Track advocacy campaign progress  
        3. Suggest strategic advocacy targets
        4. Connect personal emissions to policy needs
        
        Be persuasive but factual. Connect individual action to systemic change.
        Provide clear templates that users can personalize and send.
        """,
        tools=[generate_letter_tool, track_campaign_tool]
    )
    return agent

policy_advocate_agent = create_policy_advocate_agent()