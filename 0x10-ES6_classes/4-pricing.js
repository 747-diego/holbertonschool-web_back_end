// import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  displayFullPrice() {
    const amount = this._amount;
    const name = this._currency.name;
    const code = this._currency.displayFullCurrency();
    return (`${amount} ${name} (${code})`);
  }

  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }

  set amount(amount) {
    const setAmount = this._amount = amount;
    return (setAmount);
  }

  get amount() {
    const amount = this._amount;
    return (amount);
  }

  set currency(currency) {
    const setCurrency = this._currency = currency;
    return (setCurrency);
  }

  get currency() {
    const currency = this._currency;
    return (currency);
  }
}
