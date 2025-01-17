import threading
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_check = False
#Pozivanje modela
def model_face_check(frame):
    global face_check
    face_check = True


while True:
    ret, frame = cap.read()

    if ret:
        #Mozemo uzimat vise/manje frame-ova ovisno kak nama pase
        if counter % 30 == 0:
            try: 
                threading.Thread(target=model_face_check, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_check:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
