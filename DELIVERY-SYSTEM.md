# ROSA TurtleSim Delivery System

This document explains how to use the new delivery system capabilities added to the ROSA TurtleSim.

## Overview

The delivery system allows the TurtleSim to navigate to predefined locations and simulate delivering items. This functionality demonstrates how ROSA can be used for simple task-based navigation in a ROS environment.

## Predefined Locations

The following locations are available for delivery:

| Location Name    | Coordinates (x,y) |
|------------------|-------------------|
| professor_room   | (3.0, 3.0)        |
| water_point      | (4.0, 8.0)        |
| laboratory1      | (5.0, 9.0)        |
| laboratory2      | (5.0, 8.0)        |

## Using the Delivery System

Start the TurtleSim with the web GUI:

```bash
WEB_GUI=true ./demo.sh
```

Once the web interface is loaded at http://localhost:5000, you can interact with the delivery system using natural language:

### Example Commands

- "What locations can you deliver to?"
- "Can you deliver this screwdriver to the lab?"
- "I need a water bottle delivered to the professor"
- "Take this report to laboratory2"
- "I'm thirsty, can you help me?"

### Interaction Flow

1. **Request**: Ask the TurtleBot to deliver an item to a location
2. **Confirmation**: The TurtleBot will confirm the destination before proceeding
3. **Navigation**: Upon confirmation, the TurtleBot will navigate to the location
4. **Completion**: The TurtleBot will confirm successful delivery

## Adding New Locations

To add or modify locations, edit the `locations` dictionary in `src/turtle_agent/scripts/tools/locations.py`:

```python
locations = {
    "new_location": (x_coordinate, y_coordinate),
    # Add more locations as needed
}
```

## Technical Implementation

The delivery system is implemented using:

1. **Location Database**: Stores named locations and coordinates
2. **Navigation Tools**: Uses existing teleport functionality to move the turtle
3. **Natural Language Understanding**: LLM interprets delivery requests and maps to destinations
4. **Confirmation Protocol**: Ensures user approval before executing deliveries

## Future Enhancements

Possible enhancements to this system could include:

- Multiple delivery points in sequence
- Delivery scheduling
- Return-to-base functionality
- Path planning with obstacle avoidance 