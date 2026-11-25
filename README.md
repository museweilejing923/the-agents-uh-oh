# the-agents-uh-oh

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/museweilejing923/the-agents-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/museweilejing923/the-agents-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

The entry:

> whirring

8 characters, limit 99.

When an agent realises it is lost, it does not file a report — it makes a sound. This word is that sound: a drive spinning, a fan humming, a machine doing something audible while achieving nothing at all. It also works as a sound effect you can hear without any picture attached — the joke is audible, not explained. In a head-to-head vote the word has to land at a glance, sound like something a machine would actually blurt out, and feel fresher than the first obvious word anyone would type.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed word through a table of named rules and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The rules, in table order, are: contains letters, non-empty, no digits, within the 99-character limit, exactly one word, no control characters, no letter repeated three times in a row, not digits only, no leading or trailing space, and no double spaces or newlines.
