[![build](https://github.com/cardboardcode/door_adapter_template/actions/workflows/industrial_ci_action.yml/badge.svg)](https://github.com/cardboardcode/door_adapter_template/actions/workflows/industrial_ci_action.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

## **What Is This?**

A **mock RMF Door Adapter** that simulates the behaviour of multiple doors without the need to rely on external vendor-specific APIs.

### **Build** :hammer:

Run the commands below to build `door_adapter_mock` in Docker:

1\. Build `door_adapter_mock`:

```bash
cd $HOME
```

```bash
git clone https://github.com/cardboardcode/door_adapter_mock --branch main --depth 1 --single-branch
```

```bash
cd door_adapter_mock
```

```bash
docker build -t door_adapter_mock:jazzy .
```

### **Run**

1\.. Run `door_adapter_mock`:

```bash
docker run -it --rm \
    --name door_adapter_mock_c \
    --network host \
    -e RCUTILS_COLORIZED_OUTPUT=1 \
    -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
    -v ./door_adapter_mock/configs/config.yaml:/door_adapter_mock_ws/src/door_adapter_mock/configs/config.yaml \
door_adapter_mock:jazzy /bin/bash -c \
"source /ros_entrypoint.sh && ros2 launch door_adapter_mock run.launch.xml config_file:=/door_adapter_mock_ws/src/door_adapter_mock/configs/config.yaml"
```

### **Verify**

Upon running the command above, you should see an output similar to what is shown below:

```bash
[INFO] [launch]: All log files can be found below /root/.ros/log/2025-11-28-16-37-11-186590-PC-RMF-DEV-2025-1
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [door_adapter_mock_node-1]: process started with pid [33]
[door_adapter_mock_node-1] [INFO] [1764347831.626209628] [door_adapter_mock]: Initialising [door_adapter_mock]...
[door_adapter_mock_node-1] [INFO] [1764347831.626631404] [door_adapter_mock]: Adding door [door1]...
[door_adapter_mock_node-1] [INFO] [1764347831.626980110] [door_adapter_mock]: Adding door [door2]...
...

```


## **References**

- https://osrf.github.io/ros2multirobotbook/integration_doors.html
- https://docs.python-requests.org/en/master/

[Back To Top of Page](#table-of-contents)