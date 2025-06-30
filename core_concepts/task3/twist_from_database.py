import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, ReliabilityPolicy

import csv


class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_from_database')

        qos_profile = QoSProfile(
            depth=10,                                 # queue size
            reliability=ReliabilityPolicy.RELIABLE    # ensure reliable delivery
        )


        self.publisher_ = self.create_publisher(
            msg_type=Twist,
            topic='twist_from_database',
            qos_profile=qos_profile
        )

        self.lines = self.load_csv('values.csv')

        # Index to track which line to publish
        self.index = 0

        # A timer to publish at 10 Hz (every 0.1 seconds)
        self.timer = self.create_timer(0.1, self.timer_callback)


    def load_csv(self, filename):
        try:
            with open(filename, 'r') as f:
                return list(csv.reader(f))
        except FileNotFoundError:
            self.get_logger().error(f"CSV file '{filename}' not found.")
            return []


    # Callback function triggered by the timer
    def timer_callback(self):
        if self.index < len(self.lines):
            try:
                # Convert string values to floats
                data = [float(x.strip()) for x in self.lines[self.index]]

                # Create and populate Twist message
                twist = Twist()
                twist.linear.x, twist.linear.y, twist.linear.z = data[0:3]
                twist.angular.x, twist.angular.y, twist.angular.z = data[3:6]

                # Publish the message
                self.publisher_.publish(twist)
                self.get_logger().info(f"Published line {self.index + 1}: {data}")

                # Move to next line
                self.index += 1
            except Exception as e:
                self.get_logger().error(f"Error processing line {self.index + 1}: {e}")
        else:
            self.get_logger().info("All CSV data published.")
            self.timer.cancel()  # Stop the timer after last line


def main(args=None):
    rclpy.init(args=args)

    node = TwistPublisher()

    rclpy.spin(node)  # Keep the node running
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()