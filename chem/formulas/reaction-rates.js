/* Reaction Rate Formulas:

rate = k[X]m

k = rate / [X]
k = (M/s) / [X]
k = (M/s) / M
k = 1/s

// k:
k = 1 / M^(totalM - 1) * s

// concentration:
[X] = sqrt( rate / k )

*/

const sqrt = require("../util/sqrt")

function k(totalM) {
  if (isNaN(totalM)) return NaN
  if (totalM === 0) return `Ms^-1`
  if ((totalM - 1) === 0) return `s^-1`
  if ((totalM - 1) === 1) return `M^-1s^-1`
  return `M^-${(totalM - 1)}s^-1`
}

function concentration(rate, k) {
  return sqrt( rate / k )
}

module.exports = {
  k, // (totalM)
  concentration, // (rate, k)
}
