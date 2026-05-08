class EmailNotifier {
  send(message) {
    return `Email sent: ${message}`;
  }
}

class SMSNotifier {
  send(message) {
    return `SMS sent: ${message}`;
  }
}

class NotifierFactory {
  createNotifier() {
    throw new Error("Method not implemented");
  }

  notify(message) {
    const notifier = this.createNotifier();
    return notifier.send(message);
  }
}

class EmailNotifierFactory extends NotifierFactory {
  createNotifier() {
    return new EmailNotifier();
  }
}

class SMSNotifierFactory extends NotifierFactory {
  createNotifier() {
    return new SMSNotifier();
  }
}

const emailFactory = new EmailNotifierFactory();
const smsFactory = new SMSNotifierFactory();

console.log(emailFactory.notify("Order confirmed"));
console.log(smsFactory.notify("Delivery is on the way"));
