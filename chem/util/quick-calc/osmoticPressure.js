const getVars = require("../getvars")
const parse = require("../parsers")

const { R } = require("../../vars/constants")
const { molarity } = require("../../formulas/solutions")
const osmoticPressure = require("../../vars/osmotic-pressure")
const mol = require("../../vars/mol")

module.exports = () => {
  args = getVars({
    mass: parse.float,
    mw: parse.float,
    volume: parse.float,
    temperature: parse.float,
    ptype: parse.string
  })

  let r = R.get(args.ptype)
  let M = molarity(mol(args.mass, args.mw), args.volume)

  let ans = osmoticPressure(M, r, args.temperature)
  console.log(`π = ${ans} ${args.ptype}`)
}
