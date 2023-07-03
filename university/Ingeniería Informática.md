---
type: misc
---

## Estadísticas

```button
name Actualizar
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

### Duración media graduados

```chart
type: line
labels: [2013–2014,2014–2015,2015–2016,2016-2017,2017-2018,2018-2019,2019-2020,2020-2021,2021-2022]
series:
    - title: Zaragoza
	  data: [4,4.7,4.62,4.95,5.35,5.11,4.79,4.88,4.87]
	- title: Teruel
	  data: [4,5,5,5.67,6,6.11,5.36,5.69,6]
width: 70%
max: 25
```

### Tasas de abandono/graduación

```chart
type: line
labels: [2010–2011,2011–2012,2012–2013,2013–2014,2014–2015,2015–2016,2016-2017,2017-2018,2018-2019,2019-2020]
series:
    - title: Abandono (Z)
	  data: [56.58,42.86,40,28.4,51.95,33.33,23.26,22.73,19.10,0]
	- title: Graduados (Z)
	  data: [23.68,30,45.33,50.62,33.77,38.46,56.98,53.41,47.19,2.08]
	- title: Abandono (T)
	  data: [46.67,45.45,46.67,34.48,47.83,50,34.62,25.81,28,0]
	- title: Graduados (T)
	  data: [46.67,9.09,20,6.9,13.04,7.14,23.08,32.26,28,11.11]
width: 70%
```

