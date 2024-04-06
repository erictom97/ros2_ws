#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
from example_interfaces.srv import AddTwoInts
 
def main(args=None):
    rclpy.init(args=args)
    node = Node('add_two_ints_client_no_oop')
    client = node.create_client(AddTwoInts,'add_two_ints')
    while not client.wait_for_service(1.0):
        node.get_logger().warn('Waiting for add_two_ints server....')
        
    request = AddTwoInts.Request()
    request.a = 8
    request.b = 2
    
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    try:
        response = future.result()
        node.get_logger().info(f'{request.a} + {request.b} = {response.sum}')
    except Exception as e:
        node.get_logger().error(f'Server Call failed: {e}')
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()