import threading
import rclpy
from rclpy.node import Node
from task_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('node1_string_publisher')
        self.pub = self.create_publisher(RT2String, '/rt2string', 10)
        self.current = None
        self.lock = threading.Lock()
        self.timer = self.create_timer(1.0, self.publish_current)  # publish every 1 s
        self.get_logger().info('Node 1 started. Type a string and press Enter (Ctrl+C to quit).')

    def set_string(self, text):
        with self.lock:
            self.current = text
        self.get_logger().info(f'Now publishing continuously: "{text}"')

    def publish_current(self):
        with self.lock:
            text = self.current
        if text is None:
            return
        msg = RT2String()
        msg.data = text
        self.pub.publish(msg)


def input_loop(node):
    # Runs in a separate thread so typing doesn't stop the publishing timer
    while rclpy.ok():
        try:
            text = input()
        except EOFError:
            break
        text = text.strip()
        if text:
            node.set_string(text)


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    threading.Thread(target=input_loop, args=(node,), daemon=True).start()
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
