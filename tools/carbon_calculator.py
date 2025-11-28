from typing import Dict
from google.adk.tools import FunctionTool

class CarbonCalculator:
    def __init__(self):
        self.emission_factors = {
            "car": 0.12, "bus": 0.05, "train": 0.03, "flight": 0.25,
            "electricity": 0.85, "natural_gas": 2.75,
        }
    
    def calculate_transportation(self, vehicle_type: str, distance_km: float, passengers: int = 1) -> Dict:
        """Calculate carbon emissions for transportation methods (car, bus, train, etc.)"""
        if vehicle_type.lower() not in self.emission_factors:
            return {"status": "error", "error_message": f"Unknown vehicle type: {vehicle_type}"}
        
        co2_kg = (distance_km * self.emission_factors[vehicle_type.lower()]) / passengers
        
        return {
            "status": "success",
            "co2_kg": round(co2_kg, 2),
            "equivalent_trees": round(co2_kg / 21.77, 2),
            "vehicle_type": vehicle_type,
            "distance_km": distance_km
        }
    
    def calculate_energy(self, energy_type: str, consumption: float) -> Dict:
        """Calculate carbon emissions for energy consumption (electricity, natural gas, etc.)"""
        if energy_type.lower() not in self.emission_factors:
            return {"status": "error", "error_message": f"Unknown energy type: {energy_type}"}
        
        co2_kg = consumption * self.emission_factors[energy_type.lower()]
        
        return {
            "status": "success",
            "co2_kg": round(co2_kg, 2),
            "energy_type": energy_type,
            "consumption": consumption
        }

# UPDATED: Correct FunctionTool syntax for current ADK version
calculator = CarbonCalculator()

carbon_calculator_transportation = FunctionTool(
    calculator.calculate_transportation  # Just pass the function directly
)

carbon_calculator_energy = FunctionTool(
    calculator.calculate_energy  # Just pass the function directly
)