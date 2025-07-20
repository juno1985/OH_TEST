

from agents.planner.main import PlannerAgent
import argparse

def main():
    parser = argparse.ArgumentParser(description="AI Agent System")
    parser.add_argument("task", type=str, help="Task description to execute")
    args = parser.parse_args()

    agent = PlannerAgent()
    result = agent.execute(args.task)
    
    print("\nExecution Result:")
    print(result)

if __name__ == "__main__":
    main()

