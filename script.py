#!/usr/bin/env python
# coding: utf-8

from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("video.mp4")
clip_array = []
start = 5.0
end = 8.90
while end <= clip1.duration:
    clip_array.append(clip1.subclip(start,end))
    start += 11.1
    end += 11.1
final_clip = concatenate_videoclips(clip_array)
final_clip.write_videofile("output.mp4")