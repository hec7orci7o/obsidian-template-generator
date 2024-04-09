const headers = ["year", "term", "code", "name", "course_type", "ects", "", "number_of_places", "language"]

function fixTerm(term) { 
  if (term === "S1Semester 1") return "Semester 1"
  else if (term === "S2Semester 2") return "Semester 2"
  else if (term && term.includes("S1Semester 1") && term.includes("S2Semester 2")) return "Annual"
  else {
    return null
  }
}
function getText(html) {
  return html.replace(/<\/?[^>]+(>|$)/g, "").trim()
}

function getSubjects({ html }) {
  const data = html
    .match(/<tr\b[^>]*>(.*?)<\/tr>/g)
    .map(tr => {
      const rd = {}
      const cols = tr.match(/<td\b[^>]*>(.*?)<\/td>/g)
      cols?.forEach((td, index) => {
        const text = getText(td)
        rd[headers[index]] = text.trim()
      })
      rd.term = fixTerm(rd.term)
      rd.code = Number(rd.code)
      rd.year = Number(rd.year)
      rd.ects = Number(rd.ects)
      rd.number_of_places = rd.number_of_places === "-" ? null : Number(rd.number_of_places)
      return rd
    })
    
  return data.filter(r => Boolean(r.name))
}

module.exports = getSubjects
