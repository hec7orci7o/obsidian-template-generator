<%*
const level = await tp.system.prompt("Bandit lvl: (1)"); 
const path = "/03-WarGames/bandit/Bandit " + level 
await tp.file.rename("Bandit " + level)
await tp.file.move(path)
%>---
lvl: <% level %>
game: bandit
password: 
tags:
- wargame
- bandit
---

## Level Goal

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar nisl et sapien mollis egestas. Cras ut viverra nisl. Quisque maximus blandit enim, ac elementum nulla elementum et. Nulla facilisi. Donec nec rutrum ante, eget luctus erat. Ut sit amet pulvinar augue. Integer vel lobortis tortor. Praesent porta, diam eu fringilla hendrerit, felis est condimentum leo, id commodo lorem libero in risus. Quisque pulvinar feugiat fringilla. 

---

```bash
```
