from agent import Agent


def main():
    agent = Agent()

    print("Task Planner Assistant")
    user_input = input("Enter your study goal: ")

    result = agent.run(user_input)
    print()
    print(result)


if __name__ == "__main__":
    main()
