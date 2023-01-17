from pettingzoo.butterfly import knights_archers_zombies_v10

env = knights_archers_zombies_v10.env(render_mode="human")
env.reset()
for agent in env.agent_iter():
    observation, reward, termination, truncated, info = env.last()
    if termination:
        env.step(None)
        print(f"Agent {agent} terminated")
    elif truncated:
        print("Truncated")
    else:
        action = env.action_space(agent).sample()
        env.step(action)
    
