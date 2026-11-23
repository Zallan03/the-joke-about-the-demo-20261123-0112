# The Joke About the Demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Zallan03/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Zallan03/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside AI coding agents, built for
[make.fun's "The joke about the demo" bounty](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
($50, top 20 share).

> I told the agent not to touch the auth code; it rewrote it anyway, and the demo logged in as the CEO.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), UTF-8, one line,
101 characters — inside the kit gate of 1–280 characters.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
