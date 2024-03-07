"""
  Module for write watermark in images and videos
"""
# import libs
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"globals\\image_magic\\magick.exe"})

# main module
class Watermark :

    def __init__(self, text, input_path, output_path) : 
        self.text = text
        self.input_path = input_path
        self.output_path = output_path

    def image(self):
        # Open the input image
        image = Image.open(self.input_path)

        # Create a transparent layer with the same size as the image
        watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

        # Set the font, size, and opacity of the watermark text
        font = ImageFont.truetype('arial.ttf', image.width // 10)
        opacity = 128

        # Create a drawing context for the watermark layer
        draw = ImageDraw.Draw(watermark)

        watermark_text = self.text
        # Calculate the bounding box of the watermark text
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

        # Calculate the position of the watermark text
        x = (image.width - text_bbox[2]) // 2
        y = (image.height - text_bbox[3]) // 2

        # Draw the watermark text on the transparent layer
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

        # Convert both images to the same mode
        image = image.convert('RGBA')
        watermark = watermark.convert('RGBA')

        # Combine the original image and the watermark layer
        watermarked = Image.alpha_composite(image, watermark)

        # Convert the image to RGB mode
        watermarked = watermarked.convert('RGB')

        # Save the watermarked image as a JPEG file
        watermarked.save(self.output_path, 'JPEG')

    def video(self):
        # Load the video clip
        video_clip = VideoFileClip(self.input_path)

        # Create a TextClip for the watermark
        watermark_clip = TextClip(self.text, fontsize=100, color='#ffffff30', font='Arial-Bold')

        # Set the position of the watermark (top-right corner)
        x = (video_clip.size[0] - watermark_clip.size[0]) // 2
        y = (video_clip.size[1] - watermark_clip.size[1]) // 2


        # Set the duration of the watermark clip to match the video duration
        watermark_clip = watermark_clip.set_duration(video_clip.duration)

        # Set the position of the watermark clip
        watermark_clip = watermark_clip.set_position((x, y))

        # Overlay the watermark clip on the video clip
        video_with_watermark = CompositeVideoClip([video_clip, watermark_clip])

        # Write the video with watermark to the output file
        video_with_watermark.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

# Example usage for image
# input_image = 'RED.jpeg'
# output_image = 'output_image.jpg'
# watermark_text = 'Watermark'


# Example usage for video
# input_vid = 'vid.mp4'
# output_video= 'output_vid.mp4'
# watermark_text = 'Radwan'

# water = Watermark(
#     input_path=input_vid,
#     output_path=output_video,
#     text=watermark_text 
# )

# water.video()