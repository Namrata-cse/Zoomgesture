import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1000)
cap.set(4, 720)


detector = HandDetector(detectionCon=0.8, maxHands=2)
startDist = None
scale = 0
cx, cy = 550, 550


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread("1.jpg")

    if len(hands) == 2:
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [1,1,0,0,0] and \
                detector.fingersUp((hands[1])) == [1,1,0,0,0]:
            print("zoom")

            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            if startDist is None:
                #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                print(length)
                startDist = length
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length-startDist) // 2)
            cx, cy = info[4:]
            print(scale)
    else:
        startDist = None
    try:
        h1, w1 = img1.shape
        newW = ((h1+scale)//2)*2, ((w1+scale)//2)*2
        nh = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
        img1 = cv2.resize(img1, (newW, nh))

        img[cy - nh // 2:cy + nh // 2, cx - newW // 2:cx + newW // 2] = img1

    except:
        pass


    cv2.imshow("Image", img)
    cv2.waitKey(1)













