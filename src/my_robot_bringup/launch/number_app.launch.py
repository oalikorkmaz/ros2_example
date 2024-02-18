from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    remap_number_topic = ("number", "my_number")

    number_publisher_node = Node(
        package="my_py_pkg", # paket adı
        executable="number_publisher", # Düğüm(Node) adı
        name="my_number_publisher", # düğümleri yeniden adlandırıyoruz.
        remappings=[ 
            remap_number_topic #topic isimlerini değiştirmek için kullanırız.
        ],
        parameters=[ # parametreleri vermek için kullanırız.
            {"number_to_publish": 4},
            {"publish_frequency": 5.0}
        ]
    )

    counter_node = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings=[
            remap_number_topic,
            ("number_count", "my_number_count")
        ]
    )

    ld.add_action(counter_node)
    ld.add_action(number_publisher_node)
    return ld