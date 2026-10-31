import pathlib, random, html, urllib.parse
root = pathlib.Path(__file__).resolve().parent
SUB = "https://eddiecanyon.substack.com"
APP = "https://apps.apple.com/app/id10t/id6747997678"
SPOT = "https://open.spotify.com/artist/7kMFNpUB2KM34UrnjFqYXP"
APPLE = "https://music.apple.com/us/artist/eddie-canyon/1583303151"
YT = "https://www.youtube.com/@eddie.canyon"
MZ = "https://is1-ssl.mzstatic.com/image/thumb/"

SPOTIFY_IDS = {
 "Wild_01":"0HRBRYmKXNhHJ3VAvDZpnf","Disclosure":"0ikN7mzdSFBotEhae8I8uR","One Hit":"5JiHazPEfyy7X3rN5ps7dg",
 "Slide":"5FC46p9kNfQLxaKNkCEEbw","Prompt Engineering":"61uERX2yNqG7gBwaXOlmC6","The Lunch Table":"67td9Uown6AnLqATcL1pfR",
 "Dying In the Dark (Ac808stic)":"7z7dOqO8SKUhDKB8igSIIP","Switch or Fakie":"71NEDoOHD5OX3RxkfkMSWN",
 "Beat Tape, Vol. 1":"2OX4a0Vx3R3l7F7E2wc9Lg","Idenny Theff":"1TQGU63xCYhXgUIePUJ5t9",
}
releases = [  # date, title, kind, apple path, art path, flag
 ("2026","A Place Of Purification","Feature · Single","a-place-of-purification-feat-eddie-canyon-single/6825985346","Music211/v4/8e/a9/d9/8ea9d98c-56df-19a2-bda5-18b6f08df158/885000733093.png","Out 10.31"),
 ("2025","Wild_01","Single","wild-01-single/1833144988","Music211/v4/ef/38/57/ef385743-b8f3-48f6-d059-bb5e806ac73d/artwork.jpg",""),
 ("2025","Disclosure","Single","disclosure-single/1831331159","Music221/v4/60/15/fa/6015fa0a-94eb-c159-731b-940f2a6d2899/artwork.jpg",""),
 ("2025","One Hit","Single","one-hit-single/1828250637","Music211/v4/a2/27/53/a227531c-7a85-67e0-3a00-ce0c537b464c/artwork.jpg",""),
 ("2025","Slide","Single","slide-single/1826706748","Music221/v4/6b/d1/f1/6bd1f10a-fa2c-e649-fe2b-47d639a1bb23/artwork.jpg",""),
 ("2023","Prompt Engineering","Album","prompt-engineering/1719641035","Music116/v4/e9/f5/38/e9f53818-e52d-9657-360c-aa9699002c85/artwork.jpg",""),
 ("2023","The Lunch Table","EP","the-lunch-table-ep/1683331615","Music126/v4/57/55/67/5755670c-c8a7-d168-f0eb-ea47d6404750/artwork.jpg",""),
 ("2022","Dying In the Dark (Ac808stic)","Single","dying-in-the-dark-ac808stic-version-single/1648848816","Music112/v4/5d/11/19/5d1119bd-359c-e098-9c38-27f170d44894/artwork.jpg",""),
 ("2022","Switch or Fakie","Single","switch-or-fakie-single/1635338634","Music112/v4/1f/da/02/1fda02ae-47ab-023e-d76d-32770495dbe9/artwork.jpg",""),
 ("2022","Beat Tape, Vol. 1","Instrumental EP","beat-tape-vol-1-instrumental-ep/1618328363","Music122/v4/31/1d/df/311ddf7b-1995-f0b2-6c7e-cc10c074dc76/artwork.jpg",""),
 ("2022","Idenny Theff","Album","idenny-theff/1608094179","Music126/v4/f7/44/34/f74434cd-4a61-1067-0405-fa99f06757b3/artwork.jpg",""),
 ("2022","Xplicit Xposition","Single","xplicit-xposition-single/1607684247","Music116/v4/aa/5a/e1/aa5ae110-e70a-5823-c846-d9325f5935db/artwork.jpg",""),
 ("2021","New Day","Single","new-day-single/1585691963","Music125/v4/79/f1/e8/79f1e8d5-8f02-a983-e7d0-514225561854/artwork.jpg",""),
 ("2021","Small Town II","Single","small-town-ii-single/1583311690","Music115/v4/b5/2e/10/b52e10ca-b9aa-c90a-2cee-71c3a5644593/artwork.jpg",""),
]
music_vids = [
 ("wRlo8s12v7o","Small Town II","Official music video"),
 ("ozxSg5i6p2E","Dying In The Dark","Ac808stic · lyric video"),
 ("kuzIMtQo6LI","Shrewd as a Serpent","Live · Tiny Desk Contest 2023"),
 ("jV8ARlFi01k","Xplicit Xposition","Live · Tiny Desk Contest 2022"),
 ("3hEcjOW0pDw","The Lunch Hour","Live performance"),
]
thought_vids = [
 ("e730cmNgG3c","The Fourth Beast of Daniel 7","Thought video"),
 ("0gsI62Geasw","Material | Symbol | Technique","Form Devoid · Ep. 1"),
 ("zxsxt3k1r8I","Form Devoid: The Intro","98.3 The Cannonball presents"),
 ("HnJ9pdTQI-I","98.3 The Cannonball","Interview · Idenny Theff & the hero's journey"),
]
posts = [
 ("A Message To The Cave Dwellers","Letting your eyes adjust to the shadows","a-message-to-the-cave-dwellers"),
 ("Is A.I. The AntiChrist?","Opposing the anointed","is-ai-the-antichrist"),
 ("God &amp; Technology","Does the Bible reveal God’s stance on tech?","god-and-technology"),
]
NEW = 'tabindex' # unused
ext = 'target="_blank" rel="noopener"'

