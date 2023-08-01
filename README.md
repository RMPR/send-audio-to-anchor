# Send audio file to Anchor

This scripts sends all the *mp3 files in a directory to your Anchor-hosted
podcast.  After installing the requirements, because of some funkiness with
Selenium, the recommend way of running it is inside a loop. If you are using
Fish, that would be:

```sh
while ls *.mp3; python send_audio_to_anchor.py; end
```