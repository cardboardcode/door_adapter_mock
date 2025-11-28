#!/usr/bin/env bash

CONFIG_FILE_PATH="/door_adapter_mock_ws/src/door_adapter_mock/configs/config.yaml"

docker run -it --rm \
    --name door_adapter_mock_c \
    --network host \
    -e RCUTILS_COLORIZED_OUTPUT=1 \
    -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
    -v ./door_adapter_mock/configs/config.yaml:$CONFIG_FILE_PATH \
door_adapter_mock:jazzy /bin/bash -c \
"source /ros_entrypoint.sh && ros2 launch door_adapter_mock run.launch.xml config_file:=$CONFIG_FILE_PATH"