def rel(r):
    y,t,k,ap,art,flag = r
    f = f'<span class="flag">{flag}</span>' if flag else ''
    sid = SPOTIFY_IDS.get(t)
    sp = f"https://open.spotify.com/album/{sid}" if sid else "https://open.spotify.com/search/" + urllib.parse.quote("Eddie Canyon " + t)
    return f'''        <div class="rel">
          <a class="cover" href="{sp}" {ext} aria-label="{html.escape(t)} on Spotify">
            {f}<img src="{MZ}{art}/600x600bb.jpg" alt="" loading="lazy" width="600" height="600">
            <span class="cap"><b>{html.escape(t)}</b>{y} · {k}</span>
          </a>
          <a class="alt" href="https://music.apple.com/us/album/{ap}" {ext} aria-label="{html.escape(t)} on Apple Music">Apple ↗</a>
        </div>'''

def vid(v):
    i,t,s = v
    return f'''          <a class="vid" href="https://www.youtube.com/watch?v={i}" {ext}>
            <span class="thumb"><img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"></span>
            <span><b>{t}</b><small>{s} · YouTube ↗</small></span>
          </a>'''

def post(n,p):
    t,s,slug = p
    return f'''          <a class="post" href="{SUB}/p/{slug}" {ext}>
            <span class="n">{n:02d}{" · NEW" if n==1 else ""}</span>
            <b>{t}</b>
            <span>{s}</span>
            <em>Read ↗</em>
          </a>'''

# blue scribble for the id10t collage
random.seed(10)
x,y = 40.0, 60.0; pts=[]
for _ in range(70):
    x = min(380,max(10,x+random.uniform(-60,60))); y = min(390,max(10,y+random.uniform(-45,55)))
    pts.append(f"{x:.0f},{y:.0f}")
d = "M" + " Q".join(f"{pts[i]} {pts[i+1]}" for i in range(0,len(pts)-1,2))
PALETTES = [("acid","Acid","#e4ff3a","#ff5b1f","#2b3bff"),("infrared","Infrared","#3aa9a1","#ff2b1c","#071113"),
 ("xerox","Xerox","#f4f4f1","#cfcfca","#ff1f1f"),("desert","Desert","#e9a23b","#c1442a","#23574a"),
 ("bubblegum","Bubblegum","#ff9ad5","#34e0a1","#6a2bff"),("ice","Ice","#a8e6ff","#ffd60a","#0047ff")]
