
<%*
const anyo_academico: new Date().getMonth() + 1 >= 8 
	  ? new Date().getFullYear()
	  : (new Date().getFullYear() - 1).toString(), 
const config = {
  anyo_academico,
  // CUSTOMIZE: CHANGE THESE VALUES
  estudio_id: 20230148, // CHANGE ME
  centro_id: 110,       // CHANGE ME
  plan_id_nk: 439       // CHANGE ME
};

await tp.file.rename("dashboard-" + config.anyo_academico)

const params = new URLSearchParams(config)
const baseUrl = "https://estudios.unizar.es/estudio/asignaturas?" + params

const response = await tp.obsidian.requestUrl(baseUrl)
const subjects = tp.user.subjects({ html: response.text })
%>
<%*
tR += "| Year | Term | Code | Name | Type | Ects | Info | Places Language |\n"
tR += "| :-:  | :-   | :-:  | :-   | :-   | :-:  | :-   | :-              |\n"
subjects.forEach(r => tR += "|" + Object.values(r).join(" | ") + "|\n")
%>
