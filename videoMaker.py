def makeVideo(folder_path, text, out_path):
    import os
    from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, concatenate_videoclips
    from moviepy.editor import ImageClip
    from moviepy.config import change_settings
    change_settings({"IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})
    audio_path = "C:/Users/carac/OnlySpeakTTS/audio/"
    afiles = sorted([f for f in os.listdir(audio_path) if f.endswith(".wav")])
    afile = afiles[-1]
    files = os.listdir(folder_path)
    clips = []
    prompt = text
    audio = AudioFileClip(audio_path + afile)
    duration = audio.duration

    # Calculează durata medie pe cuvânt bazată pe durata totală și numărul total de cuvinte
    words = prompt.split()
    total_words = len(words)
    avg_duration_per_word = duration / total_words

    # Estimează numărul de cuvinte care pot fi afișate confortabil pe un rând
    words_per_line = 8  # Acest număr poate varia

    subtitles = []

    # Preia dimensiunea primului ImageClip pentru a seta dimensiunea TextClip-urilor
    if files:
        first_image_path = os.path.join(folder_path, files[0])
        first_image_clip = ImageClip(first_image_path)
        clip_width = first_image_clip.size[0]

    start_time = 0
    for file in files:
        image_clip = ImageClip(os.path.join(folder_path, file)).set_duration(duration / len(files)).set_fps(24)
        clips.append(image_clip)

    for i in range(0, total_words, words_per_line):
        sentence_fragment = " ".join(words[i:i + words_per_line])
        fragment_length = len(sentence_fragment.split())
        text_duration = avg_duration_per_word * fragment_length

        text_clip = TextClip(sentence_fragment, fontsize=24, color='white', bg_color='rgba(0, 0, 0, 0.5)', size=(clip_width, None))
        text_clip = text_clip.set_start(start_time).set_duration(text_duration).set_position(('center', 'center'))
        subtitles.append(text_clip)

        start_time += text_duration

    video_clip = concatenate_videoclips(clips, method="compose")
    final_clip = CompositeVideoClip([video_clip, *subtitles]).set_audio(audio)
    final_output_path = os.path.join(out_path, "output.mp4")  # Corectează calea de ieșire
    final_clip.write_videofile(final_output_path, fps=24)

# Corectează apelul funcției cu argumentele corecte

