import rclpy
from rclpy.node import Node

from custom_interfaces.srv import Exercise


class MathServer(Node):

    def __init__(self):
        super().__init__('math_server_node')
        self.srv = self.create_service(Exercise, 'calculator', self.add_two_ints_callback)

    def add_two_ints_callback(self, request: Exercise.Request, response: Exercise.Response):
        self.get_logger().info(f"Incoming request: {request.x} {request.op} {request.y}")
        if request.op in ["+", "-", "*"]:
            response.res = int(eval(f"{request.x}{request.op}{request.y}"))
            response.success = True
        else:
            response.res = -1
            response.success = False
        
        return response


def main():
    rclpy.init()
    minimal_service = MathServer()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()