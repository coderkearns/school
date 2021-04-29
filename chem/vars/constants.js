
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
  kPa: 8.31,
  get (type) {
    type = type.toLowerCase().replaceAll("-", "").replaceAll("_", "").replaceAll(" ", "")
    switch (type) {
      case "atm":
        return this.atm
      case "mmhg":
        return this.mmHg
      case "torr":
        return this.torr
      case "kpa":
        return this.kPa
      default:
        console.log(`Can't use ${type} as R constant, using atm by default...`)
        return this.atm
    }
  }
}

const PI = 3.14 // or Math.PI

const i = 1

module.exports = { pressureUnits, R, PI, i }
