import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("HELLO WORLD")

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("HELLO WORLD")
    rclpy.spin(node)
    rclpy.shutdown()

    if __name__==" __main__":
        main()