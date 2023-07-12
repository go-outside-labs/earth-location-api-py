## ✨🌏🐍 earth location api

<br>

### tl; dr

* this package serves an api for latitude and longitude location, given a city.

<br>


---

### endpoint `/location`

<br>

payload:

```
{
    "city": "berlin"
}
```


result:

```
{
    "lat": 52.5186925,
    "lon": 13.3996024,
    "tzone":1
}
```


<br>

----
### running locally

<br>

install dependencies and the app with:

```
make build
make install
```

run the [uvicorn](https://www.uvicorn.org/) api at `localhost:8080`:

```
make api
```

or, alternatively, run the cli:


```
loc

🌏✨ location api ✨🌏

options:
  -h, --help   show this help message and exit
  -l LOCATION  Find the latitude and longitude of a city. Example: loc -l <city>
```

for example:

```
loc -l los_angeles
latitude: 34.0536909
longitude: -118.242766
timezone: -7
```

<br>

### deploying to vercel

```
brew install vercel-cli
vercel login
vercel .
```