#!/usr/bin/env python
# coding: utf-8

# In[1]:


from moviepy.editor import VideoFileClip, concatenate_videoclips


# In[2]:


clip_list = ["Watch Boruto- Naruto Next Generations Episode 160 Online Streaming Subbed & Dubbed.mp4",
             
            ]

for i in clip_list:
    clip1 = VideoFileClip(i)
    clip_array = []
    start = 5.0
    end = 8.90
    while end <= clip1.duration:
        clip_array.append(clip1.subclip(start,end))
        start += 11.1
        end += 11.1
    final_clip = concatenate_videoclips(clip_array)
    final_clip.write_videofile("Short_Video/" + i)


# In[ ]:




