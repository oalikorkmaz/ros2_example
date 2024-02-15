#include "rclcpp/rclcpp.hpp"
#include "my_robot_interface/msg/hardware_status.hpp"

class HardwareStatusPublisherNode : public rclcpp::Node
{
public:
    HardwareStatusPublisherNode() : Node("hardware_status_publisher")
    {
        publisher_ = this->create_publisher<my_robot_interface::msg::HardwareStatus>("hardware_status", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         std::bind(&HardwareStatusPublisherNode::publish_hw_status, this));

        RCLCPP_INFO(this->get_logger(), "Hardware status has been started.");
    }

private:
    void publish_hw_status()
    {
        auto msg = my_robot_interface::msg::HardwareStatus();
        msg.temperature = 45;
        msg.are_motors_ready = true;
        msg.debug_message = "Nothing special here";
        publisher_->publish(msg);
    }
    rclcpp::Publisher<my_robot_interface::msg::HardwareStatus>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HardwareStatusPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}