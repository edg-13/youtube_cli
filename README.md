# Youtube Challenge - Python
My submission for the YT CLI challenge. This python application is command line interface acting as a mini youtube player.

## Running and testing from the Commandline
To run the command-line application:
```shell script
python3 -m src.run
```

You can close the app by typing `EXIT` as a command.

#### Running the tests
To run all the tests:
```shell script
python3 -m pytest
```
For more verbose test output you can use
```shell script
python3 -m pytest -v
```

```shell script
python3 -m pytest test/part1_test.py
python3 -m pytest test/part2_test.py
python3 -m pytest test/part3_test.py
python3 -m pytest test/part4_test.py
```

## COMMANDS
`HELP` - displays all commands
`NUMBER_OF_VIDEOS` - displays number of videos
`SHOW_ALL_VIDEOS` - displays whole library
`PLAY <VIDEO_ID>` - plays a video
`PLAY_RANDOM` - plays a random video
`STOP` - stops currently playing video
`PAUSE` - pauses the video if it playing
`CONTINUE` - continues a paused video
`SHOW_PLAYING` - shows what video is playing

`CREATE_PLAYLIST <PLAYLIST NAME>` - creates a playlist 
`ADD_TO_PLAYLIST <PLAYLIST NAME> <VIDEO ID>` - adds a video to a playlist
`REMOVE_FROM_PLAYLIST <PLAYLIST NAME> <VIDEO ID>` - removes a video from a playlist
`CLEAR_PLAYLIST <PLAYLIST NAME>` - clears all videos from a playlist
`DELETE_PLAYLIST <PLAYLIST NAME>` - deletes a playlist
`SHOW_PLAYLIST <PLAYLIST NAME>` - shows contents of a playlist
`SHOW_ALL_PLAYLISTS` - shows all playlists created

`SEARCH_VIDEOS <SEARCH TERM>` - search the video library for titles with search term
`SEARCH_VIDEOS_WITH_TAG <TAG>` - search the video library for the desired tag
`FLAG_VIDEO <VIDEO ID> <OPTIONAL REASON>` - flag a video with an optional reason. This video cannot be played or added to any playlist thereafter.
`ALLOW_VIDEO <VIDEO ID>` - unflag a video.
