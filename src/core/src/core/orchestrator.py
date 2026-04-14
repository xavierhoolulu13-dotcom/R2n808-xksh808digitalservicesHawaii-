from src.agents.researcher import ResearchAgent
from src.agents.writer import WriterAgent
from src.agents.planner import PlannerAgent

from src.workflows.research_chain import run_research_chain
from src.workflows.content_chain import run_content_chain
from src.workflows.planning_chain import run_planning_chain


class Orchestrator:
    def __init__(self):
        self.agents = {
            "researcher": ResearchAgent(),
            "writer": WriterAgent(),
            "planner": PlannerAgent()
        }

    def run_workflow(self, workflow: str, input_text: str):
        if workflow == "research":
            return run_research_chain(input_text)
        if workflow == "content":
            return run_content_chain(input_text)
        if workflow == "planning":
            return run_planning_chain(input_text)

        return {"error": "Unknown workflow"}
