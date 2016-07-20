import requests

if __name__ == "__main__":
    playlist_id = "XF9ZUENW"
    playlists_url = 'http://nhacso.net/playlists/ajax-get-detail-playlist?dataId=' + playlist_id
    print 'Playlist AJAX URL: ' + playlists_url
    r = requests.get(playlists_url)
    playlist = r.json()
    if 'songs' in playlist:
        songs = playlist['songs']
        print 'Number of songs: ' + str(len(songs))
    else:
        print 'Invalid playlist with id=%s' % playlist_id
