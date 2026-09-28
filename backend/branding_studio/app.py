from fastapi import APIRouter, HTTPException, Depends
from .schemas import OnboardingFormInput, BrandStrategicBlueprintOutput
from .agents import AutonomousBrandingStrategist
from core_orchestrator.auth import verify_tier_access

router = APIRouter(prefix="/api/v1/branding", tags=["Branding Engine Studio"])
strategist = AutonomousBrandingStrategist()

@router.post("/generate", response_model=BrandStrategicBlueprintOutput)
async def process_brand_blueprint(
    payload: OnboardingFormInput, 
    tier: str = Depends(verify_tier_access)
):
    """Processes strategic consumer insights according to tier permissions."""
    try:
        # Tiers adjust agent loop intensity limits
        if tier == "free" and len(payload.core_values) > 2:
            raise HTTPException(
                status_code=403, 
                detail="Free tier limit reached. Max 2 core values allowed."
            )
        return await strategist.execute_strategic_generation(payload)
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Branding studio fault: {str(e)}")
