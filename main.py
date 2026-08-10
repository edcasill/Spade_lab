import asyncio
from spade_bdi.bdi import BDIAgent


async def main():
    # agent with JID, password, AgentSpeak file
    ranger = BDIAgent("ranger@localhost", "p@tr0ll", "behaviour_test.asl")
    commander = BDIAgent("commander@localhost", "p@tr0ll", "commander.asl")

    # initialice agent
    await commander.start()
    await ranger.start()

    print("[SYSTEM] Agents connected to the net. Excecuting BDI reasoning")

    # this can set beliefs to the agent without using the speak file
    await asyncio.sleep(3)
    ranger.bdi.set_belief("Temperature", 20)

    ranger.bdi.remove_belief("battery_state")  # we can remove dinamically the beliefs of the ranger
    ranger.bdi.set_belief("battery_state", "low")  # set dinamically a belief on the agent

    # this retrieve the beliefs of the agent
    """
    curren_believe = ranger.bdi.get_belief("battery_state")
    all_beliefs = ranger.bdi.get_beliefs()
    """
    # this keeps alive the process, so teh agent has time to reason and execute an action
    await asyncio.sleep(5)

    # stop the agent
    await ranger.stop()
    await commander.stop()

    print("[SYSTEM] End of simulation")


if __name__ == "__main__":
    asyncio.run(main())
