
const pressureUnits = {
  1: "atm",
  2: "mmHg",
  3: "torr",
  4: "kPa"
}

const R = {
  atm: 0.0821,
  mmHg: 62.4,
  torr: 62.4,
  kPa: 8.31
}

const PI = 3.14 // or Math.PI

const i = 1

module.exports = { pressureUnits, R, PI, i }
