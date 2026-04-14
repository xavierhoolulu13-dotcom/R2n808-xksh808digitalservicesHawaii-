from src.agents.writer import WriterAgent

def run(topic):
    agent = WriterAgent()
    return {
        "workflow": "content",
        "result": agent.run(topic)
    }
