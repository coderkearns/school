// M = Molarity (mol/L)
// r = R constant
// t = temperature (in Kelvins)

function osmoticPressure(M, r, t) {
  return M*r*t
}

module.exports = osmoticPressure
