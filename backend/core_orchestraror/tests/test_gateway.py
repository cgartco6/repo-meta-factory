import os
import json
import pytest
from ..gateway import HITLGatewayInterceptor

def test_hitl_state_interceptor_mutation(tmp_path):
    # Setup standard simulation workspace structure
    test_graph = tmp_path / "dependency_graph.json"
    initial_data = {
        "modules": {
            "core_orchestrator": {"status": "PENDING", "last_error": None}
        }
    }
    test_graph.write_text(json.dumps(initial_data))
    
    interceptor = HITLGatewayInterceptor(graph_path=str(test_graph))
    interceptor.intercept_and_pause("core_orchestrator", "AssertionError: Element out of bounds")
    
    updated_data = json.loads(test_graph.read_text())
    assert updated_data["modules"]["core_orchestrator"]["status"] == "HEALING_CODE"
    assert "Element out of bounds" in updated_data["modules"]["core_orchestrator"]["last_error"]
