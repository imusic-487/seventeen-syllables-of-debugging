# Seventeen Syllables of Debugging

[![Competition](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/imusic-487/seventeen-syllables-of-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/imusic-487/seventeen-syllables-of-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard)

## The entry

> Cursor blinks at three
> the log line swears it worked here
> but the code moved on

Three lines, 5-7-5 syllables, 79 characters. The picture is concrete:
a cursor blinking at three in the morning, a log line insisting the
code worked. The turn is the last line — the log is not lying, the
code simply moved on since it ran, so the truth it swears to is
already stale.

## What this repo does

This is an entry for the make.fun bounty
[u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605).
`main.py` writes the haiku — exactly as written — to
`/output/entry.txt`, and fails loudly if the text is not 1–200
characters, not exactly three lines, not 5-7-5 syllables, or only
white space. Nothing else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `main.py` — writes the haiku to `/output/entry.txt` and verifies it.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
