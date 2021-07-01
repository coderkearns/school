// 3 signifigant digits:
function precise(num) {
  return Number.parseFloat(num).toPrecision(3)
}

module.exports = precise

module.exports.precisify = function(fn) {
  return (...args) => {
    return precise(fn(...args))
  }
}

module.exports.runPrecise = function(fn, ...args) {
  return precise(fn(...args))
}