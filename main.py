import cv2
import htsilicon as ht
import math
import numpy as np
import applescript

cap = cv2.VideoCapture(0)
det = ht.ht()

while 1:
    suc, read = cap.read()

    read = det.findhand(read)

    lml = det.findpos()

    if len(lml) != 0:
        x1, y1 = lml[4][0], lml[4][1]
        x2, y2 = lml[8][0], lml[8][1]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(read, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(read, (x2, y2), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(read, (x1, y1), (x2, y2), (0, 0, 255), 5, cv2.FILLED)
        cv2.circle(read, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        if length < 50:
            cv2.circle(read, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        vol = np.interp(length, [50, 300], [0, 100])
        print(int(vol))
        applescript.AppleScript(f"set volume output volume {int(vol)}").run()
        
    cv2.imshow("Video", read)
    if cv2.waitKey(1) == ord('q'):
        break