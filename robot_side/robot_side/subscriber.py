import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_interfaces.msg import Special
from rclpy.qos import qos_profile_sensor_data

class Sub(Node):
    
    def __init__(self):
        super().__init__('subscriber')
        # self.create_subscription(String, "information", self.info_callback, qos_profile=qos_profile_sensor_data)
        self.create_subscription(Special, "special_for_all", self.special_callback, qos_profile=qos_profile_sensor_data)

    def info_callback(self, msg: String):        
        self.get_logger().info(f"got information: {msg.data}")

    def special_callback(self, msg: Special):        
        self.get_logger().info(f"got special message: {msg.a}, {msg.b}, {msg.c}")


def main():
    rclpy.init()
    node = Sub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()