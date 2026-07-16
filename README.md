<div align="center">

# Haunted Mansion Rescue

### A Python command-line adventure through a haunted estate

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Game](https://img.shields.io/badge/Game-Text%20Adventure-6f42c1?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-Command%20Line-111111?style=for-the-badge)

[Overview](#overview) · [Game Map](#game-map) · [How to Play](#how-to-play) · [Run the Game](#run-the-game)

</div>

---

## Overview

| | |
|---|---|
| **Project** | Haunted Mansion Rescue |
| **Language** | Python |
| **Game type** | Room-based command-line adventure |
| **Starting point** | Great Hall |
| **Final location** | Dungeon |
| **Objective** | Explore the mansion, collect useful items and rescue your friend from the ghost |

The player navigates a haunted mansion by entering cardinal directions. Each room may contain an item, a new path or the route toward the final encounter in the dungeon.

## Game Map

```mermaid
flowchart TD
    GH[Great Hall]
    AT[Attic<br/>Flashlight]
    ST[Study<br/>Map]
    MU[Mudroom<br/>Boots]
    LA[Laboratory<br/>Potion]
    PA[Parlor<br/>Charm]
    BA[Basement<br/>Key]
    DU[Dungeon<br/>Friend and Ghost]

    GH -->|North| AT
    AT -->|East| ST
    GH -->|East| MU
    MU -->|North| LA
    GH -->|West| PA
    GH -->|South| BA
    BA -->|East| DU

    AT -->|South| GH
    ST -->|West| AT
    MU -->|West| GH
    LA -->|South| MU
    PA -->|East| GH
    BA -->|North| GH
    DU -->|West| BA
```

## How to Play

1. Begin in the **Great Hall**.
2. Enter `North`, `South`, `East` or `West`.
3. Explore rooms and collect available items.
4. Reach the **Dungeon** and rescue your friend.
5. Enter `quit` at any time to exit.

## Core Gameplay

```mermaid
flowchart LR
    A[Show current room] --> B[Read direction]
    B --> C{Valid move?}
    C -->|No| A
    C -->|Yes| D[Move to next room]
    D --> E[Collect room item]
    E --> F{Dungeon reached?}
    F -->|No| A
    F -->|Yes| G[Rescue friend and defeat ghost]
```

## Run the Game

```bash
git clone https://github.com/rypeguero/Text-Based-Game.git
cd Text-Based-Game
python haunted_mansion_rescue.py
```

## Python Concepts Demonstrated

`Functions` · `Dictionaries` · `Lists` · `Loops` · `Conditional Logic` · `User Input` · `String Handling` · `Game-State Tracking`

## Source Code

[**View `haunted_mansion_rescue.py`**](./haunted_mansion_rescue.py)

---

<div align="center">

**Ryan A. Peguero · Computer Science · Software Engineering**

</div>
