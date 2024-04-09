---
title: WarGames
tags:
  - wargame
---

```dataview
TABLE WITHOUT ID
game AS "Game",
lvl AS "Level",
password AS "Password"
FROM "03-WarGames"
WHERE title != "WarGames"
SORT number(lvl) DESC
```
