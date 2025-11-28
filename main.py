"""
CLIMATE ACTION ORCHESTRATOR - MAIN ENTRY POINT
"""

import asyncio
from google.adk.runners import InMemoryRunner
from agents.carbon_tracker import carbon_tracker_agent

async def test_carbon_tracker():
    print("🚀 CLIMATE ACTION ORCHESTRATOR - INITIAL TEST")
    print("=" * 60)
    
    runner = InMemoryRunner(agent=carbon_tracker_agent)
    
    test_scenarios = [
        "I drove 25 kilometers to work in my car today",
        "My apartment used 45 kWh of electricity this week",
        "I took a bus for 15 kilometers to visit friends",
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n📊 TEST {i}: {scenario}")
        print("-" * 50)
        
        try:
            response = await runner.run_debug(scenario)
            print(f"✅ AGENT RESPONSE: {response}")
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 DAY 1 COMPLETED - READY FOR DAY 2")

if __name__ == "__main__":
    asyncio.run(test_carbon_tracker())