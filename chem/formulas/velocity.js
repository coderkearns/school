/* Velocity Formulas:

u_rms = √( 3*R*T / mw )

*/

const sqrt = require("../util/sqrt")

const R = 8.31 * (10**3)

function u(t, mw) {
  return sqrt( (3*R*t) / mw )
}


module.exports = u // (t, mw)
