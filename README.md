# ros-yolov5

订阅图像话题image_topic进行yolo识别，然后将置信度最高的那个矩形框的中心坐标以PoseStamped的数据格式发送出去result_topic

## 00 环境配置

```
cd ros-yolov5
pip3 install -r requirements.txt
```

## 01 首次测试，更改laq_debug.py文件中model的导入部分

```python
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.5
```

## 02 更改你所需要的图像话题的名称

```python
image_topic = "/camera/color/image_raw" 
```

## 03 运行脚本laq_debug

```
python3 laq_debug.py
```

