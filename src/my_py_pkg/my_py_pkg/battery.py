#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interface.srv import SetLed
from functools import partial
import time


class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")
        self.get_logger().info('battery_node has been started.')
        self.declare_parameter("led_panel_state", 0)
        
        self.led_panel = self.get_parameter("led_panel_state").value

        # while True:
        #     self.call_battery_server(3, True)
        #     time.sleep(4)
        #     self.call_battery_server(3, False)
        #     time.sleep(6)
        
        self.battery_state = "full"
        self.last_time_battey_state_changed_ = self.get_current_time_seconds()
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)

    def get_current_time_seconds(self):
        secs, nsecs = self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs / 1000000000.0
    
    def check_battery_state(self):
        time_now = self.get_current_time_seconds()
        if self.battery_state == "full":
            if time_now - self.last_time_battey_state_changed_ > 4.0:
                self.battery_state = "empty"
                self.get_logger().info("Battery is empty! Charging battery...")
                self.last_time_battey_state_changed_ = time_now
                self.call_set_led_server(3, self.led_panel)
        else:
            if time_now - self.last_time_battey_state_changed_> 6.0:
                self.battery_state = "full"
                self.get_logger().info("Battery is now full again.")
                self.last_time_battey_state_changed_ = time_now
                self.call_set_led_server(3, self.led_panel)

    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().info('Waiting for server led_state...')
      
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_battery_server, led_number=led_number, state=state))
    
    def callback_call_battery_server(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info(str(led_number) + " + " + str(state) + " + " + str(response.success))
        except Exception as e:
            self.get_logger().error("Service Call Failed %r" %(e,))

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()