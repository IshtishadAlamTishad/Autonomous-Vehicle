# Autonomous Vehicle  
**Developed Autonomous Vehicle using Webots and controlled by a CNN model**

[Demo Video](https://youtu.be/mcM9Ateer5I?si=Ds7jcd3WmixGMfo3)  

---

## Table of Contents  
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [System Architecture](#system-architecture)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Dataset Preparation](#dataset-preparation)  
   - [Model Training](#model-training)  
   - [Running the Simulation](#running-the-simulation)  
5. [Project Structure](#project-structure)  
6. [Usage](#usage)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)  

---

## Project Overview  
This project implements an autonomous vehicle simulation using the open-source robotics simulator Webots. The vehicle is controlled by a Convolutional Neural Network (CNN) that interprets the simulated environment and issues driving commands. The goal is to demonstrate end-to-end autonomy: from perception (camera input) to control (steering/throttle) in a virtual environment.

---

## Features  
- Realistic simulation of a mobile robot/vehicle in Webots.  
- CNN-based perception model for understanding road environment and generating control signals.  
- Modular and extensible architecture: dataset, models, simulation components separated.  
- Visualization of model architecture (see `model_architecture.png`).  
- Easy to extend for additional sensors, environments or control strategies.

---

## System Architecture  
The system comprises three main components:  
1. **Dataset Module** – Captures or uses pre-collected data of the vehicle driving in the Webots environment.  
2. **Model Module** – Defines, trains and validates the CNN model for driving control.  
3. **Simulation Module** – Runs the vehicle in Webots and deploys the trained model in real-time for autonomous control.

Below is a high-level schematic:  
![Model Architecture](model_architecture.png)

---

## Getting Started  

### Prerequisites  
- Python 3.x  
- Webots (version consistent with your environment)  
- Standard ML/deep-learning libraries: e.g., TensorFlow or PyTorch (depending on implementation)  
- Other dependencies listed in `requirements.txt` (create one if not present)  

### Installation  
```bash
git clone https://github.com/IshtishadAlamTishad/Autonomous-Vehicle.git  
cd Autonomous-Vehicle  
