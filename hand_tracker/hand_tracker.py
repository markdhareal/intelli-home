import cv2
import mediapipe as mp
from PIL import Image, ImageTk
import threading
from controller.arduino_controller import control

class HandTracker:

    def __init__(self, panel):
        self.panel = panel
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_hand = mp.solutions.hands
        self.cap = cv2.VideoCapture(0)
        self.thread = threading.Thread(target=self.track_hands)

    def finger_counter(self,list_for_land_mark):
        tip_ids = [4,8,12,16,20]
        count_fingers = []
        if len(list_for_land_mark) != 0:
            if list_for_land_mark[tip_ids[0]][1] > list_for_land_mark[tip_ids[0]-1][1]:
                count_fingers.append(1)
            else:
                count_fingers.append(0)
            for id in range(1,5):
                if list_for_land_mark[tip_ids[id]][2] < list_for_land_mark[tip_ids[id]-2][2]:
                    count_fingers.append(1)
                else:
                    count_fingers.append(0)

            total_fingers = count_fingers.count(1)
            control(total_fingers)
            print(total_fingers)

    def track_hands(self):

         with self.mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:

            while True:
                ret, image = self.cap.read()
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # image.flags.writeable = False
                # results = hands.process(image)
                # image.flags.writeable = True
                # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                land_mark_list = []

                if ret:
                    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                    if results.multi_hand_landmarks:
                        for hand_landmark in results.multi_hand_landmarks:
                            my_hands = results.multi_hand_landmarks[0]
                            for self.id, land_mark in enumerate(my_hands.landmark):
                                h, w, c = image.shape
                                coordinate_x, coordinate_y = int(land_mark.x * w), int(land_mark.y * h)
                                land_mark_list.append([id, coordinate_x, coordinate_y])
                            self.mp_draw.draw_landmarks(image, hand_landmark, self.mp_hand.HAND_CONNECTIONS)
                
                self.finger_counter(land_mark_list)

                if ret:
                    image = cv2.resize(image, (600, 400))
                    image = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
                    self.panel.configure(image=image)
                    self.panel.image = image

                k = cv2.waitKey(1)

                if k == ord('q'):
                    break

    def start(self):
        self.thread.start()