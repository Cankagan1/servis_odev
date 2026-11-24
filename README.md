# RectangleArea ROS 2 Servisi

## Derleme ve Çalıştırma Komutları

```bash
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash

# Sunucuyu başlatma
ros2 run alan_py server

# İstemci ile test
ros2 run alan_py client 5.0 4.0

# Terminalden doğrudan servis çağrısı
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.5, height: 2.0}"

#terminalden service call çağrısı
waiting for service to become available...
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.5, height=2.0)

response:
alan_interfaces.srv.RectangleArea_Response(area=13.0, success=True)
