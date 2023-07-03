---
type: misc
---

```button
name Nueva Asignatura
type link
action obsidian://shell-commands/?vault=university&execute=91z6tg4dnk
templater true
class "border-radius: 0.25rem; background-color: #4f46e5; padding: 0.5rem 0.75rem; font-size: 0.875rem; font-weight: 600; color: #ffffff; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 3px 1px rgba(0, 0, 0, 0.1); transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, transform; transition-duration: 75ms; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); line-height: 1.25; display: inline-block; text-align: center; white-space: nowrap; vertical-align: middle; user-select: none; border-width: 1px; border-style: solid; border-color: transparent; outline: none; outline-offset: 2px; }
  &:hover {
    background-color: #4338ca;
  }
  &:focus-visible {
    outline-color: #4f46e5;
    outline-style: auto;
    outline-width: 2px;
    outline-offset: 2px;
  }"
```

## Expediente

```chart
type: bar
labels: [Fo. Básica,Obligatoria,Optativa,TFG,Prácticas, Act Compl, Sin determinar]
series:
    - title: Minimos
	  data: [60,104,64,12,null,null,null]
	- title: Superados
	  data: [null,null,null,null,null,null,null]
	- title: Mat No Superados
	  data: [null,null,null,null,null,null,null]
width: 70%
```

```dataview
TABLE WITHOUT ID
code as Id, 
file.link AS "Nombre",
curso as Curso,
periodo as Periodo,
carácter as Carácter,
creditos as Créditos,
plazas as Plazas,
idioma as Idioma
FROM "Asignaturas"
WHERE state = "in progress"
SORT code ASC
```


