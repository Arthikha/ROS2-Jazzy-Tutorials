from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

# Entry point to define what gets launched
def generate_launch_description():
    return LaunchDescription([
        
        # Launch the chatter node from 'tests' package
        Node(
            package='tests',              
            executable='chatter.py',      # Python script that publishes to /chatter
            name='test_chatter',          
            output='screen',              # Print output to terminal
            remappings=[('/chatter', '/test/chatter')]  # Remap /chatter → /test/chatter
        ),

        # Launch the listener node from 'tests' package
        Node(
            package='tests',              
            executable='listener.py',     # Python script that subscribes to /test/chatter
            name='listener',              
            output='screen',             
        ),


        # After a 2-second delay, run a command-line tool that publishes a single Twist msg
        TimerAction(
            period=2.0, 
            actions=[
                Node(
                    package='rclpy',     # Use rclpy tools
                    executable='rclpy_cli',  # ROS 2 CLI tool
                    arguments=[
                        'pub', '--once', '/twist', 'geometry_msgs/Twist',
                        '{"linear": {"x": 0.0, "y": 0.0, "z": 0.0}, "angular": {"x": 0.0, "y": 0.0, "z": 0.0}}'
                    ],
                    output='screen'
                )
            ]
        )
    ])
