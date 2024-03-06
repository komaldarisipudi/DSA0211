import cv2
video_path = "C:/Users/KOMAL DARISIPUDI/Desktop/cv images/indian-cricket-team-whatsapp-status-video-2021.mp4"
cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for frame_no in range(total_frames - 1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video in Reverse', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
