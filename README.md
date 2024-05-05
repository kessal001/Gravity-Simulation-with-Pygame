
# Gravity Simulation with Pygame

This is a Python-based gravity simulation implemented using the Pygame library. The simulation demonstrates the orbital motion of various planets within the solar system interacting through the force of gravity.

## Overview

The simulation represents a simplified model of the solar system, where each planet is represented as a colored circle moving in response to gravitational forces exerted by other celestial bodies. The user can observe the dynamic interplay of gravitational forces and planetary orbits in a visually engaging manner.

## Usage

To run the simulation:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/gravity-simulation.git
    cd gravity-simulation
    ```

2. Ensure you have Python and Pygame installed on your system. You can install Pygame via pip:

    ```bash
    pip install pygame
    ```

3. Run the simulation script:

    ```bash
    python gravity_simulation.py
    ```

## Features

- **Sun**: The central body around which other planets orbit.
- **Planets**: Each planet is represented by a colored circle with its own mass, initial position, and velocity.
- **Realistic Orbital Motion**: The simulation calculates gravitational forces and updates the positions of planets based on Newton's law of universal gravitation.
- **Visualization**: Planetary orbits and distances from the sun are visually represented for easy observation.

## Adding a New Planet

To add a new planet to the simulation:

1. Open the `gravity_simulation.py` file in a text editor.
2. Locate the section where planets are initialized (`main()` function).
3. Instantiate a new `Planet` object with the desired parameters:

    ```python
    # Example: Adding a new planet named "Neptune"
    neptune = Planet(x_position, y_position, radius, color, mass)
    neptune.x_vel = initial_x_velocity
    neptune.y_vel = initial_y_velocity
    ```

4. Append the newly created planet object to the `planets` list:

    ```python
    planets.append(neptune)
    ```

5. Run the simulation, and the new planet will interact with existing planets according to gravitational forces.

## Contributions

Contributions of any kind are welcome! Whether it's improving the code, adding features, or fixing bugs, feel free to create issues or pull requests.
