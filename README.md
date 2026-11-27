[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/intan151/makefun-boss-one-word-01/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/intan151/makefun-boss-one-word-01/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

# One Word for the Boss

A deterministic Python entry for the make.fun competition [One Word for the Boss](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735). It writes exactly one word describing the boss.

> Gasbag

Why this word: the boss talks — long meetings, longer monologues, and every "quick sync" turns into a sermon while the actual work waits. Gasbag is the word a colleague mutters at lunch after the third all-hands of the week, and everyone at the table laughs because they have all sat through the same hot air. It is funny on its own, it rings true about a real boss habit, and it is not the first word anyone reaches for.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the word (exactly one word, 1–30 characters, no whitespace) and writes it to `/output/entry.txt`, then reads it back and asserts it matches. Run it with `python3 main.py`.
