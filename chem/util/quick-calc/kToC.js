const getVars = require("../getvars")
const parse = require("../parsers")

const Temp = require("../../vars/temp")

module.exports = () => {
  args = getVars({
    k: parse.float,
  })

  console.log(`C = ${Temp.KtoC(args.k)}`)
}
