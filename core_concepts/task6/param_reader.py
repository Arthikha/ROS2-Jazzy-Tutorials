import rclpy
from rclpy.node import Node

class ParamReader(Node):
    def __init__(self):
        super().__init__('param_reader')
        robot_name = self.get_parameter_or('robot_name', 'unknown')
        self.get_logger().info(f"Robot name: {robot_name}")

def main(args=None):
    rclpy.init()
    node = ParamReader()
    rclpy.shutdown()
