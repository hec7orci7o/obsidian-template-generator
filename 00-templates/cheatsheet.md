<%*
const filename = await tp.system.prompt("Cheatsheet name:"); 
const path = "/01-CheatSheets/" + filename 
await tp.file.rename(filename)
await tp.file.move(path)
%>---
title: <% filename %>
difficulty: 
tier: 
type: 
tags:
- cheatsheet
---

# Section A

| **Command** | **Description** |
| :---------: | --------------- |
|             |                 |

# Section B

| **Command**    | **Description** |
| :------------: | --------------- |
|                |                 |
| **Subsection** |                 |
|                |                 |
| **Subsection** |                 |
|                |                 |

# Misc


