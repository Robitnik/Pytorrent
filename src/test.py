from client import Torrent


file_path = "/home/elon/Downloads/Ameku Likarka-detektyv [RG][WEBRip Ai Rem 1080p x265 AAC 2.0].torrent"

t = Torrent(file_path=file_path)
print(t.get_info().show_info())