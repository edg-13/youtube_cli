"""A video player class."""

from .video_library import VideoLibrary
import random
from .playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = []
        self.is_paused = False
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_data = self._video_library.get_all_videos()
        sorted_vids = sorted(all_data, key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for vid in sorted_vids:
            print(vid)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if video.flag:
                print(f"Cannot play video: Video is currently flagged (reason: {video.flag})")
            else:
                self.is_paused = False
                if self.is_playing:
                    print(f"Stopping video: {self.is_playing.pop(0).title}")
                self.is_playing.append(video)
                print(f"Playing video: {video.title}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.is_playing:
            print(f"Stopping video: {self.is_playing.pop(0).title}")
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        video_list = self._video_library.get_all_videos()
        flag_filter = lambda x: len(x.flag) == 0
        filtered_videos = list(filter(flag_filter, video_list))
        if filtered_videos:
            random_video = random.choice(filtered_videos)
            self.play_video(random_video.video_id)
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""

        if self.is_playing:
            if self.is_paused:
                print(f"Video already paused: {self.is_playing[0].title}")
            else:
                self.is_paused = True
                print(f"Pausing video: {self.is_playing[0].title}")
        else:
            print("Cannot pause video: No video is currently playing")
        

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_playing:
            if self.is_paused:
                print(f"Continuing video: {self.is_playing[0].title}")
                self.is_paused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.is_playing:
            pause_status = "- PAUSED" * self.is_paused
            print(f"Currently playing: {self.is_playing[0]} {pause_status}")
        else:
            print("No video is currently playing")

#################################################################################

#                   PART 2

################################################################################

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() in self.playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
    


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        check = True
        if playlist_name.lower() not in self.playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            check = False
        if video is None and check:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            check = False
        if check and video.flag:
            print(f"Cannot add video to my_playlist: Video is currently flagged (reason: {video.flag})")
            check = False
        if check:
            playlist = self.playlists[playlist_name.lower()]
            success = playlist.add_video(video)
            # names = list(map(lambda x: x.title, playlist.video_list))
            # if video.title in names:
            #     print(f"Cannot add video to {playlist_name}: Video already added")
            # else:
            #     playlist.video_list.append(video)
            #     print(f"Added video to {playlist_name}: {video.title}")

            if success:
                print(f"Added video to {playlist_name}: {video.title}")
            else:
                print(f"Cannot add video to {playlist_name}: Video already added")
            

    def show_all_playlists(self):
        """Display all playlists."""

        if self.playlists:
            print("Showing all playlists:")
            sorted_playlists = sorted(self.playlists.items(), key=lambda x: x[1].name)
            for p in sorted_playlists:
                print(p[1].name)
        else:
            print("No playlists exist yet")


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists:
            print(f"Showing playlist: {playlist_name}")
            print(self.playlists[playlist_name.lower()])
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video = self._video_library.get_video(video_id)
        playlist = self.playlists.get(playlist_name.lower(), None)
        check = True
        if playlist is None:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            check = False
        if video is None and check:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            check = False
        if check:
            removed = playlist.delete_video(video)
            if removed:
                print(f"Removed video from {playlist_name}: {video.title}")
            else:
                print(f"Cannot remove video from {playlist_name}: Video is not in playlist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self.playlists.get(playlist_name.lower(), None)
        if playlist is None:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            playlist.clear_all()
            print(f"Successfully removed all videos from {playlist_name}")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self.playlists.get(playlist_name.lower(), None)
        if playlist is None:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            playlist.clear_all()
            del self.playlists[playlist_name.lower()]
            print(f"Deleted playlist: {playlist_name}")

################################################################################

#                   PART 3

################################################################################

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        search_filter_func = lambda x: search_term.lower() in x.title.lower() and len(x.flag) == 0
        results = list(filter(search_filter_func, all_videos))
        if results:
            print(f"Here are the results for {search_term}:")
            #video_results = list(map(self._video_library.get_video, results))
            sorted_results = sorted(results, key=lambda x: x.title)
            for idx,video in enumerate(sorted_results):
                print(f"{idx+1}) {video}")
            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            choice = input()
            if choice in [str(i) for i in range(1,len(results)+1)]:
                self.play_video(sorted_results[int(choice)-1].video_id)
        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        filtered_videos = [vid for vid in all_videos if not vid.flag]
        # all_tags = [[y.lower() for y in x.tags] for x in all_videos]
        # print(all_tags)
        results = []
        for video in filtered_videos:
            tag_list = [tag.lower() for tag in video.tags]
            if video_tag.lower() in tag_list:
                results.append(video)
        if results:
            print(f"Here are the results for {video_tag}:")
            #video_results = list(map(self._video_library.get_video, results))
            sorted_results = sorted(results, key=lambda x: x.title)
            for idx,video in enumerate(sorted_results):
                print(f"{idx+1}) {video}")
            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            choice = input()
            if choice in [str(i) for i in range(1,len(results)+1)]:
                self.play_video(sorted_results[int(choice)-1].video_id)
        else:
            print(f"No search results for {video_tag}")

#################################################################################

#                         PART 4

################################################################################

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        check = True
        if video is None:
            print(f"Cannot flag video: Video does not exist")
            check = False
        if check and video.flag:
            print("Cannot flag video: Video is already flagged")
            check = False
        if check:
            video.flag = flag_reason if flag_reason else "Not supplied"
            if self.is_playing:
                if self.is_playing[0].video_id == video_id:
                    self.stop_video()
            print(f"Successfully flagged video: {video.title} (reason: {video.flag})")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        check = True
        if video is None:
            print("Cannot remove flag from video: Video does not exist")
            check = False
        if check and not video.flag:
            print("Cannot remove flag from video: Video is not flagged")
            check = False
        if check:
            del video.flag
            print(f"Successfully removed flag from video: {video.title}")
