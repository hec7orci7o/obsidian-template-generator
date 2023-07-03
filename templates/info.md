---
title: {{name}}
difficulty: {{difficultyText}}
os: {{os}}
release_date: {{release}}
type: machine
---

<div
	style="display: flex; align-items: center;"
>
	<img
		src="https://www.hackthebox.com{{avatar}}"
		style="width: 5rem; height: 5rem;"
	/>
	
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Dificultad
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				{{difficultyText}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				SO
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				{{os}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Fecha Lanzamiento
			</span>
			<span style="font-size: 0.875rem; line-height: 1.5;">{{release}}</span>
		</li>
	</ul>
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				IP
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				{{ip}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Usuario 🏴‍☠️
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  ---
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Sistema 🏴‍☠️
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  ---
			</span>
		</li>
	</ul>
</div>

---

## Índice

- **Meow**
	- [Estadísticas](#Estadísticas)
	- [Valoración](#Valoración)
- **Pentest**
	- [[Pentest#Reconocimiento|Reconocimiento]]
	- [[Pentest#Explotación|Explotación]]
	- [[Pentest#Post-Explotación|Post-Explotación]]

---

## Estadísticas

```chart
type: radar
labels: [ENUM,REAL,CVE,CUSTOM,CTF]
series:
    - title: Creador
	  data: {{maker}}
    - title: Usuario
      data: {{user}}
width: 50%
```

## Valoración

```chart
type: bar
labels: [PIECE OF CAKE,VERY EASY,EASY,NOT TOO EASY,MEDIUM,A BIT HARD,HARD,EXTREMELY HARD,INSANE,BRAINFUCK!]
series:
    - title: User
	  data: {{bar_user}}
	- title: Root
	  data: {{bar_root}}
width: 70%
```
