import rclpy
from rclpy.node import Node
from task_interfaces.msg import TaskOne


class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.subscription = self.create_subscription(
            TaskOne, '/taskone', self.callback, 10)
        self.get_logger().info('Subscriber started, waiting for data on /taskone...')

    def callback(self, msg):
        speed = msg.ang_vel * msg.radius   # v = omega * r
        self.get_logger().info(
            f'Received ang_vel={msg.ang_vel:.2f} rad/s, radius={msg.radius:.2f} m '
            f'-> Longitudinal speed v = {speed:.2f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
