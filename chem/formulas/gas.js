/* Gas Formulas:

// Pressure and Volume

PV = nRT

P = pressure
V = volume
n = moles
R = constant (see contants.r)
T = temperature


PV = mRT / (MW)

P = pressure
V = volume
m = mass
R = constant (see contants.r)
T = temperature
MW = molecular weight

// Density

d_new = d_old * ( newV / oldV ) * ( oldP / newP )

d = density
V = volume
P = pressure

d = P(MW) / RT

d = density
P = pressure
MW = molecular weight
R = constant (see vars.constants.r)
T = temperature

// Combined Gas

newV = oldV * ( Pold / Pnew ) * ( Tnew / Told )
newP = oldP * ( Vold / Vnew ) * ( Tnew / Told )
newT = oldT * ( Vold / Vnew ) * ( Pold / Pnew )


*/

// PV = nRT
const nRT = {
  // V = nRT / P
  v: (p, n, r, t) => (n * r * t) / p,
  // P = nRT / V
  p: (v, n, r, t) => (n * r * t) / v,
}

// PV = mRT / (MW)
const mRTmw = {
  // V = ( mRT / (MW) ) / P
  v: (p, mw, m, r, t) => (m * r * t) / mw / p,
  // P = ( mRT / (MW) ) / V
  p: (v, mw, m, r, t) => (m * r * t) / mw / v,
}

// d = P(MW) / RT
const d_PmwRT = (p, mw, r, t) => (p * mw) / (r * t)

// d_new = d_old * ( newV / oldV ) * ( oldP / newP )
const d_dVP = (d, ov, nv, op, np) => d * (nv / ov) * (op / np)

// Combined Gas
const combinedGas = {
  // newV = oldV * ( Pold / Pnew ) * ( Tnew / Told )
  v: (v, op, np, ot, nt) => v * (op / np) * (nt / ot),
  // newP = oldP * ( Vold / Vnew ) * ( Tnew / Told )
  p: (p, ov, nv, nt, ot) => p * (ov / nv) * (nt / ot),
  // newT = oldT * ( Vold / Vnew ) * ( Pold / Pnew )
  t: (t, ov, nv, op, np) => t * (ov / np) * (op / np),
}

module.exports = {
  nRT,
  // { v, p }
  // v(p, n, r, t)
  // p(v, n, r, t)

  mRTmw,
  // { v, p }
  // v(p, mw, m, r, t)
  // p(v, mw, m, r, t)

  d_PmwRT,
  // (p, mw, r, t)

  d_dVP,
  // (d, ov, nv, op, nv)

  combinedGas,
  // { v, p, t }
  // v(v, op, np, ot, nt)
  // p(p, ov, nv, nt, ot)
  // t(t, ov, nv, op, np)
}
