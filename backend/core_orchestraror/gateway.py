import json
import os

class HITLGatewayInterceptor:
    def __init__(self, graph_path: str = "../dependency_graph.json"):
        self.graph_path = graph_path

    def intercept_and_pause(self, module_id: str, error_message: str = None):
        """Halts automation pipelines until an operator clears the task"""
        if not os.path.exists(self.graph_path):
            return
        with open(self.graph_path, "r") as f:
            graph = json.load(f)
            
        if module_id in graph["modules"]:
            graph["modules"][module_id]["status"] = "HEALING_CODE" if error_message else "PENDING"
            if error_message:
                graph["modules"][module_id]["last_error"] = error_message
                
        with open(self.graph_path, "w") as f:
            json.dump(graph, f, indent=2)
