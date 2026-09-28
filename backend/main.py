from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import json

from database import init_cloud_db_tables
from branding_studio.app import router as branding_router
from design_studio.app import router as design_router
from marketing_studio.app import router as marketing_router

app = FastAPI(
    title="Automated AI Agency Production Core Mesh",
    description="Stateless agent orchestration engine built for low-spec hardware validation.",
    version="1.0.0"
)

# Global Cross-Origin Resource Sharing (CORS) rules for easy Vercel front-end binding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect standalone modular routers to the central API core matrix
app.include_router(branding_router)
app.include_router(design_router)
app.include_router(marketing_router)

GRAPH_FILE = "../dependency_graph.json"

@app.on_event("startup")
def on_startup():
    try:
        init_cloud_db_tables()
        print("🟢 Production Database Engines Connected cleanly.")
    except Exception as e:
        print(f"⚠️ Remote Database offline ({e}). Running inside local memory buffer.")

@app.get("/api/v1/factory/state")
def fetch_factory_state():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {"system_status": "OFFLINE", "global_score": 0, "modules": {}, "logs": []}

@app.post("/api/v1/factory/approve/{module_id}")
def verify_hitl_gateway_block(module_id: str):
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            graph = json.load(f)
        if module_id in graph.get("modules", {}):
            graph["modules"][module_id]["status"] = "LOCKED"
            graph["modules"][module_id]["progress"] = 100
            graph["modules"][module_id]["test_score"] = 100
            graph["logs"].insert(0, f"[HITL SUCCESS] Manual operator clearance confirmed for: {module_id}")
            with open(GRAPH_FILE, "w") as f:
                json.dump(graph, f, indent=2)
            return {"status": "SUCCESS", "target_locked": module_id}
    return {"status": "ERROR", "message": "Failed to update target matrix state."}
