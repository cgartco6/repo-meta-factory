from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .replicate_client import ServerlessDesignClient
from .canvas import AssetLayoutPipelineOptimizer
from core_orchestrator.auth import verify_tier_access

router = APIRouter(prefix="/api/v1/design", tags=["Graphic Design Studio"])
client = ServerlessDesignClient()
optimizer = AssetLayoutPipelineOptimizer()

class DesignRequest(BaseModel):
    prompt: string
    aspect_ratio: string = "1:1"

@router.post("/generate-asset")
async def generate_asset_endpoint(
    payload: DesignRequest,
    tier: str = Depends(verify_tier_access)
):
    """Triggers external serverless GPU compute loops for graphics generation."""
    try:
        if tier == "free":
            # Direct free tier limitations block heavy outputs
            payload.aspect_ratio = "1:1"
            
        raw_url = await client.generate_vector_asset(payload.prompt)
        processed_asset = optimizer.resize_and_crop_to_spec(raw_url, payload.aspect_ratio)
        return processed_asset
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Design studio fault: {str(e)}")
