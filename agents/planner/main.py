
from typing import Literal
from langgraph.prebuilt import chat_agent_executor
from ..coding.agent import CodingAgent
from ..ci.agent import CIAgent

class PlannerAgent:
    def __init__(self):
        self.coding_agent = CodingAgent()
        self.ci_agent = CIAgent()
    
    def route_request(self, task: str) -> dict:
        return {"task": task}
    
    def decide_next_step(self, state: dict) -> Literal["coding", "ci"]:
        task = state["task"].lower()
        if "code" in task or "implement" in task or "test" in task:
            return "coding"
        elif "ci" in task or "pipeline" in task or "build" in task:
            return "ci"
        else:
            raise ValueError(f"Unknown task type: {task}")
    
    def execute(self, task: str):
        state = self.route_request(task)
        next_step = self.decide_next_step(state)
        
        if next_step == "coding":
            return self.coding_agent.handle_request(state)
        else:
            return self.ci_agent.handle_request(state)
