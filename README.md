# eddiecanyon.com

Static one-page site for Eddie Canyon, served by GitHub Pages from `main`.

## Editing

`index.html` is generated. Edit content in `build.py`, then run:

```
python3 build.py
```

Styles live in `style.css`. Behavior lives in `main.js`: the palette picker,
the id10t photo reveal and the section highlight. After changing either file,
bump its `?v=` number in `build.py` so browsers fetch the new version.

Preview locally:

```
python3 -m http.server 8642
```

## Hosting

- The domain is registered at Squarespace Domains and uses Squarespace
  nameservers.
- DNS has four A records for `@` (185.199.108.153, .109, .110, .111) and a
  `www` CNAME pointing to `sean-cannon.github.io`.
- `CNAME` holds the custom domain. HTTPS is enforced in Settings → Pages.

## TODO

- [ ] Add Spotify album links for **Small Town II**, **New Day** and
      **Xplicit Xposition**. They currently open a Spotify search.
- [ ] **A Place Of Purification**: add its Spotify link once it's out (10.31)
      and remove the "Out 10.31" flag from its row in `releases`.
- [ ] Add a vinyl purchase link for id10t. The page currently says "Vinyl:
      details soon".

To add a Spotify link, put the album ID from the album's Spotify URL into
`SPOTIFY_IDS` in `build.py`. Use the exact title as the key.
