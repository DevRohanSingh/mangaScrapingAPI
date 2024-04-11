# API Docs

## 1. '/today': returns a list of today's updated comics (latest update)

```json
[
    {
        "id": "manga-eb981436",
        "thumb": "https://avt.mkklcdnv6temp.com/14/r/19-1583497652.jpg",
        "title": "In The Sunroom"
    },
    {
        "id": "manga-dv981004",
        "thumb": "https://avt.mkklcdnv6temp.com/49/f/17-1583497041.jpg",
        "title": "Boku no Kokoro no Yabai yatsu"
    },
]
```


## 2. '/hot': returns a list of hottest/trending comics

```json
[
  {
    "id": "manga-ax951880",
    "thumb": "https://avt.mkklcdnv6temp.com/19/v/1-1583464475.jpg",
    "title": "Tales of Demons and Gods"
  },
  {
    "id": "manga-dr980474",
    "thumb": "https://avt.mkklcdnv6temp.com/30/a/17-1583496340.jpg",
    "title": "Solo Leveling"
  },
]
```

## 3. '/id': Returns a single comic's information by id
```json
{
    "about": "Nie Li, one of the strongest Demon Spiritist in his past life standing at the pinnacle of the martial world , however he lost his life during the battle with Sage Emperor and the six deity ranked beast, his soul was then reborn back in time back to when he is still 13. Although he’s the weakest in his class with the lowest talent at only Red soul realm, with the aid of the vast knowledge which he accumulated in his previous life, he trained faster then anyone. Trying to protect the city which in the coming future was being assaulted by beast and ended up being destroyed as well as protecting his lover, friends and family who died by the beast assault. and to destroy the Sacred family whom abandon their duty and betrayed the city in his past life.",
    "genre": [
        "Action",
        "Adventure",
        "Comedy",
        "Drama",
        "Fantasy",
        "Harem",
        "Romance",
        "Shounen",
        "Manhua"
    ],
    "thumb": "https://avt.mkklcdnv6temp.com/19/v/1-1583464475.jpg",
    "title": "Tales Of Demons And Gods"
}
```

## 4. '/id/episodes': returns the latest episodes for a comic by id
```json
[
  {
    "date": "Apr 10,24",
    "id": "manga-ax951880",
    "link": "https://chapmanganato.to/manga-ax951880/chapter-470.1",
    "thumb": "https://avt.mkklcdnv6temp.com/19/v/1-1583464475.jpg",
    "title": "Chapter 470.1",
    "view": "40.2K"
  },
  {
    "date": "Apr 06,24",
    "id": "manga-ax951880",
    "link": "https://chapmanganato.to/manga-ax951880/chapter-469.5",
    "thumb": "https://avt.mkklcdnv6temp.com/19/v/1-1583464475.jpg",
    "title": "Chapter 469.5",
    "view": "60.3K"
  },
]
```