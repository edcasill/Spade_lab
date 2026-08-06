import asyncio
from spade_bdi.bdi import BDIAgent


async def main():
    # agent with JID, password, AgentSpeak file
    agent = BDIAgent("ranger@localhost", "p@tr0ll", "behaviour_test.asl")

    # initialice agent
    await agent.start()

    print("Agent connected to the net. Excecuting BDI reasoning")

    # this can set beliefs to the agent without using the speak file
    await asyncio.sleep(3)
    agent.bdi.set_belief("Temperature", 20)

    agent.bdi.remove_belief("battery_state")
    agent.bdi.set_belief("battery_state", "low")
    
    # this retrieve the beliefs of the agent
    """
    curren_believe = agent.bdi.get_belief("battery_state")
    all_beliefs = agent.bdi.get_beliefs()
    """

    # we can remove dinamically the beliefs of the agent
    # agent.bdi.remove_belief("Temperature")

    # this keeps alive the process, so teh agent has time to reason and execute an action
    await asyncio.sleep(5)

    # stop the agent
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())