#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class CounterNode(Node):
    def __init__(self):
        super().__init__('number_counter')
        self.counter = 0
        self.server = self.create_service(SetBool, "reset_number_count", self.callback_reset_count)
        self.subscriptions_ = self.create_subscription(Int64, 'number', self.callback_number, 1)

        self.publishers_ = self.create_publisher(Int64, 'number_count', 10)
        self.timer_ = self.create_timer(0.5, self.count_publishers)

        self.get_logger().info('Counter node has been started.')

    def callback_number(self, msg):
        self.number = msg.data
        self.counter = self.counter + 1

    def count_publishers(self):
        msg = Int64()
        msg.data = self.counter
        self.publishers_.publish(msg)
    
    def callback_reset_count(self, request, response):
        if request.data:
            response.success = True
            response.message = "Number count reset successful."
            self.get_logger().info(response.message)
            self.counter = 0
        else:
            response.success = False
            response.message = "Number count reset failed."
            self.get_logger().error(response.message)
        
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = CounterNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

