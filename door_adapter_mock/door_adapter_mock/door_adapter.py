# Copyright 2024 Bey Hao Yun, Gary.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import yaml
import argparse

import rclpy
from rclpy.node import Node
from rmf_door_msgs.msg import DoorRequest, DoorState, DoorMode


class Door:
    def __init__(self, id):
        self.id = id
        self.door_mode = DoorMode.MODE_CLOSED

###############################################################################


class DoorAdapter(Node):
    def __init__(self, config_yaml):
        super().__init__('door_adapter_mock')
        self.get_logger().info('Initialising [door_adapter_mock]...')

        # Get value from config file
        self.door_state_publish_period = config_yaml['door_publisher']['door_state_publish_period']

        door_pub = config_yaml['door_publisher']
        door_sub = config_yaml['door_subscriber']

        # Add doors from config.yaml
        self.doors = {}
        for door_id in config_yaml['doors']:
            self.get_logger().info(f"Adding door [{door_id}]...")
            self.doors[door_id] = Door(door_id)

        self.door_states_pub = self.create_publisher(
            DoorState, door_pub['topic_name'], 100)

        self.door_request_sub = self.create_subscription(
            DoorRequest, door_sub['topic_name'], self.door_request_cb, 100)

        self.periodic_timer = self.create_timer(
            self.door_state_publish_period, self.timer_cb)

    def timer_cb(self):

        for door_id, door_data in self.doors.items():
            state_msg = DoorState()
            state_msg.door_time = self.get_clock().now().to_msg()
            # Publish states of the door
            state_msg.door_name = door_id
            state_msg.current_mode.value = door_data.door_mode
            self.door_states_pub.publish(state_msg)

    def door_request_cb(self, msg: DoorRequest):
        self.get_logger().warn(f"Door Request for [{msg.door_name}] to be mode [{msg.requested_mode.value}] - [TRIGGERED]")

        # Determine that requested door exists
        is_door_in_list = False
        for door_id, door_data in self.doors.items():
            if door_id == msg.door_name:
                is_door_in_list = True
                break

        if not is_door_in_list:
            self.get_logger().warn(f"Requested door [{msg.door_name}] is not in list...")
            self.get_logger().debug("Please ensure requested door matches what is defined in config.yaml...")
            self.get_logger().warn("Ignoring Door Request...")
            return
        else:
            # Update current door mode to what is being requested.
            self.doors[msg.door_name].door_mode = msg.requested_mode.value
            self.get_logger().info(f"Door [{msg.door_name}] is set to mode [{self.doors[msg.door_name].door_mode}] - [SUCCESS]")


###############################################################################


def main(argv=sys.argv):
    rclpy.init(args=argv)

    args_without_ros = rclpy.utilities.remove_ros_args(argv)
    parser = argparse.ArgumentParser(
        prog="door_adapter_mock",
        description="Configure and spin up door adapter for door ")
    parser.add_argument("-c", "--config_file", type=str, required=True,
                        help="Path to the config.yaml file for this door adapter")
    args = parser.parse_args(args_without_ros[1:])
    config_path = args.config_file

    # Load config and nav graph yamls
    with open(config_path, "r") as f:
        config_yaml = yaml.safe_load(f)

    door_adapter = DoorAdapter(config_yaml)
    rclpy.spin(door_adapter)

    door_adapter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main(sys.argv)
