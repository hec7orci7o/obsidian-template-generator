<%*
const subject_code = await tp.system.prompt("Subject code:"); 
const anyo_academico: new Date().getMonth() + 1 >= 8 
	  ? new Date().getFullYear()
	  : (new Date().getFullYear() - 1).toString(), 
const config = {
  anyo_academico,
  asignatura_id: Number(subject_code),
  // CUSTOMIZE: CHANGE THESE VALUES
  estudio_id: 20230148,	// CHANGE ME
  centro_id: 110,				// CHANGE ME
  plan_id_nk: 439,			// CHANGE ME
};

const params = new URLSearchParams(config)
const baseUrl = "https://estudios.unizar.es/estudio/asignatura?" + params

const response = await tp.obsidian.requestUrl(baseUrl)
const subject = tp.user.subject({ html: response.text })
%><%*
const path = "/01-Subjects/" + subject.name + "/" 
await this.app.vault.createFolder(tp.obsidian.normalizePath(path))
await this.app.vault.createFolder(tp.obsidian.normalizePath(path)+"/assets")
await tp.file.rename(subject.name)
await tp.file.move(path + subject.name)
%>---
code: <% subject.code %>
name: <% subject.name %>
year: <% subject.year %>
term: <% subject.term %>
type: <% subject.type %>
ects: <% subject.ects %>
language: <% subject.language %>
tags:
- subject

---
<div style="display: grid; grid-template-columns: repeat(7, 1fr); align-items: center;">
		<img
			src="https://robohash.org/<% subject.code %>" 
			style="width: 5rem; height: 5rem;"
		/>
	
	<ul style="grid-column: span 3;">
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Code
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(16, 185, 129, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); box-shadow: inset 0 1px 1px rgba(16, 185, 129, 0.2);">
				<% subject.code %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Year
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  <% subject.year %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Term
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  <% subject.term %>
			</span>
		</li>
	</ul>
	<ul style="grid-column: span 3;">
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Type
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  <% subject.course_type %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				ECTS
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			  <% subject.ects %>
			</span>
		</li>
		<li>
			<span style="font-size: 0.8rem; font-weight: 600; line-height: 1.5; letter-spacing: 0.025em;">
				Language
			</span>
			<span style="display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: rgba(156, 163, 175, 0.1); padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: #9CA3AF; border: 1px solid rgba(156, 163, 175, 0.2); box-shadow: inset 0 1px 1px rgba(156, 163, 175, 0.2);">
			 <% subject.ects %>
			</span>
		</li>
	</ul>
</div>

---

<%* 
const academic_plan = `https://sia.unizar.es/doa/consultaPublica/look[conpub]MostrarPubGuiaDocAs?entradaPublica=true&idiomaPais=es.ES&_anoAcademico=${config.anyo_academico}&_codAsignatura=${subject_code}`

tR += "[academic plan](" + academic_plan + ")\n"
%>
# Instructors

<%*
subject.instructors.forEach(i => tR += `- [${i.replaceAll("_"," ")}](https://directorio.unizar.es/#/personas?cadena=${i})\n`)
%>
# Notes