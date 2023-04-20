from printind.printind_function import printi, printiv
from env import resume_env, nb_actuations

import os
import numpy as np
from tensorforce.agents import PPOAgent
from tensorforce.execution import Runner

# Define environment and network specifications
environment = MyEnvironment()
network_spec = [
    dict(type='dense', size=512),
    dict(type='dense', size=512),
]

# Define PPO agent with hyperparameters for memory model, distribution model, policy gradient model, and PPO algorithm
agent = PPOAgent(
    states=environment.states,
    actions=environment.actions,
    network=network_spec,
    update_mode=dict(
        unit='episodes',
        batch_size=20,
        frequency=20
    ),
    memory=dict(
        type='latest',
        include_next_states=False,
        capacity=10000
    ),
    entropy_regularization=0.01,
    baseline_mode='states',
    baseline=dict(
        type='mlp',
        sizes=[32, 32]
    ),
    baseline_optimizer=dict(
        type='multi_step',
        optimizer=dict(
            type='adam',
            learning_rate=1e-3
        ),
        num_steps=5
    ),
    gae_lambda=0.97,
    likelihood_ratio_clipping=0.2,
    step_optimizer=dict(
        type='adam',
        learning_rate=1e-3
    ),
    subsampling_fraction=0.2,
    optimization_steps=25,
)

# Define runner with episode_finished function to save the model after each episode and print some statistics
def episode_finished(r):
    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,
                                                                                 reward=r.episode_rewards[-1]))
    # Save the model after each episode
    agent.save_model(directory='./saved_models', append_timestep=False)

    return True

runner = Runner(agent=agent, environment=environment)
runner.run(episodes=10000, max_episode_timesteps=1000, episode_finished=episode_finished)

# Print statistics
print("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(
    ep=runner.episode,
    ar=np.mean(runner.episode_rewards[-100:])
))

# Close runner and agent
runner.close()
agent.close()


