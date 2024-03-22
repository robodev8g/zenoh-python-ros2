import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_interfaces.msg import Special
from rclpy.qos import qos_profile_sensor_data

class Pub(Node):

    
    def __init__(self):
        super().__init__('publisher')
        self.word_publisher = self.create_publisher(String, 'word', qos_profile=qos_profile_sensor_data)
        self.special_publisher = self.create_publisher(Special, 'special_only', qos_profile=qos_profile_sensor_data)
        self.timer = self.create_timer(1, self.send_special_message)
        self.counter = 0

    def send_word(self):
        msg = String()
        msg.data = f"Hello World: {self.counter}"
        self.word_publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.counter += 1
        
    def send_special_message(self):
        msg = Special()
        msg.a = 5
        msg.b = 2.4
        msg.c = "hyush"
        self.special_publisher.publish(msg)
        


def main():
    rclpy.init()
    node = Pub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()