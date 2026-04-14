from src.core.orchestrator import Orchestrator

def main():
    orch = Orchestrator()

    print("XAVIER MANUS LAB")
    print("1 = research")
    print("2 = content")
    print("3 = planning")

    choice = input("Select: ")
    text = input("Input: ")

    mapping = {"1": "research", "2": "content", "3": "planning"}
    workflow = mapping.get(choice)

    print(orch.run(workflow, text))

if __name__ == "__main__":
    main()
