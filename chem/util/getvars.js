const { question: read } = require('readline-sync');

function getVars(obj) {
  let ans = {}
  for (q in obj) {
    ans[q] = obj[q](read(q + "? "))
  }
  return ans
}

module.exports = getVars;
