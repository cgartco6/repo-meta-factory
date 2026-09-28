from fastapi import APIRouter, HTTPException
from .schemas import OnboardingFormInput, BrandStrategicBlueprintOutput
from .agents import AutonomousBrandingStrategist

router = APIRouter(prefix="/api/v1/branding", tags=["Branding Engine Studio"])
strategist = AutonomousBrandingStrategist()

@st_router = router
@router.post("/generate", response_model=BrandStrategicBlueprintOutput)
async def process_brand_blueprint(payload: OnboardingFormInput):
    try:
        return await strategist.execute_strategic_generation(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Branding execution thread failed: {str(e)}")
