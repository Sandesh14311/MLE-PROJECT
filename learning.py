from printind.printind_function import printi, printiv
from env import resume_env, nb_actuations


import os
import numpy as np
from tensorforce.agents import PPOAgent
from tensorforce.execution import Runner

# Import environment and define network specifications
from env import resume_env, nb_actuations
environment = resume_env(plot=False, step=50, dump=100)
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
    distributions=None,
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
    execution=dict(
        type='single',
        session_config=None,
        distributed_spec=None
    )
)

# Restore saved model if it exists
if(os.path.exists('saved_models/checkpoint')):
    restore_path = './saved_models'
else:
    restore_path = None

if restore_path is not None:
    print("Restoring saved model...")
    agent.restore_model(restore_path)

# Define runner with episode_finished function to save the model after each episode and print some statistics
def episode_finished(r):
    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,
                                                                                 reward=r.episode_rewards[-1]))
    # Save the model after each episode
    name_save = "./saved_models/ppo_model"
    agent.save_model(name_save, append_timestep=False)

    return True

# Define and execute runner for a specified number of episodes with a maximum number of timesteps per episode
print("Starting learning...")
runner = Runner(agent=agent, environment=environment)
runner.run(episodes=2000, max_episode_timesteps=nb_actuations, episode_finished=episode_finished)
runner.close()

# Print statistics
print("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(
    ep=runner.episode,
    ar=np.mean(runner.episode_rewards[-100:])
))

