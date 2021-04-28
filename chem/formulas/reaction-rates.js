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
  m = totalM - 1
  if (m === 0) return `1/s`
  if (m === 1) return `1/M*s`
  return `1/(M^${m} * s)`
}

function concentration(rate, k) {
  return sqrt( rate / k )
}

module.exports = {
  k, // (totalM)
  concentration, // (rate, k)
}
