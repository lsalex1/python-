from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO(r"yolo11n.pt")
    model.train(data=r"african-wildlife.yaml", epochs=30,
                imgsz=640,
                batch=2,
                cache=False,
                workers=0,
                #val = False, #这个参数是用来关闭验证集的
                )