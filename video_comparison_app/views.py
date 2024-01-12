from django.shortcuts import render
from .utils import compare_videos

def choose_videos(request):
    if request.method == 'POST':
        video_path1 = request.FILES.get('video1')
        video_path2 = request.FILES.get('video2')

        if video_path1 and video_path2:
            compare_result = compare_videos(video_path1, video_path2)
            return render(request, 'result.html', {'compare_result': compare_result})

    return render(request, 'choose_videos.html')
