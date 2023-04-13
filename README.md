# Active Flow Control of a 2D Cylinder using Deep Reinforcement Learning

This repository contains code for implementing a deep reinforcement learning algorithm to control the flow around a 2D circular cylinder. The objective is to minimize the drag force acting on the cylinder by manipulating the flow using an optimal control policy learned through reinforcement learning.

## Background

The study of flow around a cylindrical body is one of the classical fluid mechanics and flow control problems. Active flow control is a new and exciting area that has the potential to revolutionize industries that deal with wind turbines and aerospace vehicles. This project aims to use deep reinforcement learning to learn an optimal control policy that can manipulate the flow around a 2D circular cylinder, based on the approach described in the paper "Active flow control of a 2D cylinder using deep reinforcement learning" by Zhu et al. (2018).

## Getting Started

### Prerequisites

This project has the following dependencies:

- TensorFlow 1.8.0
- TensorForce 0.4.2
- Gmsh (version 3.+ but not 4.+)
- FEniCS (version 2017.1.0 or 2017.2.0)

### Credit

This code is based on the work of several researchers who have made significant contributions to the field of flow control using deep reinforcement learning. Specifically, this code is inspired by the following sources:

- Zhu et al. (2018). "Active flow control of a 2D cylinder using deep reinforcement learning". ArXiv:1808.07664 [cs.LG].
- Jerabaul29 (https://github.com/jerabaul29/Cylinder2DFlowControlDRL)
- Darshan Patel (https://github.com/darshan315/flow_past_cylinder_by_DRL).
- Shahzeb Aamir (https://github.com/ShahzebAamir/DRL-for-Active-Flow-Control).
- Fabian Gabriel (https://github.com/FabianGabriel/Active_flow_control_past_cylinder_using_DRL). 
- The paper "Active flow control of a circular cylinder using deep reinforcement learning" by Nakata et al. (2020) (https://doi.org/10.1063/1.5136859).
- The paper "Active flow control of a circular cylinder wake using deep reinforcement learning" by Shotorban et al. (2020)   (https://doi.org/10.1016/j.jfluidstructs.2020.103107).
If you use this code or any part of it in your research, please provide appropriate credit to the sources mentioned above and cite their original work.







































# MLE-PROJECT
Active Flow Control of a Circular Cylinder (2D)


Problem Statement


The study of flow around a cylindrical body is one of the classical fluid mechanics and flow control problems. The goal of this project is to develop a deep reinforcement learning (DRL)-based active flow control method for a 2D circular cylinder and evaluate its performance compared to existing methods. The project aims to use DRL to learn an optimal control phenomenon that can manipulate the flow around the cylinder. The use of DRL in controlling the flow around the cylinder is a new and exciting area, with potential applications in industries that deal with wind turbines and aerospace vehicles.

Literature Review

Several studies have been conducted in the area of flow control using DRL, some of which are referenced below:

Lu, Q., Huang, J., & Qin, N. (2020). Flow control with deep reinforcement learning: a review. Applied Mechanics Reviews, 72(2), 020802.

Shotorban, B., Malekzadeh, K., & Roshanian, J. (2020). Control of a circular cylinder wake using deep reinforcement learning. Journal of Fluids and Structures, 98, 103107.

Zhang, C., Wang, L., Li, Y., & Zhu, Z. (2021). DRLinFluids: An open-source Python platform of coupling deep reinforcement learning and OpenFOAM. Computer Physics Communications, 263, 107929.

Nakata, T., Fukami, K., & Morinishi, Y. (2020). Active flow control of a circular cylinder using deep reinforcement learning. Physics of Fluids, 32(1), 015112.
Duraisamy, K., Iaccarino, G., & Xiao, H. (2019). Reinforcement learning for flow control: A review of challenges and opportunities. Journal of Fluid Mechanics, 859, P1.


Data

The data for the project will be generated using computational fluid dynamics (CFD) simulations. Additionally, Sandesh may generate his own data using simulation software like OpenFOAM or the lattice Boltzmann method. Control inputs will be manipulated to achieve the desired flow control.

Methods and Algorithms

The project will use either the Deep Q-Networks (DQN) algorithm or Proximal Policy Optimization (PPO) algorithm. The algorithms will be modified to fit the requirements of the flow control problem. A noise will be introduced into the action space to help the agent learn a more effective control policy. A curriculum learning approach will also be considered, where there is a gradual increase in the complexity of the task to help learn a robust control policy. A multi-agent approach may also be used, where various agents are trained simultaneously to control various aspects of the flow.

Evaluation and Interpretation of Models

The model will be evaluated using the drag force, with the primary metric being the minimum drag coefficient. The project aims to produce animations for cases using flow control and without using flow control. Results obtained will be compared with different other flow control methods used previously to determine the effectiveness of the ML method in comparison to classical methods.
