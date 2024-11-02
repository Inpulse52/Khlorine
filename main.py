import VideoObject
import TextObject
import GraphObject

video = VideoObject.Video(video_name="Khlorine_v0.3_example", duration=20)

title_text = TextObject.Text(value="There are three basic &ltrigonometric&l functions")
title_text.add_color(color='LimeGreen', code='l')
title_text = TextObject.Text(value="There are three basic &ltrigonometric&w functions", length=50, x=400, y=100, size=45, start=1, end=3, duration=20)
video.add(title_text)

sin_graph = GraphObject.Graph(value='math.sin(x)', scale=4, x=384, start=5, duration=20)
sin_text = TextObject.Text(value='Sin(x)', color='red', x=384, y=800, start=5, end=8, duration=20, size=45)
video.add(sin_graph)
video.add(sin_text)

cos_graph = GraphObject.Graph(value='math.cos(x)', scale=4, pointsColor='blue', start=10, duration=20)
cos_text = TextObject.Text(value='Cos(x)', color='blue', x=960, y=800, start=10, end=13, duration=20, size=45)
video.add(cos_graph)
video.add(cos_text)

tan_graph = GraphObject.Graph(value='math.tan(x)', scale=4, x=1536, pointsColor='yellow', start=15, duration=20)
tan_text = TextObject.Text(value='Tan(x)', color='yellow', x=1536, y=800, start=15, end=18, duration=20, size=45)
video.add(tan_graph)
video.add(tan_text)


video.render_objects()