from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # robot_news_station_giskard = Node(
    #     package="my_py_pkg",
    #     executable="robot_news_station",
    #     remappings=[
    #         ("robot_news_station", "robot_news_station_giskard")
    #     ],
    #     parameters=[
    #         {"robot_name": "Giskard"}
    #     ]
    # )
    # robot_news_station_bb8 = Node(
    #     package="my_py_pkg",
    #     executable="robot_news_station",
    #     remappings=[
    #         ("robot_news_station", "robot_news_station_bb8")
    #     ],
    #     parameters=[
    #         {"robot_name": "BB8"}
    #     ]
    # )
    # robot_news_station_daneel = Node(
    #     package="my_py_pkg",
    #     executable="robot_news_station",
    #     remappings=[
    #         ("robot_news_station", "robot_news_station_daneel")
    #     ],
    #     parameters=[
    #         {"robot_name": "Daneel"}
    #     ]
    # )
    # robot_news_station_jander = Node(
    #     package="my_py_pkg",
    #     executable="robot_news_station",
    #     remappings=[
    #         ("robot_news_station", "robot_news_station_jander")
    #     ],
    #     parameters=[
    #         {"robot_name": "Jander"}
    #     ]
    # )
    # robot_news_station_c3po = Node(
    #     package="my_py_pkg",
    #     executable="robot_news_station",
    #     remappings=[
    #         ("robot_news_station", "robot_news_station_c3po")
    #     ]
    # )
    

    robot_names = ["Giskard", "BB8", "Daneel", "Jander", "C3PO"]

    robot_news_station_nodes = []

    for name in robot_names:
        robot_news_station_nodes.append(Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name = "robot_news_station_" + name.lower(),
            parameters=[{"robot_name": name}]
        ))

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smart_phone"
    )


    # ld.add_action(robot_news_station_giskard)
    # ld.add_action(robot_news_station_bb8)
    # ld.add_action(robot_news_station_daneel)
    # ld.add_action(robot_news_station_jander)
    # ld.add_action(robot_news_station_c3po)
    for node in robot_news_station_nodes:
        ld.add_action(node)
    ld.add_action(smartphone_node)
    return ld