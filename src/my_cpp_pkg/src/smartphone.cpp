#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class Smartphone : public rclcpp::Node // MODIFY NAME
{
public:
    Smartphone() : Node("smartphone") // MODIFY NAME
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>("robot_news_cpp", 10,
                                                                                 std::bind(&Smartphone::callback_robot_news, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Smartphone has been started");
    }

private:
    void callback_robot_news(const example_interfaces::msg::String::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Smartphone>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}