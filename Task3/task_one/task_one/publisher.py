import rclpy
from rclpy.node import Node
from task_interfaces.msg import TaskOne


class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)
        self.get_logger().info('Publisher started. Enter values (Ctrl+C to quit).')

    def publish_from_input(self):
        try:
            ang_vel = float(input('Enter angular velocity (rad/s): '))
            radius = float(input('Enter wheel radius (m): '))
        except ValueError:
            self.get_logger().warn('Please enter numbers only.')
            return
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: ang_vel={ang_vel}, radius={radius}')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    try:
        while rclpy.ok():
            node.publish_from_input()
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
