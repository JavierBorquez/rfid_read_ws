import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pynput import keyboard

class RFIDPublisher(Node):

    def __init__(self):
        super().__init__('rfid_publisher')
        self.publisher_ = self.create_publisher(String, 'rfid_topic', 10)
        self.rfid_buffer = ""
        self.get_logger().info('RFID Publisher started. Ready to read 10-digit codes.')
        
        # Start listening to keyboard
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, key):
        try:
            # Capture digit keys only
            if key.char.isdigit():
                self.rfid_buffer += key.char
                self.get_logger().info(f'Buffer: {self.rfid_buffer}')
                
                # Publish when we have 10 digits
                if len(self.rfid_buffer) == 10:
                    msg = String()
                    msg.data = self.rfid_buffer
                    self.publisher_.publish(msg)
                    self.get_logger().info(f'Publishing RFID: "{msg.data}"')
                    self.rfid_buffer = ""
        except AttributeError:
            pass

    def destroy_node(self):
        self.listener.stop()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    rfid_publisher = RFIDPublisher()

    rclpy.spin(rfid_publisher)

    rfid_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()