import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanIstemci(Node):
    def __init__(self):
        super().__init__('alan_istemci')
        self.cli = self.create_client(RectangleArea, 'rectangle_area')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')
        self.req = RectangleArea.Request()

    def istek_gonder(self, width, height):
        self.req.width = width
        self.req.height = height
        return self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print('Kullanim: ros2 run alan_py client <width> <height>')
        sys.exit(1)

    width = float(sys.argv[1])
    height = float(sys.argv[2])

    istemci = AlanIstemci()
    future = istemci.istek_gonder(width, height)
    rclpy.spin_until_future_complete(istemci, future)

    yanit = future.result()
    if yanit.success:
        istemci.get_logger().info(f'Basarili! Dikdortgen Alani: {yanit.area}')
    else:
        istemci.get_logger().error('Hata: Negatif veya gecersiz deger girildi!')

    istemci.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
