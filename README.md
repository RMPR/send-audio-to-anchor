# Send audio file to anchors

This scripts sends all the *mp3 files in a directory to your Anchor-hosted podcast.
Because of some funkiness with Selenium, the recommend way of running it is inside a
loop. If you are using Fish, that would be:

```sh
while ls *.mp3; python send_audio_to_anchor.py; end
```