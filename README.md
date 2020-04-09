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

Once the server is up and running you can use CURL to send a GET request and test it out:
```
curl -v http://server:5000/state
```

Should return:
```
* TCP_NODELAY set
* Connected to server (10.10.10.10) port 5000 (#0)
> GET /state HTTP/1.1
> Host: server:5000
> User-Agent: curl/7.58.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 95
< Server: Werkzeug/1.0.1 Python/3.8.2
< Date: Thu, 09 Apr 2020 02:24:59 GMT
<
{"activity":"com.amazon.tv.launcher.ui.HomeActivity_vNext","package":"com.amazon.tv.launcher"}
* Closing connection 0
```
