import cv2
import mediapipe as mp

class HandTracker:
    # def __init__(self, mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
    #     self.mode = mode
    #     self.max_num_hands = max_num_hands
    #     self.min_detection_confidence = min_detection_confidence
    #     self.min_tracking_confidence = min_tracking_confidence

    #     self.mp_draw = mp.solutions.drawing_utils
    #     self.mp_hand = mp.solutions.hands
    #     self.hand = self.mp_hand.Hands(self.mode, self.max_num_hands, self.min_detection_confidence, self.min_tracking_confidence)

    def __init__(self):
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_hand = mp.solutions.hands

    def track_hands(self):
         cap = cv2.VideoCapture(0)

         with self.mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:

            while True:
                ret, image = cap.read()
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmark in results.multi_hand_landmarks:
                        self.mp_draw.draw_landmarks(image, hand_landmark, self.mp_hand.HAND_CONNECTIONS)
                cv2.imshow("Frame", image)
                k = cv2.waitKey(1)

                if k == ord('q'):
                    break
        
         cap.release()
         cv2.destroyAllWindows()