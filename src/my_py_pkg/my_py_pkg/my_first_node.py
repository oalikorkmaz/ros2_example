#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2!!!")# Node print
        self.create_timer(0.5, self.timer_callback) 

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Hello {self.counter_}")

def main(args=None):
    rclpy.init(args = args) #Start
    node = MyNode() # Create py_test Node 
    rclpy.spin(node) # while 
    rclpy.shutdown() # End


if __name__ == "__main__":
    main()