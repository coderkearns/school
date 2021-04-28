/* Molecular Weight Formulas:

MW = i * k * ( ( massSolute / Δt ) / kgSolovent )

MW = i * R * T * ( ( massSolute / osmoticPressure ) / literSolution )

*/

const { osmoticPressure, constants:{i} } = require("../vars")

function ikt(i, k, massSolute, t, kgSolovent) {
  return i * k * (massSolute / t / kgSolovent)
}

function rtmv(r, t, massSolute, literSolution) {
  return r * t * ( ( massSolute / osmoticPressure(massSolute, r, t) ) / literSolution)
}

module.exports = {
  ikt, // (i, k, massSolute, t, kgSolovent)
  rtmv, // (r, t, massSolute, literSolution)
}
