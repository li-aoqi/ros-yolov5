# from roboflow import Roboflow
# rf = Roboflow(api_key="hAOxxbzmPoh9Lua3xVZ6")
# project = rf.workspace("aoqi-li-ihhbf").project("target-car")
# dataset = project.version(1).download("yolov5")

# from roboflow import Roboflow
# rf = Roboflow(api_key="hAOxxbzmPoh9Lua3xVZ6")
# project = rf.workspace("aoqi-li-ihhbf").project("target-car")
# dataset = project.version(3).download("yolov5")

# from roboflow import Roboflow
# rf = Roboflow(api_key="hAOxxbzmPoh9Lua3xVZ6")
# project = rf.workspace("aoqi-li-ihhbf").project("target-car")
# dataset = project.version(4).download("yolov5")


from roboflow import Roboflow
rf = Roboflow(api_key="8yxhIW9U9qo9MmaIhQmw")
project = rf.workspace("maslab").project("circle_detector_for_702image")
dataset = project.version(2).download("yolov5")