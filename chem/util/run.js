const args = require("minimist")(process.argv.slice(2))
const calc = require(`./quick-calc/${args._[0]}`)

calc()
