# firetv
A simple Python Flask server to determine which app is running on a Fire TV.

This script accesses a Fire TV using ADB and executes ADB shell scripts to determine which app is running.  You'll need to have your "adbkey" and "adbkey.pub" files in order to authenticate to the Fire TV.  These files should be located in the directory that you're mapping to "/app" in the container.

Check out the following link for more information on how to access the Fire TV using ADB.
https://developer.amazon.com/docs/fire-tv/connecting-adb-to-device.html

In its current state you'll need to edit firetv.py so that the IP address for your fire tv is present.  Then build the container like this:
```
docker build . -t firetv_status:latest
```

You can run this container like this:
```
docker run -d -v /some/path/on/host:/app -p 5000:5000 firetv_status
```

You can also use the docker-compose file to run the container like this:
```
docker-compose -f docker-compose.yaml up -d
```
