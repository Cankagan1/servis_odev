import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanSunucu(Node):
    def __init__(self):
        super().__init__('alan_sunucu')
        self.srv = self.create_service(
            RectangleArea, 'rectangle_area', self.alan_hesapla_callback
        )
        self.get_logger().info('RectangleArea servisi hazir ve istek bekliyor...')

    def alan_hesapla_callback(self, request, response):
        if request.width <= 0.0 or request.height <= 0.0:
            response.area = 0.0
            response.success = False
            self.get_logger().warn(
                f'Gecersiz boyutlar reddedildi: width={request.width}, height={request.height}'
            )
        else:
            response.area = request.width * request.height
            response.success = True
            self.get_logger().info(
                f'Istek: width={request.width}, height={request.height} -> Alan: {response.area}'
            )
        return response


def main(args=None):
    rclpy.init(args=args)
    dugum = AlanSunucu()
    rclpy.spin(dugum)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
