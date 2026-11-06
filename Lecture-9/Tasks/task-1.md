## Practice Question: Smart Home Assistant

### Problem Statement

You are developing a Smart Home Assistant that combines the functionalities of a Security System and a Home Entertainment System.

Create a Python program using multiple inheritance to implement the following classes.

### Class 1: SecuritySystem

Create a class named `SecuritySystem`.

Constructor:

- Accept `system_name` and `price` as parameters.
- Initialize the corresponding instance variables.
- `setup_date` assign current date 

Methods:

1. `activate_alarm()` – Display a message indicating that the security alarm is activated.
- Display the time at which alaram has been activated 
2. `check_door_status()` – Display a message indicating that the door is locked or unlocked.
3. `detect_motion()` – Display a message indicating that motion is being detected.

### Class 2: HomeEntertainment

Create a class named `HomeEntertainment`.

Constructor:

- Accept `system_name` and `price` as parameters.
- Initialize the corresponding instance variables.
- `setup_date` assign current date 

Methods:

1. `play_music(song)` – Display the name of the song being played.
2. `adjust_volume(level)` – Display the current volume level.
3. `connect_bluetooth(device)` – Display a message indicating that the device is connected through Bluetooth.

### Class 3: SmartHome

Create a class named `SmartHome` that inherits from both `SecuritySystem` and `HomeEntertainment`.

Constructor:

- Accept `system_name` and `price` as parameters.
- Initialize the parent classes using their constructors.
- `setup_date` assign current date 

Additional Methods:

1. `control_lights(status)` – Display whether the lights are turned ON or OFF.
2. `check_temperature()` – Display the current room temperature.

### Tasks

1. Create an object of the `SmartHome` class.
2. Call at least two methods from `SecuritySystem`.
3. Call at least two methods from `HomeEntertainment`.
4. Call both methods defined in `SmartHome`.
5. Display the `system_name` and `price` of the object.
6. Explain how the `SmartHome` class achieves multiple inheritance.

### Expected Object Creation

```
smart_home = SmartHome("Google Nest", 25000)
```

### Sample Output

```
Security Alarm Activated
Door is Locked
Playing music: Believer
Volume adjusted to 50
Lights are turned ON
Current room temperature is 25°C
```

### Challenge

Modify the program so that:

- Both parent classes have a method named `display_info()`.
- Each parent class displays its own information.
- In security Sytem `display_info_security_sys()`
- In Home Entertainment System `display_info_home_entertainment_sys()`

Concepts to practice: Multiple inheritance, constructors, instance variables, and method calls through child objects.