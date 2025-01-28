import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

async def main() -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(
        model="llama3.2:1b",
        api_key="NotRequiredSinceWeAreLocal",
        base_url='http://host.docker.internal:11434/v1',
        model_capabilities={
            "json_output": False,
            "vision": False,
            "function_calling": True,
        }
        )
    )
    print(await agent.run(task="Say 'Hello World!'"))

asyncio.run(main())
