from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI(title="Automated Agency Gateway Core Mesh", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GRAPH_FILE = "../dependency_graph.json"

class SystemApprovalSchema(BaseModel):
    module_id: str
    approver: str = "Human-in-the-Loop Operator"

@app.get("/api/v1/factory/state")
def fetch_factory_state():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {"system_status": "OFFLINE", "global_score": 0, "modules": {}, "logs": []}

@app.post("/api/v1/factory/approve/{module_id}")
def verify_hitl_gateway_block(module_id: str):
    if not os.path.exists(GRAPH_FILE):
        raise HTTPException(status_code=404, detail="State matrix trace file unavailable")
    with open(GRAPH_FILE, "r") as f:
        graph = json.load(f)
        
    if module_id in graph.get("modules", {}):
        graph["modules"][module_id]["status"] = "LOCKED"
        graph["modules"][module_id]["progress"] = 100
        graph["modules"][module_id]["test_score"] = 100
        graph["logs"].insert(0, f"[HITL SUCCESS] Manual validation pass applied to: {module_id}")
        with open(GRAPH_FILE, "w") as f:
            json.dump(graph, f, indent=2)
        return {"status": "SUCCESS", "target_locked": module_id}
    raise HTTPException(status_code=400, detail="Target module identification token mismatch")
