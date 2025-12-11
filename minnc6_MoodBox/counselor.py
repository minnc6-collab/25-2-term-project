from ytmusicapi import YTMusic
import random

def safe_extract_playlist_id(item):
    """
    YTMusic 검색 결과 하나(item)에서
    실제 유튜브 재생목록 링크에 쓸 수 있는 playlist ID만 뽑는 함수
    """
    browse_id = item.get("browseId")
    if not browse_id:
        return None

    # YTMusic 쪽은 재생목록에 VL 접두사가 붙어 있는 경우가 많음
    # → 웹 유튜브에서는 list= 뒤에 VL 빼고 쓰는 게 더 안정적
    if browse_id.startswith("VL"):
        playlist_id = browse_id[2:]
    else:
        playlist_id = browse_id

    # 너무 짧은 이상한 ID는 버리기 (대충 필터용)
    if len(playlist_id) < 10:
        return None

    return playlist_id


def recommend_song(emotion):
    print(f"🔍 '{emotion}' 감정에 맞는 플레이리스트를 찾는 중...")

    yt = YTMusic()

    mood_keywords = {
        'joy': [
            'Party Dance Hits', 'Feel Good Pop', 'Happy Vibes',
            'Upbeat K-pop', 'Driving Music', 'Summer Hits'
        ],
        'sadness': [
            'Mood Booster Pop', 'Energetic Pop', 'Happy Songs',
            'Cheer Up Music', 'Positive Vibes'
        ],
        'anger': [
            'Calming Piano', 'Relaxing Jazz', 'Stress Relief Music',
            'Meditation Music', 'Deep Sleep Music'
        ],
        'neutral': [
            'Work Study Lo-Fi', 'Coffee Shop Jazz', 'Acoustic Pop',
            'Instrumental Hip Hop', 'Background Music'
        ],
        'surprise': [
            'Chill R&B', 'Mellow Pop', 'Acoustic Covers',
            'Calm Jazz', 'Lo-Fi Hip Hop'
        ],
        'fear': [
            'Peaceful Piano', 'Calming Nature Sounds', 'Disney Piano',
            'Hopeful Music', 'Comforting Songs'
        ],
        'disgust': [
            'Fresh Acoustic', 'Clean Pop', 'Healing Music',
            'Forest Sounds', 'Morning Jazz'
        ]
    }

    # 감정에 맞는 검색 키워드 리스트에서 하나 랜덤 선택
    keyword_list = mood_keywords.get(emotion, ['Trending Music'])
    selected_keyword = random.choice(keyword_list)

    # 1) 플레이리스트 검색
    results = yt.search(selected_keyword, filter='playlists')

    if results:
        # 상위 10개 정도만 후보로 보고, 그 중에서
        # 실제로 유효한 playlistId가 있는 것만 모음
        candidates = []
        for item in results[:10]:
            pid = safe_extract_playlist_id(item)
            if pid:
                title = item.get('title', '제목 없음')
                candidates.append((title, pid))

        if candidates:
            title, playlist_id = random.choice(candidates)
            link = f"https://www.youtube.com/playlist?list={playlist_id}"
            return f"💿 테마: {selected_keyword}\n🎹 추천 재생목록: {title}\n🔗 바로 듣기: {link}"

    # 2) 플레이리스트 쪽이 전부 애매하면, 그냥 노래 단일곡 추천으로 fallback
    song_results = yt.search(selected_keyword, filter='songs')
    if song_results:
        top_song = random.choice(song_results[:5])
        title = top_song.get('title', '제목 없음')
        video_id = top_song.get('videoId')
        if video_id:
            return f"💿 AI 추천곡: {title}\n🔗 바로 듣기: https://www.youtube.com/watch?v={video_id}"

    return "노래를 찾을 수 없습니다 ㅠㅠ"
