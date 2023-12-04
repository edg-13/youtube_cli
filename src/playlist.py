from .video import Video

class Playlist:
    def __init__(self, playlist_name: str):
        self._name = playlist_name
        self.video_list = []

    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        if self.video_list:
            return "\n".join([str(vid) for vid in self.video_list])
        else:
            return "No videos here yet"
    
    def add_video(self, vid: Video):
        names = list(map(lambda x: x.title, self.video_list))
        if vid.title in names:
            success = False
        else:
            self.video_list.append(vid)
            success = True
        return success

    def delete_video(self, vid: Video):
        found = False
        for idx,video in enumerate(self.video_list):
            if video.video_id == vid.video_id:
                found = True
                break
        if found:
            self.video_list.pop(idx)
            return True
        else:
            return False
        
    def clear_all(self):
        self.video_list[:] = []