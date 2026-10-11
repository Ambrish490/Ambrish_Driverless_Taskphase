import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class Answerer(Node):
    def __init__(self):
        super().__init__('node3_answer')
        self.create_subscription(Int32, '/palindrome_result', self.callback, 10)
        self.answer_pub = self.create_publisher(String, '/palindrome_answer', 10)
        self.get_logger().info('Node 3 started. Waiting for 1/0 from Node 2...')

    def callback(self, msg):
        answer = 'Yes' if msg.data == 1 else 'No'
        out = String()
        out.data = answer
        self.answer_pub.publish(out)
        self.get_logger().info(f'Received {msg.data} from Node 2 -> sending "{answer}" back')


def main(args=None):
    rclpy.init(args=args)
    node = Answerer()
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
