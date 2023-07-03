---
title: {{Nombre}}
code: {{Código}}
curso: {{Curso}}
periodo: {{Periodo}} 
carácter: {{Carácter}}
creditos: {{Créditos}}
plazas: {{Plazas}}
idioma: {{Idioma}}
---

<div
	style="display: flex; align-items: center;"
>
	<a href="https://sia.unizar.es/doa/consultaPublica/look[conpub]MostrarPubGuiaDocAs?entradaPublica=true&idiomaPais=es.ES&_anoAcademico={{school_year}}&_codAsignatura={{Código}}" rel="noopener" target="_blank">
		<img
			src="https://www.hackthebox.com/storage/avatars/b55987f8ef9a42df2ad4b4c096e3824d.png"
			style="width: 5rem; height: 5rem;"
		/>
	</a>
	
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Código
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				{{Código}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Curso
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  {{Curso}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Periodo
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  {{Periodo}}
			</span>
		</li>
	</ul>
	<ul>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Carácter
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  {{Carácter}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Créditos
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  {{Créditos}}
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Plazas
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  {{Plazas}}
			</span>
		</li>
	</ul>
</div>

---

## Índice

%% Begin Waypoint %%
- **Prácticas**
- **Problemas**
- **Teoría**

%% End Waypoint %%

---

## Contacto

{{Profesores}}
## Estadísticas (curso pasado)

### Análisis de los indicadores del título

```chart
type: bar
labels: [Apro,Susp,No Pre,Recu]
series:
    - title: % Alumnos
	  data: {{analysis_data}}
width: 70%
max: {{analysis_data_max}}
labelColors: true
```

### Distribución de calificaciones

```chart
type: bar
labels: [MH,Sobresaliente,Notable,Aprobado,Suspenso, No Presentado, Otro]
series:
    - title: Alumnos
	  data: {{distributed_data}}
width: 70%
labelColors: true
```
