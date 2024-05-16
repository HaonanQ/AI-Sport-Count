import cv2
from utils import *
import mediapipe as mp
from bodypartangle import BodyPartAngle
from typesofexercise import TypeOfExercise
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from keepsport import sport
from tkinter import filedialog
sports=["sit-up","pull-up","push-up","squat","walk"]

root = ttk.Window(
    title="AI运动分析",  # 设置窗口的标题
    themename="morph",  # 设置主题
    size=(460, 620),  # 窗口的大小
    resizable=None,  # 设置窗口是否可以更改大小
    alpha=1.0,  # 设置窗口的透明度(0.0完全透明）
    iconphoto="icon.png"
)
def get_file():
    filetypes = (
        ('vidoe files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='选择视频文件（mp4）类型',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        print(f"Selected file: {filename}")
        return filename
    pass

def b7():
    ttk.dialogs.dialogs.Messagebox.ok(title='提示', message='请提前打开摄像头，选择想要进行的体育活动让AI进行分析，退出分析按q键。\n'
                                     '如果选择智能对比练习，默认专业视频在data/video下，也可自行下载运动视频,'
                                    '刚刚进入时不会开始运动，而是先进行调节，双手合十才开始运动。退出练习按q键。\n'
                                    '智能对比练习动作成绩分为5个等级：\n''1.Great  2.Good  3.Normal  4.Not good  5.Bad\n'
                                      '点击其他按钮时会卡一会，程序正在加载，请耐心等待。')
def bt(flag):
    ## drawing body
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)  # webcam

    cap.set(3, 1200)  # width
    cap.set(4, 720)  # height

    ## setup mediapipe
    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:

        counter = 0  # movement of exercise
        status = True  # state of move
        while cap.isOpened():
            try:
                ret, frame = cap.read()
                # result_screen = np.zeros((250, 400, 3), np.uint8)

                frame = cv2.resize(frame, (1200, 720), interpolation=cv2.INTER_AREA)
                ## recolor frame to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame.flags.writeable = False
                ## make detection
                results = pose.process(frame)
                ## recolor back to BGR
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark
                    counter, status = TypeOfExercise(landmarks).calculate_exercise(
                        sports[flag], counter, status)
                except:
                    pass

                score_table(sports[flag], counter, status)

                ## render detections (for landmarks)
                mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(255, 255, 255),
                                           thickness=2,
                                           circle_radius=2),
                    mp_drawing.DrawingSpec(color=(174, 139, 45),
                                           thickness=2,
                                           circle_radius=2),
                )

                cv2.imshow('Video', frame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    print("counter: " + str(counter))
                    break
            except:
                print("err counter: " + str(counter))
                break

        cap.release()
        cv2.destroyAllWindows()
        ttk.dialogs.dialogs.Messagebox.ok(title='提示', message="本次练习（次）：" + str(counter))

    pass

root.place_window_center()    #让显现出的窗口居中
root.resizable(False,False)   #让窗口不可更改大小
ttk.Label(root,width=20).grid()

# 按钮
# 创建了一个匿名函数（lambda函数），当单选按钮被点击时，这个匿名函数会被调用，进而执行 bt(4)。
ttk.Label(root, text="AI运动分析", font=("微软雅黑", 26),bootstyle="primary").grid(row=3, column=0, sticky=ttk.W,padx=121, pady=30)
b1 = ttk.Radiobutton(root,name="b1", text="深蹲运动",width=20, bootstyle="outline-toolbutton",command=lambda:bt(3)).grid(row=9, column=0, sticky=ttk.W,padx=129, pady=15)
b2 = ttk.Radiobutton(root,name="b2",  text="引体向上",width=20, bootstyle="outline-toolbutton",command=lambda:bt(1)).grid(row=13, column=0, sticky=ttk.W,padx=129, pady=15)
b3 = ttk.Radiobutton(root,name="b3",  text="俯卧撑",width=20, bootstyle="outline-toolbutton",command=lambda:bt(2)).grid(row=17, column=0, sticky=ttk.W,padx=129, pady=15)
b4 = ttk.Radiobutton(root,name="b4",  text="仰卧起坐",width=20, bootstyle="outline-toolbutton",command=lambda:bt(0)).grid(row=21, column=0, sticky=ttk.W,padx=129, pady=15)
b5 = ttk.Radiobutton(root,name="b5",  text="步行",width=20, bootstyle="outline-toolbutton",command=lambda:bt(4)).grid(row=25, column=0, sticky=ttk.W,padx=129, pady=15)
b6 = ttk.Radiobutton(root,name="b6",  text="智能对比练习",width=20, bootstyle="outline-toolbutton",command=lambda:sport(get_file(),1)).grid(row=29, column=0, sticky=ttk.W,padx=129, pady=15)
b7 = ttk.Radiobutton(root,name="b7",  text="先点我看使用说明",width=20, bootstyle="outline-toolbutton",command=b7).grid(row=34, column=0, sticky=ttk.W,padx=129, pady=15)
root.mainloop()

