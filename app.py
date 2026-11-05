
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class FlowPilotAgent:
    """A simple AI agent created with FlowPilot."""

    def __init__(self, name, instructions, model="gpt-4o-mini"):
        self.name = name
        self.instructions = instructions
        self.model = model

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.conversation = []

    def run(self, user_message):
        """Send a message to the AI agent."""

        self.conversation.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.instructions
                    },
                    *self.conversation
                ],
                temperature=0.7
            )

            answer = response.choices[0].message.content

            self.conversation.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except Exception as error:
            return f"Agent error: {error}"


# Create an AI agent using FlowPilot
support_agent = FlowPilotAgent(
    name="Customer Support Agent",
    instructions="""
    You are a helpful customer support AI agent.

    Your responsibilities:
    - Answer customer questions.
    - Explain products and services.
    - Help customers solve common problems.
    - Keep responses friendly and professional.
    """
)


# Run the agent
if __name__ == "__main__":

    print(f"\n🚀 {support_agent.name} is running!")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("FlowPilot Agent: Goodbye!")
            break

        response = support_agent.run(user_input)

        print(f"\n{support_agent.name}: {response}\n")

