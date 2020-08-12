# Split video on frames: 
Run the python videoToFrames.py script. It reads the current video file and separates each video into image files that are compatible with the frames.

## Usage:

```sh
$ videoToFrame.py
```

# Split video on short videos: 
Run the shell script *videoToShortVideos.sh* that receives a video file, with the interval parameters in seconds, the name of the output video,and the extension of the output videos.
For testing, there is a short video file in *sample_video/jh1_16.mp4*, the output can be directed to the *output_video* directory, an example of use is described below.
In the execution below, files with the name *"test"*, followed by an index, will be generated inside the *output_video* directory.

## Usage:
```sh
$ videoToShortVideos.sh sample_video/jh1_16.mp4 10 output_video/teste mp4
```