def picker():
    btns = "".join(f'<button class="swatch" type="button" data-palette-btn="{k}" aria-label="{n} colors" title="{n}" style="--a:{a};--b:{b};--c:{c}"></button>' for k,n,a,b,c in PALETTES)
    return f'<div class="palette" role="group" aria-label="Color palette"><span class="label">Color</span>{btns}</div>'
glyphs = ("id10t·" * 900)

tick_items = [
 "<b>Eddie Canyon</b>", "Not for the surface dwellers",
 "<b>New</b> A Place Of Purification · out 10.31",
 "<b>id10t</b> the album is an app", "Words on Substack", "Videos on YouTube",
]
tick = "".join(f"<span>{t} ++</span>" for t in tick_items)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Eddie Canyon</title>
  <meta name="description" content="Eddie Canyon: music, videos and writing. Not for the surface dwellers.">
  <meta property="og:title" content="Eddie Canyon">
  <meta property="og:description" content="Music, videos and writing. Not for the surface dwellers.">
  <meta name="theme-color" content="#e4ff3a">
  <meta property="og:image" content="https://eddiecanyon.com/img/og.jpg">
  <script>try{{var p=new URLSearchParams(location.search).get("palette")||localStorage.getItem("ec-palette");if(p&&p!=="acid")document.documentElement.setAttribute("data-palette",p)}}catch(e){{}}</script>
  <link rel="stylesheet" href="style.css?v=13">
  <script src="main.js?v=12" defer></script>
