import numpy as np
import cv2
import torch
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import PoseStamped
import os

# 加载本地的模型文件

# 可以使用自己训练的模型来替换
model_weights_path = os.getcwd()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 加载模型并将其移动到GPU
model = torch.hub.load(model_weights_path, 'custom', 'best.pt', source='local').to(device)

bridge = CvBridge()

def dectshow(org_img, boxs):
    img = org_img.copy()
    for box in boxs:
        # 绘制边界框
        cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        # 显示类别和中心点坐标
        cv2.putText(img, f"{box[-1]} ({int((box[0]+box[2])/2)}, {int((box[1]+box[3])/2)})", 
                    (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('detect_img', img)
    cv2.waitKey(1)

def detect_image_callback(msg):
    try:
        # 将ROS图像消息转换为OpenCV格式
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        # 在这里可以对cv_image进行进一步处理
        # 调节图片的大小
        cv_image = cv2.resize(cv_image, (640, 640))
        # 转变为yolo所需要的格式
        color_image = np.asanyarray(cv_image)

        # 将图像数据移动到GPU
        color_image = torch.from_numpy(color_image).permute(2, 0, 1).unsqueeze(0).float().to(device)

        # 运行模型以获取结果
        results = model(color_image)
        print(results)
        
        # boxes = results[0]['boxes']  # 提取边界框坐标信息
        # scores = results[0]['scores']  # 提取置信度分数
        # labels = results[0]['labels']  # 提取目标类别

        # print(boxes)

        # if len(boxes) == 0:
        #     print("[error]: 一个目标都没有识别到")
        # else:
        #     position_x = int((boxes[0][0] + boxes[0][2]) / 2)
        #     position_y = int((boxes[0][1] + boxes[0][3]) / 2)
        #     print("置信度最高的中心点的坐标为:", (position_x, position_y))
        #     position_msg = PoseStamped()
        #     position_msg.header.stamp = rospy.Time.now()
        #     position_msg.pose.position.x = position_x
        #     position_msg.pose.position.y = position_y
        #     position_msg.pose.position.z = 0
        #     result_publisher.publish(position_msg)
        # dectshow(cv_image, boxes)

    except CvBridgeError as e:
        rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('yolov5_ros_node')
    image_topic = "/prometheus/sensor/monocular_front/image_raw"
    result_topic = "/object_detection_results"

    # 创建一个发布器，发布检测结果//置信度最高的图像信息x,y
    result_publisher = rospy.Publisher(result_topic, PoseStamped, queue_size=10)
    # 创建一个订阅器，订阅图像话题
    rospy.Subscriber(image_topic, Image, detect_image_callback)
    rospy.spin()
