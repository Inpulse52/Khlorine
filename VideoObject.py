import subprocess

class Video:
    def __init__(self, video_name="video", duration=20):

        self.name = video_name
        self.duration = str(duration)
        self.objects = []

        ffmpeg_cmd = [
            r'C:\ffmpeg\ffmpeg.exe',
            '-f', 'lavfi',                                          # Format
            '-r', '25',                                             # Frame Rate (25 fps)
            '-i', 'color=c=black:s=1920x1080:d=' + self.duration,   # Input (Black 2930x1080p 5 second long video)
            '-c:v', 'libx264',                                      # Codec (libx264)
            '-pix_fmt', 'yuv420p',                                  # Pixal Format (yuv420p)
            '-loglevel', 'quiet',                                   # Prevents ffmpeg from displaying updates during the creation of the video
            '-y',                                                   # Can over-write the output file
            self.name + '.mp4'                                      # Name of file
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"Succesfully created '{self.name}.mp4' ({self.duration} seconds long)")
        except subprocess.CalledProcessError as e:
            print("Failed to create a video")

    def add(self, object=None):
        self.objects.append(object)

    def display_objects(self):
        print(self.objects)
    
    def render_objects(self):

        fs = open("command.txt", "w")
        for object in self.objects:
            if (object.type() == "text"):
                fs.write(object.animate())
            elif object.type() == "graph":
                fs.write(object.toText())
        fs.close()

        ffmpeg_cmd = [
            r'C:\ffmpeg\ffmpeg.exe',
            '-f', 'lavfi',                                          # Format
            '-r', '25',                                             # Frame Rate (25 fps)
            '-i', 'color=c=black:s=1920x1080:d=' + self.duration,   # Input (Black 2930x1080p 5 second long video)
            '-filter_script', "command.txt",                        # Displays all the filters in the 'command.txt' file
            '-c:v', 'libx264',                                      # Codec (libx264)
            '-pix_fmt', 'yuv420p',                                  # Pixal Format (yuv420p)
            '-loglevel', 'quiet',                                   # Prevents ffmpeg from displaying updates during the creation of the video
            '-y',                                                   # Can over-write the output file
            self.name + '.mp4'                                      # Name of file
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print("Succesfully Rendered the Video")
        except subprocess.CalledProcessError as e:
            print("Render Failed: " + str(e))