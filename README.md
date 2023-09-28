# ros-yolov5-OKEY

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
python3 laq_debug_cpu.py
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 04 数据集的制作与标注
https://roboflow.com/?ref=ultralytics

## 05 训练


```
python3 train.py --img 640 --epochs 3 --data coco128.yaml --weights yolov5s.pt
```
1. **`python train.py`**：这是要运行的训练脚本的命令。
2. **`-img 640`**：此参数指定了训练时输入图像的大小。在这种情况下，图像将被调整为 640x640 像素的大小。通常，您可以根据自己的数据集和硬件资源来选择适当的图像大小。
3. **`-epochs 3`**：这个参数设置了训练的轮数，即要运行多少个完整的训练周期。在这里，训练将运行 3 个周期。您可以根据需要增加或减少训练轮数，以获得更好的模型性能。
4. **`-data coco128.yaml`**：此参数指定了数据集的配置文件。**`coco128.yaml`** 文件应该包含有关数据集的信息，例如数据集的类别、训练和验证图像的路径等。这个配置文件用于告诉训练脚本如何加载和处理数据。
5. **`-weights yolov5s.pt`**：这个参数用于指定要加载的预训练权重文件，这些权重将用作模型的初始权重。在这里，**`yolov5s.pt`** 是一个预训练的 YOLOv5 小型模型的权重文件。通过加载预训练权重，您可以加速模型的训练过程，并在更小的数据集上进行有效的微调。