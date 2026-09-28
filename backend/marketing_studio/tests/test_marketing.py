import pytest
from ..copywriters import AgentMarketingCopywriter

@pytest.mark.asyncio
async def test_copywriting_agent_variant_generation():
    writer = AgentMarketingCopywriter()
    variants = await writer.construct_ad_variants("Continuous automated software optimization.")
    assert "linkedin" in variants
    assert "instagram" in variants
    assert "✨" in variants["instagram"]
