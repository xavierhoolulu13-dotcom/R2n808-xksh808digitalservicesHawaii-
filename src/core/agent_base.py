class Agent:
    def __init__(self, name: str, role: str, tools: list = None):
        self.name = name
        self.role = role
        self.tools = tools or []

    def run(self, input_text: str) -> str:
        """
        Basic agent execution method.
        Override in child agents for custom behavior.
        """
        return f"[{self.name}] received: {input_text}"
