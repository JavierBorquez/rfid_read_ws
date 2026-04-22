# RFID PubSub

A ROS 2 project for publishing and subscribing to RFID data over a ROS 2 topic.

## Overview

This project demonstrates a simple publisher-subscriber pattern using ROS 2:

- **Publisher** ([`rfid_publish.py`](src/rfid_pubsub/rfid_pubsub/rfid_publish.py)): Captures 10-digit RFID codes from keyboard input and publishes them to the `rfid_topic`
- **Subscriber** ([`subscriber_member_function.py`](src/rfid_pubsub/rfid_pubsub/subscriber_member_function.py)): Listens to the `rfid_topic` and logs received RFID codes to the console