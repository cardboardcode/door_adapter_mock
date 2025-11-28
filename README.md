[![build](https://github.com/cardboardcode/door_adapter_template/actions/workflows/industrial_ci_action.yml/badge.svg)](https://github.com/cardboardcode/door_adapter_template/actions/workflows/industrial_ci_action.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

## **What Is This?**

A mock RMF Door Adapter that simulates the behaviour of a real door without the need to rely on external vendor-specific APIs.

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
[INFO] [launch]: All log files can be found below /root/.ros/log/2024-10-23-12-28-14-574052-rosi-0-1
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [mock_door_server-1]: process started with pid [59]
[INFO] [door_adapter_mock_node-2]: process started with pid [61]
[mock_door_server-1] [door_obj_array] door_id = door_1
[mock_door_server-1] [door_obj_array] door_id = door_2
[mock_door_server-1]  * Serving Flask app 'door_adapter_mock.mock_door_server'
[mock_door_server-1]  * Debug mode: on
[mock_door_server-1] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
[mock_door_server-1]  * Running on http://127.0.0.1:8888
[mock_door_server-1] Press CTRL+C to quit
[mock_door_server-1]  * Restarting with stat
[door_adapter_mock_node-2] [INFO] [1729686494.992788679] [door_adapter]: Starting door adapter...
[mock_door_server-1]  * Debugger is active!
[mock_door_server-1]  * Debugger PIN: 556-308-017
[mock_door_server-1] 127.0.0.1 - - [23/Oct/2024 12:28:15] "POST /system/ping HTTP/1.1" 200 -
[mock_door_server-1] 127.0.0.1 - - [23/Oct/2024 12:28:16] "POST /door/door_1/status HTTP/1.1" 200 -
[door_adapter_mock_node-2] [INFO] [1729686496.143892656] [door_adapter]: DoorState = DoorMode.MODE_CLOSED
[mock_door_server-1] 127.0.0.1 - - [23/Oct/2024 12:28:16] "POST /door/door_2/status HTTP/1.1" 200 -
[door_adapter_mock_node-2] [INFO] [1729686496.146284578] [door_adapter]: DoorState = DoorMode.MODE_CLOSED
[mock_door_server-1] 127.0.0.1 - - [23/Oct/2024 12:28:17] "POST /door/door_1/status HTTP/1.1" 200 -
[door_adapter_mock_node-2] [INFO] [1729686497.144141635] [door_adapter]: DoorState = DoorMode.MODE_CLOSED

```


## **References**

- https://osrf.github.io/ros2multirobotbook/integration_doors.html
- https://docs.python-requests.org/en/master/

[Back To Top of Page](#table-of-contents)