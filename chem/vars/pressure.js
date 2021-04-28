class Pressure {
  // Create new Pressure
  constructor({ atm, mmHg, torr, kPa }) {
    if (atm) this.loadAtm(atm)
    if (mmHg) this.loadMmHg(mmHg)
    if (torr) this.loadTorr(torr)
    if (kPa) this.loadKPa(kPa)
  }

  // Getters
  get atm() {
    return this._atm
  }
  get mmHg() {
    return this._mmHg
  }
  get torr() {
    return this._torr
  }
  get kPa() {
    return this._kPa
  }

  // Setters
  set atm(v) {
    this.loadAtm(v)
  }
  set mmHg(v) {
    this.loadMmHg(v)
  }
  set torr(v) {
    this.loadTorr(v)
  }
  set kPa(v) {
    this.loadKPa(v)
  }

  // From atm
  static fromAtm(atm) {
    return new Pressure({ atm })
  }
  // From mmHg
  static fromMmHg(mmHg) {
    return new Pressure({ mmHg })
  }
  // From torr
  static fromTorr(torr) {
    return new Pressure({ torr })
  }
  // From kPa
  static fromKPa(kPa) {
    return new Pressure({ kPa })
  }

  // Convert from atm
  static atmToMmHg(atm) {
    return atm * 760
  }
  static atmToTorr(atm) {
    return Pressure.atmToMmHg(atm)
  }
  static atmToKPa(atm) {
    return atm * 101.3
  }

  // Convert from mmHg
  static mmHgToAtm(mmHg) {
    return mmHg / 760
  }
  static mmHgToTorr(mmHg) {
    return mmHg
  }
  static mmHgToKPa(mmHg) {
    return (mmHg / 760) * 101.3
  }

  // Convert from torr
  static torrToAtm(torr) {
    return Pressure.mmHgToAtm(torr)
  }
  static torrToMmHg(torr) {
    return torr
  }
  static torrToKPa(torr) {
    return Pressure.mmHgToKPa(torr)
  }

  // Convert from kPa
  static kPaToAtm(kPa) {
    return kPa / 101.3
  }
  static kPaToMmHg(kPa) {
    return (kPa / 101.3) * 760
  }
  static kPaToTorr(kPa) {
    return Pressure.kPaToMmHg(kPa)
  }

  // Loaders
  loadAtm(atm) {
    this._atm = atm
    this._mmHg = Pressure.atmToMmHg(atm)
    this._torr = Pressure.atmToTorr(atm)
    this._kPa = Pressure.atmToKPa(atm)
  }
  loadMmHg(mmHg) {
    this._atm = Pressure.mmHgToAtm(mmHg)
    this._mmHg = mmHg
    this._torr = mmHg
    this._kPa = Pressure.mmHgToKPa(mmHg)
  }
  loadTorr(torr) {
    this._atm = Pressure.torrToAtm(torr)
    this._mmHg = torr
    this._torr = torr
    this._kPa = Pressure.torrToKPa(torr)
  }
  loadKPa(kPa) {
    this._atm = Pressure.kPaToAtm(kPa)
    this._mmHg = Pressure.kPaToMmHg(kPa)
    this._torr = Pressure.kPaToTorr(kPa)
    this._kPa = kPa
  }
}

module.exports = Pressure
