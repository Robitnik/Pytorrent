from dataclasses import dataclass, asdict
import os
from typing import List, Optional

@dataclass
class FileInfo:
    file_name: Optional[str] = None
    size: Optional[int] = None
    offset: Optional[int] = None
    mtime: Optional[float] = None
    executable_attribute: Optional[bool] = None
    hidden_attribute: Optional[bool] = None
    pad_file: Optional[bool] = None
    path: Optional[str] = None
    symlink_attribute: Optional[bool] = None
    symlink_path: Optional[str] = None

    def as_dict(self) -> dict:
        return asdict(self)

@dataclass
class TrackerInfo:
    complete_sent: Optional[bool] = None
    fail_limit: Optional[int] = None
    fails: Optional[int] = None
    message: Optional[str] = None
    min_announce: Optional[int] = None
    next_announce: Optional[int] = None
    scrape_complete: Optional[int] = None
    scrape_downloaded: Optional[int] = None
    scrape_incomplete: Optional[int] = None
    source: Optional[str] = None
    tier: Optional[int] = None
    trackerid: Optional[str] = None
    updating: Optional[bool] = None
    url: Optional[str] = None
    verified: Optional[bool] = None

    def as_dict(self) -> dict:
        return asdict(self)

@dataclass
class Info:
    name: Optional[str] = None
    comment: Optional[str] = None
    creation_date: Optional[int] = None
    creator: Optional[str] = None
    files_list: Optional[List[FileInfo]] = None
    is_i2p: Optional[bool] = None
    is_merkle_torrent: Optional[bool] = None
    is_valid: Optional[bool] = None
    metadata_size: Optional[int] = None
    nodes: Optional[List[str]] = None
    num_files: Optional[int] = None
    num_pieces: Optional[int] = None
    piece_length: Optional[int] = None
    priv: Optional[bool] = None
    total_size: Optional[int] = None
    trackers: Optional[List[TrackerInfo]] = None
    web_seeds: Optional[List[str]] = None

    def as_dict(self) -> dict:
        return asdict(self)


class TorrentInfo:
    def __init__(self, path: str, libtorrent):
        self._path = path
        self._lt = libtorrent
        self._info = self._lt.torrent_info(self._path)

    def info_as_dict(self) -> dict:
        return self.create_torrent_info().as_dict()

    def show_info(self) -> None:
        for key, value in self.info_as_dict().items():
            print(f"{key}: {value}")

    def create_torrent_info(self) -> Info:
        torrent_info = self._lt.torrent_info(self._path)
        info = Info(
            name=torrent_info.name(),
            comment=torrent_info.comment(),
            creation_date=torrent_info.creation_date(),
            creator=torrent_info.creator(),
            files_list=self.parse_file_info(torrent_info),
            is_i2p=torrent_info.is_i2p(),
            is_merkle_torrent=torrent_info.is_merkle_torrent(),
            is_valid=torrent_info.is_valid(),
            metadata_size=torrent_info.metadata_size(),
            nodes=torrent_info.nodes(),
            num_files=torrent_info.num_files(),
            num_pieces=torrent_info.num_pieces(),
            piece_length=torrent_info.piece_length(),
            priv=torrent_info.priv(),
            total_size=torrent_info.total_size(),
            trackers=self.parse_tracker_info(torrent_info),
            web_seeds=torrent_info.web_seeds()
            )
        return info

    def parse_tracker_info(self, torrent_info) -> List[TrackerInfo]:
        trackers = [
            TrackerInfo(
                complete_sent=getattr(tracker, "complete_sent", False),
                fail_limit=getattr(tracker, "fail_limit", 0),
                fails=getattr(tracker, "fails", 0),
                message=getattr(tracker, "message", ""),
                min_announce=getattr(tracker, "min_announce", 0),
                next_announce=getattr(tracker, "next_announce", 0),
                scrape_complete=getattr(tracker, "scrape_complete", 0),
                scrape_downloaded=getattr(tracker, "scrape_downloaded", 0),
                scrape_incomplete=getattr(tracker, "scrape_incomplete", 0),
                source=getattr(tracker, "source", ""),
                tier=getattr(tracker, "tier", 0),
                trackerid=getattr(tracker, "trackerid", ""),
                updating=getattr(tracker, "updating", False),
                url=getattr(tracker, "url", ""),
                verified=getattr(tracker, "verified", False)
            )
            for tracker in torrent_info.trackers()
        ]
        return trackers

    def parse_file_info(self, torrent_info) -> List[FileInfo]:
        files_list = [
            FileInfo(
                file_name=os.path.basename(f.path),
                size=f.size,
                offset=f.offset,
                mtime=getattr(f, "mtime", 0.0),
                executable_attribute=getattr(f, "executable_attribute", False),
                hidden_attribute=getattr(f, "hidden_attribute", False),
                pad_file=getattr(f, "pad_file", False),
                path=f.path,
                symlink_attribute=getattr(f, "symlink_attribute", False),
                symlink_path=getattr(f, "symlink_path", "")
            )
            for f in torrent_info.files()
        ]
        return files_list

    def __str__(self) -> str:
        return str(self.info_as_dict())

    def __repr__(self) -> str:
        return f"TorrentInfo(path={self._path!r})"

    def __call__(self) -> Info:
        return self.create_torrent_info()
