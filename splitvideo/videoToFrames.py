import os
import cv2
print(cv2.__version__)
videos = os.listdir('sample_video')
#videos.remove('videoToFrames.py')

for video in videos:
    
    if video.endswith(".mp4"):
    
      print(video[:-4])
      if not os.path.exists(video[:-4]):
          os.mkdir('output_video/'+video[:-4])

      print('Reading '+str(video))
      vidcap = cv2.VideoCapture('sample_video'+'/'+video)
      success,image = vidcap.read()
      count = 1
      success = True
      step=5
      while success:
      
        if count%step==0:  
          cv2.imwrite('output_video/'+video[:-4] + "/"+video[:-4]+str(count)+".jpg", image)     # save frame as JPEG file
        
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1
      
      vidcap.release()
