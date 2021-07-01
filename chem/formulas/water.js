const { pH, pOH, undo } = require("./ph-poh")
const { Kw, H, OH } = require("./water-ion")

const p = require("../util/precise")

const precise = returns => {
  Object.keys(returns).map(function(key, index) {
    returns[key] = p(returns[key])
  })
  return returns
}

function fromH(h) {
  let oh = OH(h)
  return precise({
    H: h,
    OH: oh,
    pH: pH(h),
    pOH: pOH(oh),
  })
}
function fromOH(oh) {
  let h = H(oh)
  return precise({
    H: h,
    OH: oh,
    pH: pH(h),
    pOH: pOH(oh),
  })
}

function fromPH(ph) {
  let h = undo(ph)
  let oh = OH(h)
  return precise({
    H: h,
    OH: oh,
    pH: ph,
    pOH: pOH(oh),
  })
}
function fromPOH(poh) {
  let oh = undo(poh)
  let h = H(oh)
  return precise({
    H: h,
    OH: oh,
    pH: pH(h),
    pOH: oh,
  })
}

module.exports = { fromH, fromOH, fromPH, fromPOH }
module.exports.from = { H: fromH, OH: fromOH, pH: fromPH, pOH: fromPOH }
