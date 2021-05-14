import Currency from './3-currency'

export default class Pricing {
  constructor (amount, currency) {
    this._amount = amount
    this._currency = currency
  }

  displayFullPrice () {
    return `${this.amount} ${this.currency.displayFullCurrency()}`
  }

  static convertPrice (amount, conversionRate) {
    return (amount * conversionRate)
  }

  get amount () {
    const amount = this._amount
    return (amount)
  }

  set amount (amount) {
    const setAmount = this._amount = amount
    return (setAmount)
  }

  get currency () {
    const currency = this._currency
    return (currency)
  }

  set currency (currency) {
    const setCurrency = this._currency = currency
    return (setCurrency)
  }
}
