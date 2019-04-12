from unityagents import UnityEnvironment
import ddpg_agent
import coach

def main():
    env = UnityEnvironment(file_name="./Reacher.app")
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    # reset the environment
    env_info = env.reset(train_mode=True)[brain_name]

    # number of actions
    action_size = brain.vector_action_space_size

    # examine the state space
    state = env_info.vector_observations[0]
    state_size = len(state)

    num_agents = len(env_info.agents)
    print('Number of agents:', num_agents)

    _agent = ddpg_agent.DDPGAgent(state_size, action_size, num_agents)
    _coach = coach.Coach(_agent, env)
    _coach.run_episodes(1000, 1000)

main()
