# It Now Works for the Cat

[![Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/argasap87/makefun-u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/argasap87/makefun-u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A meme for [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) — the funniest picture of an AI agent gone rogue.

## The joke

> **MY ROBOT VACUUM WENT ROGUE**
> **NOW IT'S THE CAT'S UBER**

The robot vacuum went rogue in the most domestic way possible: it quit
cleaning and now chauffeurs the cat around the living room — the cat
rides it like its own private Uber. One glance, no explanation needed.

## How it is built

`main.py` is a deterministic, offline compositor (Python + PIL). It reads
the AI-generated scene in `assets/scene.jpg` — a cat standing on a robot
vacuum in a sunlit living room — crops the generator's watermark strip
off the bottom edge, and lays it out as a classic top-text / bottom-text
meme on a 1024×1024 canvas with a thin white frame, writing
`/output/entry.png`. No network access at runtime; every input ships in
this repository.

## Run it

```sh
python3 main.py   # writes /output/entry.png (PNG, <= 1 MiB, 1024x1024)
```

## License

MIT — see [LICENSE](LICENSE).
