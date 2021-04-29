const getVars = require("../getvars")
const parse = require("../parsers")

const { combinedGas } = require("../../formulas/gas")

function getV() {
  let args = getVars({
    oldV: parse.float,
    oldP: parse.float,
    newP: parse.float,
    oldT: parse.float,
    newT: parse.float,
  })
  console.log(`newV = ${combinedGas.v(args.oldV, args.oldP, args.newP, args.oldT, args.newT)} L`)
}
function getP() {
  let args = getVars({
    oldP: parse.float,
    oldV: parse.float,
    newV: parse.float,
    oldT: parse.float,
    newT: parse.float,
  })
  console.log(`newP = ${combinedGas.p(args.oldP, args.oldV, args.newV, args.oldT, args.newT)}`)
}
function getP() {
  let args = getVars({
    oldT: parse.float,
    oldV: parse.float,
    newV: parse.float,
    oldP: parse.float,
    newP: parse.float,
  })
  console.log(`newT = ${combinedGas.t(args.oldT, args.oldV, args.newV, args.oldP, args.newP)} K`)
}

module.exports = () => {
  let type = getVars({
    "What do you want (V, P, or T)": parse.string,
  })

  switch (type["What do you want (V, P, or T)"].toLowerCase()[0]) {
    case "v":
      return getV()
    case "p":
      return getP()
    case "t":
      return getT()
    default:
      console.log("Automatically using V!")
      return getV()
  }
}
