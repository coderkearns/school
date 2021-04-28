const fs = require('fs');

let files = fs.readdirSync("./quick-calc")

let f = ""

for (let file of files) {
  f += file.replace(".js", "")
  f += "\t"
}

console.log(f)
