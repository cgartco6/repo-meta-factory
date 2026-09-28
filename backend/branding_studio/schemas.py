from pydantic import BaseModel, Field
from typing import List

class OnboardingFormInput(BaseModel):
    company_name: str = Field(..., min_length=2)
    industry: str
    target_audience: str
    core_values: List[str]

class BrandStrategicBlueprintOutput(BaseModel):
    archetype: str
    voice_tone_guidelines: List[str]
    competitive_positioning_statement: str
