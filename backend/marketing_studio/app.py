from fastapi import APIRouter
from .copywriters import AgentMarketingCopywriter

router = APIRouter(prefix="/api/v1/marketing")
copywriter = AgentMarketingCopywriter()

@router.get("/generate-campaign")
async def generate_campaign_endpoint(brand_statement: str):
    return await copywriter.construct_ad_variants(brand_statement)
