from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ YT Stream Proxy đang hoạt động!"

@app.route('/stream')
def stream():
    yt_url = request.args.get('v')
    if not yt_url:
        return "Thiếu tham số ?v=", 400

    try:
        ydl_opts = {'quiet': True, 'format': 'best[ext=mp4]'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url, download=False)
            video_url = info['url']
        return redirect(video_url)
    except Exception as e:
        return f"Lỗi khi lấy link: {e}", 500
