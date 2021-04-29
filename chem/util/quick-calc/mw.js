const getVars = require("../getvars")
const parse = require("../parsers")

const { R } = require("../../vars/constants")
const calculateMW = require("../../formulas/mw").mrtpv

module.exports = () => {
  args = getVars({
    mass: parse.float,
    temp: parse.float,
    pressure: parse.float,
    v: parse.float,
    ptype: parse.string
  })

  const r = R.get(args.ptype)
  const mw =  calculateMW(args.mass, r, args.temp, args.pressure, args.v)
  console.log(`MW = ${mw} g/mol`)
}
