import urllib
import json


playlist_url = 'http://nhacso.net/playlists/ajax-get-detail-playlist?dataId='


if __name__ == "__main__":
  response = urllib.urlopen("%s%s" % (playlist_url, 'XF5ZVEBY'))
  playlist_data = json.loads(response.read())
  songs = playlist_data['songs']
  print 'Number of songs: ' + str(len(songs))
  for song in songs:
    print song['name']
    print song['link_mp3']


