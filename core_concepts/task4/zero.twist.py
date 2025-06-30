import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, ReliabilityPolicy

class ZeroTwist(Node):
    def __init__(self, node_name='zero_twist'):
        super().__init__(node_name)

        qos_profile = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE
        )

        self.publisher_ = self.create_publisher(
            msg_type=Twist,
            topic='twist',
            qos_profile=qos_profile
        )

        self.subscription_ = self.create_subscription(
            msg_type=String,
            topic='is_stopped',
            callback=self.stop_callback,
            qos_profile=qos_profile
        )

    # Callback function to handle incoming 'is_stopped' messages
    def stop_callback(self, msg: String):
        # If message content is "true" (case insensitive)
        if msg.data.lower() == 'true':
            zero_twist = Twist()                            # All fields initialized to 0.0 by default
            self.publisher_.publish(zero_twist)
            self.get_logger().info("Received stop signal. Published zero Twist.")


def main(args=None):
    rclpy.init()
    node = ZeroTwist()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
