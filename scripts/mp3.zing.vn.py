import requests
import threading
import time
from bs4 import BeautifulSoup

class Song:
    song_id = None
    name = None
    url = None
    code = None

    def __init__(self):
        pass

    def __str__(self):
        return "%s[%s],url=%s" % (self.name, self.song_id, self.url)

def download_worker(song):
    r = requests.get(song.url)
    print('File size: %d bytes' % len(r.content))
    with open(song.name + '.mp3', 'wb') as song_file:
        song_file.write(r.content)

if __name__ == '__main__':
    playlist_url = 'http://mp3.zing.vn/playlist/nhac-linh-songtu82vn/IWBUAUEZ.html'
    soup = BeautifulSoup(requests.get(playlist_url).content, 'html.parser')
    data_xml = None
    try:
        data_xml = soup.find(id= 'html5player')['data-xml']
    except:
        print('Cannot found Album URL')
    data_xml = data_xml.replace('/xml/', '/html5xml/')    
    data = requests.get(data_xml).json()['data']
    songs = []
    for song_json in data:
        song = Song()
        if 'code' in song_json:
            song.code = song_json['code']
        else:
            song.code = None
        song.song_id = song_json['id'].encode('utf-8')
        song.name = song_json['name']
        for song_url in song_json['source_list']:
            if len(song_url) > 0:
                song.url = song_url.encode('utf-8')
                if not song.url.startswith("http"):
                    song.url = "http://" + song.url
                break
        songs.append(song)

    print('Total song to be downloaded: %d' % len(songs))
    
    threads = []
    for song in songs:
        if song.code is not None:
            print("Error occured downloading song %s with code %d" % (song.song_id, song.code))            
        else:
            t = threading.Thread(target=download_worker, args=(song,))
            threads.append(t)
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
