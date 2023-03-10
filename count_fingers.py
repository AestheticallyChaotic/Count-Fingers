import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)
tipIds = [4,8,12,16,20]

def countFingers(image,hand_landmarks,handNo = 0):
    
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        fingers = []
        
        for i in tipIds:
            finger_tip = landmarks[i].y
            finger_bottom = landmarks[i-2].y

            if i!=4:
                if finger_tip<finger_bottom:
                    fingers.append(1)
                if finger_tip > finger_bottom:
                    fingers.append(0)
                    
        total_fingers = fingers.count(1)

def drawHandLandmarks(image,hand_landmarks):

    if hand_landmarks:
        
        for landmarks in hand_landmarks:
            mp_drawings.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)

while True:
    success, image = cap.read()

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

