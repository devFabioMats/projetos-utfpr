class OrderServiceWithDIP {
  constructor(logger) {
    this.logger = logger;
  }

  finalizeOrder(customer, amount) {
    this.logger.log(
      `Pedido finalizado para ${customer}. Valor total: R$ ${amount.toFixed(2)}`
    );
  }
}

module.exports = OrderServiceWithDIP;
