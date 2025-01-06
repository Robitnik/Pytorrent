from client import Torrent


file_path = "/home/elon/Downloads/That Christmas (2024) NF WEB-DL 1080p [UKR_ENG] [Hurtom].mkv.torrent"


t = Torrent(file_path=file_path)
info = t.info
info.show_info()