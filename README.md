# The World in One Image — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/yafiteesss/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/yafiteesss/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A 1024×1024 newspaper-style front page that sums up Friday 20 November 2026 in six stories. `main.py` writes the finished picture to `/output/entry.png`.

## How to run

```sh
python3 main.py
# writes /output/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tgs239he&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## Stories

Friday 20 November 2026, six stories from Kyiv to Cincinnati:

1. **Kyiv hit by ballistic missiles** — Russia strikes Kyiv overnight, damaging three bridges over the Dnipro; a drone hits a hospital in Kharkiv and injures four.
2. **Houthis strike Saudi targets** — Houthi forces claim drone and missile strikes on four targets in Saudi Arabia; a tanker catches fire after hitting a mine east of the Strait of Hormuz.
3. **COP31 closes in Antalya** — UN climate talks end with a 144-paragraph draft, $120 billion on the table, and fossil fuels left as two unresolved options.
4. **Drones halt Genoa airport** — Genoa suspends flights after unidentified drones are spotted over the airport.
5. **California probes Nvidia** — California targets Nvidia in a probe over AI chips bound for China.
6. **Fiona the hippo dies** — Cincinnati Zoo's beloved hippo Fiona dies after swallowing a hat; the premature baby who became a social media star is gone.

## Bounty

- Bounty: https://make.fun/bounty/news-image-20261120
- Entries close: 22 Nov 2026, 00:00 UTC (22 Nov 2026, 07:00 WIB)
- Prize: $250 total, shared by the 50 highest-ranked entries
- Entry: a public GitHub repository under the MIT license, with `main.py` at its root
- Image: 1024×1024 PNG, about 109 KiB (limit 1 MiB), six stories

## Determinism

```sh
python3 main.py && sha256sum /output/entry.png
python3 main.py && sha256sum /output/entry.png
```

The two hashes must match. The program makes no network requests and needs nothing beyond the Python standard library: it copies the `entry.png` stored in this repository into `/output/entry.png`.

`build_image.py` is the local PIL script that drew `entry.png`; the entry itself does not run it.
