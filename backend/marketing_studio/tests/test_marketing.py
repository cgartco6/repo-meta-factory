import pytest
from copywriters import AgentMarketingCopywriter
from channels import DistributionChannelGateway

@pytest.mark.asyncio
async def test_copywriter_variant_generation_integrity():
    copywriter = AgentMarketingCopywriter()
    test_statement = "Disrupting traditional supply chain networks."
    
    variants = await copywriter.construct_ad_variants(test_statement)
    
    assert "linkedin" in variants
    assert "instagram" in variants
    assert "twitter" in variants
    assert test_statement in variants["linkedin"]

def test_distribution_gateway_validation():
    gateway = DistributionChannelGateway()
    
    # Empty payloads must be rejected cleanly by the engine
    assert gateway.dispatch_mock_payload("linkedin", "") is False
    # Valid copy strings must be cleared for social media delivery paths
    assert gateway.dispatch_mock_payload("linkedin", "Valid agency ad block text asset") is True
