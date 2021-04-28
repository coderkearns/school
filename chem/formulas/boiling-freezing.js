/* Boiling and Freezing formula:

Δt_f = i*m*k_f
Δt_b = i*m*k_b

Δt = change in C° (freezing or boiling)
m = molality
k = constant (freezing or boiling) (provided in problem)

*/

const { constants:{i} } = require("../vars")

function t(m, k) {
  return i * m * k
}

module.exports = t // (m, k)
