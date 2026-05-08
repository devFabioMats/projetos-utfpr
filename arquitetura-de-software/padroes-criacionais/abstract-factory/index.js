class WebButton {
  render() {
    return "Web button rendered";
  }
}

class WebInput {
  render() {
    return "Web input rendered";
  }
}

class MobileButton {
  render() {
    return "Mobile button rendered";
  }
}

class MobileInput {
  render() {
    return "Mobile input rendered";
  }
}

class WebUIFactory {
  createButton() {
    return new WebButton();
  }

  createInput() {
    return new WebInput();
  }
}

class MobileUIFactory {
  createButton() {
    return new MobileButton();
  }

  createInput() {
    return new MobileInput();
  }
}

function buildScreen(factory) {
  const button = factory.createButton();
  const input = factory.createInput();
  return [button.render(), input.render()];
}

const webScreen = buildScreen(new WebUIFactory());
const mobileScreen = buildScreen(new MobileUIFactory());

console.log("Web:", webScreen);
console.log("Mobile:", mobileScreen);
