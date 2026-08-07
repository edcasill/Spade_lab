import asyncio
from spade_bdi.bdi import BDIAgent


async def main():
    # agent with JID, password, AgentSpeak file
    agent = BDIAgent("ranger@localhost", "p@tr0ll", "behaviour_test.asl")
    commander = BDIAgent("commander@localhost", "p@tr0ll", "commander.asl")

    # initialice agent
    await commander.start()
    await agent.start()

    print("Agent connected to the net. Excecuting BDI reasoning")

    # this can set beliefs to the agent without using the speak file
    await asyncio.sleep(3)
    agent.bdi.set_belief("Temperature", 20)

    agent.bdi.remove_belief("battery_state")  # we can remove dinamically the beliefs of the agent
    agent.bdi.set_belief("battery_state", "low")  # set dinamically a belief on the agent

    # this retrieve the beliefs of the agent
    """
    curren_believe = agent.bdi.get_belief("battery_state")
    all_beliefs = agent.bdi.get_beliefs()
    """
    # this keeps alive the process, so teh agent has time to reason and execute an action
    await asyncio.sleep(5)

    # stop the agent
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
