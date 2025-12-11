from ytmusicapi import YTMusic
import random

def safe_extract_playlist_id(item):
    """
    Extracts a YouTube playlist ID from a YTMusic search result.
    Filters out IDs that cannot be used in a normal YouTube playlist link.
    """
    browse_id = item.get("browseId")
    if not browse_id:
        return None

    # On YTMusic, some playlists start with "VL". 
    # Removing "VL" generally makes the ID usable in a standard web playlist URL.
    if browse_id.startswith("VL"):
        playlist_id = browse_id[2:]
    else:
        playlist_id = browse_id

    # Reject IDs that are too short 
    if len(playlist_id) < 10:
        return None

    return playlist_id


def recommend_song(emotion):
    print(f"🔍 Searching for a playlist that matches the emotion '{emotion}'...")

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

    # Select one keyword based on the emotion
    keyword_list = mood_keywords.get(emotion, ['Trending Music'])
    selected_keyword = random.choice(keyword_list)

    # 1) Search for playlists
    results = yt.search(selected_keyword, filter='playlists')

    if results:
        # Look at the top 10 results and keep only valid playlists
        candidates = []
        for item in results[:10]:
            pid = safe_extract_playlist_id(item)
            if pid:
                title = item.get('title', 'No Title')
                candidates.append((title, pid))

        if candidates:
            title, playlist_id = random.choice(candidates)
            link = f"https://www.youtube.com/playlist?list={playlist_id}"
            return f"💿 Theme: {selected_keyword}\n🎹 Recommended Playlist: {title}\n🔗 Listen: {link}"

    
    return "No playlists could be found😢"
