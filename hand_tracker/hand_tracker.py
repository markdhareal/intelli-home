import cv2
import mediapipe as mp

class HandTracker:

    def __init__(self):
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_hand = mp.solutions.hands

    def track_hands(self):
         
         tip_ids = [4,8,12,16,20]

         cap = cv2.VideoCapture(0)

         with self.mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:

            while True:
                ret, image = cap.read()
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                land_mark_list = []
                if results.multi_hand_landmarks:
                    for hand_landmark in results.multi_hand_landmarks:
                        my_hands = results.multi_hand_landmarks[0]
                        for id, land_mark in enumerate(my_hands.landmark):
                            h, w, c = image.shape
                            coordinate_x, coordinate_y = int(land_mark.x * w), int(land_mark.y * h)
                            land_mark_list.append([id, coordinate_x, coordinate_y])
                        self.mp_draw.draw_landmarks(image, hand_landmark, self.mp_hand.HAND_CONNECTIONS)

                count_fingers = []
                if len(land_mark_list) != 0:
                    if land_mark_list[tip_ids[0]][1] > land_mark_list[tip_ids[0]-1][1]:
                        count_fingers.append(1)
                    else:
                        count_fingers.append(0)
                    for id in range(1,5):
                        if land_mark_list[tip_ids[id]][2] < land_mark_list[tip_ids[id]-2][2]:
                            count_fingers.append(1)
                        else:
                            count_fingers.append(0)

                    total_fingers = count_fingers.count(1)
                    print(total_fingers)
                cv2.imshow("Frame", image)
                k = cv2.waitKey(1)

                if k == ord('q'):
                    break
        
         cap.release()
         cv2.destroyAllWindows()