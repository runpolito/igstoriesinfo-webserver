# Instagram stories info webserver
This webserver allows to get stories information of an instagram account.

## Requirements
An instagram account to authenticate the requests.

## Configuration
The web server relies on several environmental variables to configure every aspect of itself. Each topic will be shortly presented with its variables, showing the possible values that can be assigned.

### Flask
The server is exposed at `http://localhost:port`, and the `port`can be configured setting the `PORT` variable. It can assume any values in the range `1024-65353`.

The default value is `3001`.
```
PORT=[1024-65353]
```

### Instagram credentials
The server need Instagram credentials to auhtenticate requests: username and password can be set by using respectively `INSTAGRAM_USER` and `INSTAGRAM_PASSWORD` variables.

There are no default values.
```
INSTAGRAM_USER='usertestusername'
INSTAGRAM_PASSWORD='supersecretpassword@1'
```

## APIs
### Livingness
The answer should be the string `I am alive` with HTTP code `200 - OK`.

### Readiness
The answer should be the string `I am ready` with HTTP code `200 - OK`.
For now, this API is not useful, because it is necessary to understand the Instagram API limits, otherwise checkig the readiness will consume Instagram APIs and then the real funcionality will be affected.