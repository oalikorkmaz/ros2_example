#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Bool
from my_robot_interface.msg import LedStateArray
from my_robot_interface.srv import SetLed

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")

        self.led_states_ = [0, 0, 0]
        #self.led_panel_state = self.create_publisher(Bool, "set_panel_state", 1)
        self.led_states_publisher_ = self.create_publisher(LedStateArray, "led_states", 10)
        self.led_state_timer = self.create_timer(4, self.publish_led_states)

        
        #self.server = self.create_service(SetLed, "set_led", self.callback_battery)
        self.set_led_service_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.get_logger().info("Led panel node has been started.")



    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_publisher_.publish(msg)


    def callback_set_led(self, request, response):
        led_number = request.led_number
        state = request.state

        if led_number > len(self.led_states_) or led_number <= 0:
            response.success = False
            return response

        if state not in [0, 1]:
            response.success = False
            return response
        
        self.led_states_[led_number - 1] = state
        response.success = True
        self.publish_led_states()
        return response


    # def callback_battery(self, request, response): # callback_battery
    #     if request.state == False:
    #         response.success = True
    #         self.led_panel_state.publish(Bool(data=response.success))
    #     else:
    #         response.success = False
    #         self.led_panel_state.publish(Bool(data=response.success))
        
    #     self.get_logger().info(str(request.led_number) + " + " + str(request.state) + " + " + str(response.success))
    #     return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()