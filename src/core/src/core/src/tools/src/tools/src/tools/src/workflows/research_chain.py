from src.agents.researcher import ResearchAgent

def run(query):
    agent = ResearchAgent()
    return {
        "workflow": "research",
        "result": agent.run(query)
    }
