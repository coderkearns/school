class Temp {
  constructor({ c, k, f }) {
    if (c) this.loadC(c)
    if (k) this.loadK(k)
    if (f) this.loadF(f)
  }

  // Getters
  get c() {
    return this._c
  }
  get k() {
    return this._k
  }
  get f() {
    return this._f
  }

  // Setters
  set c(v) {
    this.loadC(v)
  }
  set k(v) {
    this.loadK(v)
  }
  set f(v) {
    this.loadF(v)
  }

  // Create from temp
  static fromC(c) {
    return new Temp({ c })
  }
  static fromK(k) {
    return new Temp({ k })
  }
  static fromF(f) {
    return new Temp({ f })
  }

  // Convert Celsius and Kelvin
  static CtoK(c) {
    return c + 273
  }
  static KtoC(k) {
    return k - 273
  }

  // Convert Farenhiet and Celsius
  static FtoC(f) {
    return (f - 32) * (5 / 9)
  }
  static CtoF(c) {
    return c / (5 / 9) + 32
  }

  // Convert Kelvin and Farenhiet
  static KtoF(k) {
    return Temp.CtoF(Temp.KtoC(k))
  }
  static FtoK(f) {
    return Temp.CtoK(Temp.FtoC(f))
  }

  // Loaders
  loadC(c) {
    this._c = c
    this._k = Temp.CtoK(c)
    this._f = Temp.CtoF(c)
  }
  loadK(k) {
    this._c = Temp.KtoC(k)
    this._k = k
    this._f = Temp.KtoF(k)
  }
  loadF(f) {
    this._c = Temp.FtoC(f)
    this._k = Temp.FtoK(f)
    this._f = f
  }
}

module.exports = Temp
