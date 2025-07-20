

import os
import yaml
from typing import Dict, Any

class CIAgent:
    def handle_request(self, state: Dict[str, Any]) -> Dict[str, Any]:
        task = state["task"]
        try:
            if "setup" in task.lower() or "create" in task.lower():
                return self._setup_ci_pipeline()
            return {
                "status": "success",
                "message": "CI pipeline setup simulated (actual GitHub integration would require valid GITHUB_TOKEN)"
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }

    def _setup_ci_pipeline(self) -> Dict[str, Any]:
        """Simulate CI pipeline setup without actual GitHub API calls"""
        workflow_dir = ".github/workflows"
        os.makedirs(workflow_dir, exist_ok=True)
        
        workflow_config = {
            "name": "CI Pipeline",
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"uses": "actions/checkout@v4"},
                        {"name": "Set up Python", "uses": "actions/setup-python@v5"},
                        {"name": "Install dependencies", "run": "pip install -r requirements.txt"},
                        {"name": "Run tests", "run": "pytest"}
                    ]
                }
            }
        }

        with open(f"{workflow_dir}/ci.yml", "w") as f:
            yaml.dump(workflow_config, f)

        return {
            "status": "success",
            "message": "Created GitHub Actions workflow file",
            "workflow_file": "ci.yml"
        }
