from session import Session
from torrent_info import TorrentInfo
from torrent_downloader import TorrentDownloader
import libtorrent as lt


class Torrent:
    def __init__(self, file_path):
        self._path = file_path
        self.info = TorrentInfo(path=self._path, libtorrent=lt)
    
