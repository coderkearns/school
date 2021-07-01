// M = Molarity (mol/L)
// r = R constant
// t = temperature (in Kelvins)

const { i } = require("./constants")

function osmoticPressure(M, r, t) {
  return i * M * r * t
}

module.exports = osmoticPressure
