import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from rclpy.qos import QoSProfile, ReliabilityPolicy


class PoseRepublisher(Node):
    def __init__(self, node_name='pose_re_pub'):
        super().__init__(node_name)
        

        qos_profile = QoSProfile(
            depth=10,                                 # queue size
            reliability=ReliabilityPolicy.RELIABLE    # ensure reliable delivery
        )

        
        self.subscriber_ = self.create_subscription(
            msg_type=PoseWithCovarianceStamped,
            topic='pose_with_covariance_stamped',
            callback=self.perception,             # calls self.perception() when a new message arrives
            qos_profile=qos_profile
        )


        self.publisher_ = self.create_publisher(
            msg_type=Pose,
            topic='pose',
            qos_profile=qos_profile
        )

    # Callback function:
    # - triggered whenever a new PoseWithCovarianceStamped message is received
    # - extracts just the pose (without covariance)
    def perception(self, msg: PoseWithCovarianceStamped):
        pose_only = msg.pose.pose  
        self.publisher_.publish(pose_only) 
        self.get_logger().info(f'Received and republished pose: {pose_only}')



def main(args=None):
    rclpy.init()
    node = PoseRepublisher()

    rclpy.spin(node)  # Keep the node running
    node.destroy_node()  # Cleanup
    rclpy.shutdown()


if __name__ == '__main__':
    main()
