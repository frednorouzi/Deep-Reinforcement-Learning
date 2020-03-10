import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset() # The process gets started by calling reset(), which returns an initial observation.
    print(observation)
    total_reward=0

    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_reward = total_reward+reward
        print(observation)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Total Reward {}".format(total_reward))
            break

'''
The environment’s step function returns exactly what we need. In fact, step returns four values. These are:

observation (object): an environment-specific object representing your observation of the environment. For example, pixel data from a camera, joint angles and joint velocities of a robot, or the board state in a board game.
reward (float): amount of reward achieved by the previous action. The scale varies between environments, but the goal is always to increase your total reward.
done (boolean): whether it’s time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and done being True indicates the episode has terminated. (For example, perhaps the pole tipped too far, or you lost your last life.)
info (dict): diagnostic information useful for debugging. It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment’s last state change). However, official evaluations of your agent are not allowed to use this for learning.
This is just an implementation of the classic “agent-environment loop”. Each timestep, the agent chooses an action, and the environment returns an observation and a reward.
'''            