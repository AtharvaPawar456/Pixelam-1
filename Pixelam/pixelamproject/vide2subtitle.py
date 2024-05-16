from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

# Define the video file path
video_path = "data.mp4"

# Define the subtitle text and duration
subtitle_text = "This is a sample subtitle"
subtitle_duration = 5  # Duration of the subtitle in seconds

# Create a TextClip for the subtitle
subtitle_clip = TextClip(subtitle_text, fontsize=24, color='white').set_duration(subtitle_duration)

# Create a SubtitlesClip with the TextClip and set its duration
subtitles = SubtitlesClip([(subtitle_clip, 0)])  # Add the subtitle clip at t=0

# Load the original video clip
video_clip = VideoFileClip(video_path)

# Composite the video clip and subtitles
final_clip = CompositeVideoClip([video_clip, subtitles.set_pos(('center', 'bottom'))])

# Write the final video with subtitles to a new file
final_clip.write_videofile("video_with_subtitles.mp4", codec='libx264')
