const getVars = require("../getvars")
const parse = require("../parsers")

const calculateVolume = require("../../formulas/gas").mRTmw.v
const { R } = require("../../vars/constants")

module.exports = () => {
  args = getVars({
    pressure: parse.float,
    mw: parse.float,
    moles: parse.float,
    temperature: parse.float,
    ptype: parse.string
  })

  let r = R.get(args.ptype)
  let mass = args.mw * args.moles
  let volume = calculateVolume(args.pressure, args.mw, mass, r, args.temperature)
  console.log(`V = ${volume} L`)
}
