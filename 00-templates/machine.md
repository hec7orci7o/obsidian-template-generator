<%*
const API_TOKEN = "YOUR-API-TOKEN-GOES-HERE"
%><%*
let filename = await tp.system.prompt("Machine name:"); 

const { info } = await tp.obsidian.requestUrl({
  url: `https://www.hackthebox.com/api/v4/machine/profile/${filename}`,
  headers: { Authorization: `Bearer ${API_TOKEN}` }
}).then(r => r.json)
const ip = info.ip ?? "Disconected"
%>---
title: <% info.name %>
difficulty: <% info.difficultyText %>
os: <% info.os %>
release_date: <% moment(info.release).format('DD MMM YYYY') %>
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date() %>
user: 
root: 
tags:
- machine

---

<div style="display: flex; align-items: center;">
	<img
		src="https://www.hackthebox.com<% info.avatar %>"
		style="width: 5rem; height: 5rem;"
	/>
	
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Difficulty
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				<% info.difficultyText %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				OS
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				<% info.os %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
Release Date
			</span>
			<span style="font-size: 0.875rem; line-height: 1.5;"><% moment(info.release).format('DD MMM YYYY') %></span>
		</li>
	</ul>
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				IP
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				<% ip %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				User 🏴‍☠️
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  ---
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Root 🏴‍☠️
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  ---
			</span>
		</li>
	</ul>
</div>

---
## Statistics
<%*
const { info: matrix } = await tp.obsidian.requestUrl({
  url: `https://www.hackthebox.com/api/v4/machine/graph/matrix/${info.id}`,
  headers: { Authorization: `Bearer ${API_TOKEN}` }
}).then(r => r.json)
const {aggregate, maker, user} = matrix
const ma = JSON.stringify(Object.values(aggregate))
const mm = JSON.stringify(Object.values(maker))
const mu = JSON.stringify(Object.values(user))
%>```chart
type: radar
labels: [ENUM,REAL,CVE,CUSTOM,CTF]
series:
    - title: Maker
	  data: <% mm %>
    - title: User
      data: <% mu %>
    - title: Aggregate
	  data: <% ma %>
width: 50%
rMin: 0
```

## Rating

<%*
const { info: graph } = await tp.obsidian.requestUrl({
  url: `https://www.hackthebox.com/api/v4/machine/graph/owns/difficulty/${info.id}`,
  headers: { Authorization: `Bearer ${API_TOKEN}` }
}).then(r => r.json)

let buser = [];
let broot = [];

for (const key in graph) {
	buser.push(graph[key].user);
	broot.push(graph[key].root);
}
buser = JSON.stringify(buser)
broot = JSON.stringify(broot)
%>```chart
type: bar
labels: [PIECE OF CAKE,VERY EASY,EASY,NOT TOO EASY,MEDIUM,A BIT HARD,HARD,EXTREMELY HARD,INSANE,BRAINFUCK!]
series:
    - title: User
	  data: <% buser %>
	- title: Root
	  data: <% broot %>
width: 70%
```

---
## Walkthrough

### Enumeration

```bash
```

### Foothold

```bash
```

### Exploitation

```bash
```

### Post Exploitation

```bash
```

### Lateral Movement

```bash
```

### Privilege Escalation

```bash
```

---

## Appendices

<%*
const path = "/02-Machines/" + filename + "/" 
await this.app.vault.createFolder(tp.obsidian.normalizePath(path))
await this.app.vault.createFolder(tp.obsidian.normalizePath(path + "assets"))
await tp.file.rename(filename)
await tp.file.move(path + filename)
%>