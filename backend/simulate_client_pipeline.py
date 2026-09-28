import os
import json
import asyncio
from database import SessionLocal, init_cloud_db_tables, engine
from sqlalchemy import text
from branding_studio.agents import AutonomousBrandingStrategist
from branding_studio.schemas import OnboardingFormInput
from marketing_studio.copywriters import AgentMarketingCopywriter

async def run_live_simulation():
    print("🚀 INITIALIZING FULL SYSTEM INTEGRATION TEST SIMULATION...")
    
    # Force initialize the targeted Neon/Supabase or Local DB mappings
    try:
        init_cloud_db_tables()
        print("✅ Database connection layer validated.")
    except Exception as e:
        print(f"❌ Database error: {e}. Ensure your DATABASE_URL environment variable is set correctly.")
        return

    # Simulate front-end onboarding submission form data payload
    mock_input = OnboardingFormInput(
        company_name="Quantum Loom Automations",
        industry="Automated SaaS Infrastructure Solutions",
        target_audience="DevOps Teams and Engineering Directors",
        core_values=["Speed", "Security", "Scalability"]
    )

    # 1. Commit records to database instance
    db = SessionLocal()
    try:
        print(f"📝 Registering client '{mock_input.company_name}' into database profiles...")
        insert_query = text("""
            INSERT INTO agency_clients (company_name, industry, target_audience, tier)
            VALUES (:name, :ind, :aud, :tier)
        """)
        db.execute(insert_query, {
            "name": mock_input.company_name,
            "ind": mock_input.industry,
            "aud": mock_input.target_audience,
            "tier": "premium"
        })
        db.commit()
        print("✅ Client database record committed successfully.")
    except Exception as e:
        db.rollback()
        print(f"❌ Database commit failed: {e}")
        return
    finally:
        db.close()

    # 2. Trigger Module 1: Branding Studio Strategy Generation
    print("\n🧠 Activating Studio Module 1: Branding Strategist Agent...")
    branding_engine = AutonomousBrandingStrategist()
    blueprint = await branding_engine.execute_strategic_generation(mock_input)
    print(f"🔮 Result Archetype: {blueprint.archetype}")
    print(f"📋 Result Value Statement: {blueprint.competitive_positioning_statement}")

    # 3. Trigger Module 3: Marketing Studio Platform Copy blocks
    print("\n📢 Activating Studio Module 3: Marketing Copywriter Agent...")
    marketing_engine = AgentMarketingCopywriter()
    campaign_payload = await marketing_engine.construct_ad_variants(blueprint.competitive_positioning_statement)
    print(f"📱 Generated LinkedIn Campaign Copy:\n   '{campaign_payload['linkedin']}'")

    print("\n🏆 END-TO-END PIPELINE SIMULATION COMPLETED SUCCESSFULY WITHOUT HARDWARE DELAYS.")

if __name__ == "__main__":
    # Ensure system modules are discoverable locally across parent folders
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    asyncio.run(run_live_simulation())
