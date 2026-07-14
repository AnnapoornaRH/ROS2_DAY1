# ROS2---INTERNSHIP

A beginner-friendly ROS 2 project demonstrating how to create a Python package, write a simple node, build the workspace, and run a **Hello World** program.

## Prerequisites

- Ubuntu
- ROS 2 Jazzy
- Python 3
- Colcon

## Project Structure

```
ROS2_DAY1/
├── src/
│   └── my_first_pkg/
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── my_first_pkg/
│           ├── __init__.py
│           └── my_first_node.py
```

## Steps

### 1. Create a Workspace

```bash
mkdir -p ~/ROS2_DAY1/src
cd ~/ROS2_DAY1
```

### 2. Create a Python Package

```bash
cd src
ros2 pkg create my_first_pkg --build-type ament_python --dependencies rclpy
```

### 3. Create the Node

```bash
cd my_first_pkg/my_first_pkg
touch my_first_node.py
chmod +x my_first_node.py
```

Add your Python node code and update `setup.py` with:

```python
'py_node = my_first_pkg.my_first_node:main'
```

### 4. Build the Package

```bash
cd ~/ROS2_DAY1
colcon build --symlink-install
```

### 5. Source the Workspace

```bash
source install/setup.bash
```

### 6. Run the Node

```bash
ros2 run my_first_pkg py_node
```

Expected output:

```
Hello World!
```

## Common Issues

- Ensure the node file is named **`my_first_node.py`**.
- Verify `__init__.py` exists in the package directory.
- Rebuild after making changes:
  ```bash
  colcon build --symlink-install
  ```
- Source the workspace after every build:
  ```bash
  source install/setup.bash
  ```

## Learning Outcomes

- Create a ROS 2 Python package
- Write and execute a Python node
- Build packages using `colcon`
- Run nodes using `ros2 run`
- Understand the basic ROS 2 package structure
