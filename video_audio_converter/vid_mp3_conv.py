from moviepy.editor import VideoFileClip


def extract_audio(video_title):
    try:
        video = VideoFileClip(video_title + ".mp4")
        audio_file = video_title + ".mp3"
        video.audio.write_audiofile(audio_file)
    except Exception as e:
        print("Error occurred while extracting audio:", str(e))


video_title = input("Video title: ")
extract_audio(video_title)