</head>
<body>
  <div class="ticker" aria-hidden="true"><div class="track">{tick}{tick}</div></div>

  <nav class="rail" aria-label="Sections">
    <a class="home" href="#top" aria-label="Top">EC</a>
    <a href="#music" data-sec="music"><span class="n">01</span>Music</a>
    <a href="#watch" data-sec="watch"><span class="n">02</span>Watch</a>
    <a href="#think" data-sec="think"><span class="n">03</span>Think</a>
    <a href="#bio" data-sec="bio"><span class="n">04</span>Bio</a>
    <a href="#id10t" data-sec="id10t"><span class="n">05</span>id10t</a>
  </nav>

  <main id="top">
    <section class="hero" aria-label="Intro">
      <div class="dark">
        <ol class="index">
          <li><a href="#music"><span class="n">01</span>Music</a></li>
          <li><a href="#watch"><span class="n">02</span>Watch</a></li>
          <li><a href="#think"><span class="n">03</span>Think</a></li>
          <li><a href="#bio"><span class="n">04</span>Bio</a></li>
          <li><a href="#id10t"><span class="n">05</span>id10t</a></li>
        </ol>
      </div>
      <h1><span>Eddie</span><span>Canyon</span></h1>
      <a class="sticker" href="#id10t"><b>id10t</b>the album is an app →</a>
      <div class="intro">
        <p class="lede"><em>Not</em> for the surface dwellers.</p>
        <p>Songs, live sets and writing from underneath. New feature “A Place Of Purification” lands 10.31.</p>
        <div class="links">
          <a class="tag solid" href="{SPOT}" {ext}>Spotify ↗</a>
          <a class="tag" href="{APPLE}" {ext}>Apple Music ↗</a>
          <a class="tag" href="{YT}" {ext}>YouTube ↗</a>
        </div>
        {picker()}
      </div>
    </section>

    <section id="music" aria-labelledby="music-h">
      <div class="head">
        <h2 id="music-h"><span class="num">01 / {len(releases)} releases</span>Music</h2>
        <div class="links">
          <a class="tag solid" href="{SPOT}" {ext}>Spotify ↗</a>
          <a class="tag" href="{APPLE}" {ext}>Apple Music ↗</a>
        </div>
      </div>
      <div class="covers">
{chr(10).join(rel(r) for r in releases)}
      </div>
    </section>

    <section id="watch" class="watch" aria-labelledby="watch-h">
      <div class="head">
        <h2 id="watch-h"><span class="num">02 / YouTube</span>Watch</h2>
        <div class="links"><a class="tag" href="{YT}" {ext}>@eddie.canyon ↗</a></div>
      </div>
      <div class="cols">
        <div>
          <h3><span>Music videos &amp; live</span><span>{len(music_vids):02d}</span></h3>
{chr(10).join(vid(v) for v in music_vids)}
        </div>
        <div>
          <h3><span>Thought videos &amp; talk</span><span>{len(thought_vids):02d}</span></h3>
{chr(10).join(vid(v) for v in thought_vids)}
        </div>
      </div>
    </section>

    <section id="think" class="think" aria-labelledby="think-h">
      <div class="side"><div><h2 id="think-h">Think</h2><span class="num">03 / Substack</span></div></div>
      <div>
        <div class="bar"><span>Essays · eddiecanyon.substack.com</span><a class="tag" href="{SUB}" {ext}>All posts ↗</a></div>
        <div class="posts">
{chr(10).join(post(n,p) for n,p in enumerate(posts,1))}
        </div>
        <a class="subscribe" href="{SUB}/subscribe" {ext}>Subscribe on Substack ↗</a>
      </div>
    </section>

    <section id="bio" class="bio" aria-labelledby="bio-h">
      <div class="label"><span class="num">04</span><h2 id="bio-h">Bio</h2></div>
      <div class="text">
        <p class="body">As the collective attention span shrinks, Eddie Canyon finds himself searching for meaning within the noise. Reaching into and around his Arkansas roots, Eddie carves a distinctively southern Hip Hop undercurrent in his exploratory approach to music. Weaving tales of battling addiction, thoughts on spirituality, and irreverent social commentary into his lyrics, Eddie aims to intrigue his audience at the least, and at most, leave them with a liberating degree of thoughtfulness. In his own words:</p>
        <blockquote>“The Matrix is real, but there’s a way out.”</blockquote>
      </div>
    </section>

    <section id="id10t" class="id10t" aria-labelledby="id10t-h">
      <div class="copy">
        <span class="num">05 / Eddie Canyon presents</span>
        <h2 id="id10t-h">id10t</h2>
        <p class="lede">The album is an app. On iPhone now. On vinyl too.</p>
        <div class="links">
          <a class="tag solid" href="{APP}" {ext}>Get the app ↗</a>
          <span class="tag muted">Vinyl: details soon</span>
        </div>
      </div>
      <div class="collage" tabindex="0" role="button" aria-label="Reveal the id10t album art">
        <div class="art" aria-hidden="true"><img src="{MZ}Purple221/v4/01/4d/f1/014df16e-9b99-dc6b-a782-4b6573fdda74/AppIcon-0-0-1x_U007ephone-0-1-85-220.png/48x48bb.jpg" alt="" width="48" height="48"></div>
        <div class="glyphs" aria-hidden="true">{glyphs}</div>
        <svg class="scribble" viewBox="0 0 400 400" preserveAspectRatio="none"><path d="{d}" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
        <span class="hud">● Rec · cam 05 · id10t</span>
        <span class="cross"></span>
        <div class="photo"></div>
        <span class="hint">Hover or tap to develop ↯</span>
      </div>
    </section>
  </main>

  <footer class="foot">
    <div><div class="big">Eddie Canyon</div><p>© 2026 · Not for the surface dwellers</p>{picker()}</div>
    <ul>
      <li><a href="{SPOT}" {ext}>Spotify ↗</a></li>
      <li><a href="{APPLE}" {ext}>Apple Music ↗</a></li>
      <li><a href="{YT}" {ext}>YouTube ↗</a></li>
      <li><a href="{SUB}" {ext}>Substack ↗</a></li>
      <li><a href="{APP}" {ext}>id10t app ↗</a></li>
    </ul>
  </footer>
</body>
</html>
'''
(root/"index.html").write_text(page)
for name, anchor in [("listen.html","music"),("watch.html","watch")]:
    (root/name).write_text(f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Eddie Canyon</title>
<meta http-equiv="refresh" content="0; url=./#{anchor}"><link rel="canonical" href="./#{anchor}"></head>
<body><a href="./#{anchor}">Moved to the home page</a></body></html>
''')
print("ok")
