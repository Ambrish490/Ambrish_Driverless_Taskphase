import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from task_interfaces.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('node2_palindrome_checker')
        self.create_subscription(RT2String, '/rt2string', self.string_callback, 10)
        self.result_pub = self.create_publisher(Int32, '/palindrome_result', 10)
        self.create_subscription(String, '/palindrome_answer', self.answer_callback, 10)
        self.last_text = ''
        self.get_logger().info('Node 2 started. Waiting for strings on /rt2string...')

    def string_callback(self, msg):
        text = msg.data
        cleaned = text.replace(' ', '').lower()
        result = 1 if cleaned == cleaned[::-1] else 0   # 1 = palindrome, 0 = not
        self.last_text = text
        out = Int32()
        out.data = result
        self.result_pub.publish(out)
        self.get_logger().info(f'Received "{text}" -> sent {result} to Node 3')

    def answer_callback(self, msg):
        self.get_logger().info(f'Node 3 replied: {msg.data}   (for "{self.last_text}")')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
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
