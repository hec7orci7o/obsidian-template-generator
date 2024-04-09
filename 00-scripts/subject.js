function getSubject({ html }) {
  const data = {};
  const headers = html
    .match(/<th\b[^>]*>(.*?)<\/th>/g)
    .map(th => th.replace(/<\/?th\b[^>]*>/g, '').trim().toLowerCase().replaceAll(" ", "_"));

  html
    .match(/<td\b[^>]*>(.*?)<\/td>/g)
    .map((th, index) => {
      const text = th.replace(/<\/?td\b[^>]*>/g, '').trim()
      data[headers[index]] = text
    });

  data["code"] = Number(data["code"])
  data["year"] = Number(data["year"])
  data["ects"] = Number(data["ects"])
  data["instructors"] = data["instructors"]
    .match(/<a\b[^>]*>(.*?)<\/a>/g)
    .map(th => th.replace(/<\/?a\b[^>]*>/g, '').trim().toLowerCase())
    .map(i => i.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('_'))
  delete data["recommended_bibliography"]

  return data
}

module.exports = getSubject