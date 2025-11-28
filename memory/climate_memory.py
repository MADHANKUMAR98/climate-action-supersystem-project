class ClimateMemoryBank:
    """Long-term memory for climate actions and user preferences"""
    
    def __init__(self):
        self.user_profiles = {}
    
    async def save_climate_session(self, user_id: str, session_data: dict):
        """Save climate session data to long-term memory"""
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {}
        
        self.user_profiles[user_id].update(session_data)
        
        return {
            "status": "success", 
            "message": f"Climate profile saved for user {user_id}",
            "profile_snapshot": self.user_profiles[user_id]
        }
    
    async def get_climate_history(self, user_id: str):
        """Retrieve user's climate action history"""
        if user_id not in self.user_profiles:
            # Return default profile
            return {
                "total_emissions_tracked_kg": 0,
                "offsets_purchased_kg": 0,
                "policy_letters_sent": 0,
                "community_challenges_completed": 0,
                "preferred_transportation": "unknown",
                "energy_reduction_goal_percent": 10
            }
        
        return self.user_profiles[user_id]

# Memory instance
climate_memory = ClimateMemoryBank()

# Mock memory tools (in production, use actual ADK memory tools)
def save_memory_tool(user_id: str, data: dict):
    return climate_memory.save_climate_session(user_id, data)

def load_memory_tool(user_id: str):
    return climate_memory.get_climate_history(user_id)