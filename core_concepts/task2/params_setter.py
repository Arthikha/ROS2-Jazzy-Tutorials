import rclpy
from rclpy.node import Node


class ParamsSetter(Node):
    def __init__(self, node_name='params_setter'):
        super().__init__(node_name)

        self.param_name = 'robot_name'
        self.param_value = 'my_robot'

        self.declare_parameter(self.param_name, self.param_value)
        
        param_result = self.get_parameter(self.param_name).get_parameter_value().string_value
        self.get_logger().info(f"[{self.get_name()}] Set parameter: {self.param_name} = {param_result}")

def main(args=None):
    rclpy.init()
    node = ParamsSetter()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()