const LogResource = require('./log-resource');

class OrderServiceWithoutDIP {
  constructor() {
    this.logResource = new LogResource();
  }

  finalizeOrder(customer, amount) {
    this.logResource.log(
      `Pedido finalizado para ${customer}. Valor total: R$ ${amount.toFixed(2)}`
    );
  }
}

module.exports = OrderServiceWithoutDIP;
