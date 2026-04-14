from src.agents.planner import PlannerAgent

def run(goal):
    agent = PlannerAgent()
    return {
        "workflow": "planning",
        "result": agent.run(goal)
    }
