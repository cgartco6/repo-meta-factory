from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .copywriters import AgentMarketingCopywriter
from .channels import DistributionChannelGateway

router = APIRouter(prefix="/api/v1/marketing", tags=["Marketing Engine Studio"])
copywriter = AgentMarketingCopywriter()
gateway = DistributionChannelGateway()

class CampaignRequest(BaseModel):
    brand_statement: str
    target_platform: str = "linkedin"

@router.post("/create-campaign")
async def create_campaign_endpoint(payload: CampaignRequest):
    """Generates platform copy blocks and tests distribution channel readiness."""
    try:
        variants = await copywriter.construct_ad_variants(payload.brand_statement)
        chosen_copy = variants.get(payload.target_platform, variants["linkedin"])
        
        # Verify media distribution pipeline health status
        is_ready = gateway.dispatch_mock_payload(payload.target_platform, chosen_copy)
        
        return {
            "platform": payload.target_platform,
            "copy": chosen_copy,
            "pipeline_dispatched": is_ready
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Marketing studio fault: {str(e)}")
