import pytest
from ..schemas import OnboardingFormInput

def test_onboarding_schema_assertions():
    valid_payload = {
        "company_name": "AI Software Factory Corp",
        "industry": "Enterprise Automation Platforms",
        "target_audience": "Mid Market Technical Teams",
        "core_values": ["Speed", "Total Lockdown Security"]
    }
    model = OnboardingFormInput(**valid_payload)
    assert model.company_name == "AI Software Factory Corp"
    assert len(model.core_values) == 2
