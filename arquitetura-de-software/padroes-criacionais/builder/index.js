class Computer {
  constructor() {
    this.cpu = "";
    this.ram = "";
    this.storage = "";
    this.gpu = "";
  }
}

class ComputerBuilder {
  constructor() {
    this.computer = new Computer();
  }

  setCPU(cpu) {
    this.computer.cpu = cpu;
    return this;
  }

  setRAM(ram) {
    this.computer.ram = ram;
    return this;
  }

  setStorage(storage) {
    this.computer.storage = storage;
    return this;
  }

  setGPU(gpu) {
    this.computer.gpu = gpu;
    return this;
  }

  build() {
    return this.computer;
  }
}

const officeComputer = new ComputerBuilder()
  .setCPU("Intel i5")
  .setRAM("16GB")
  .setStorage("512GB SSD")
  .build();

const gamingComputer = new ComputerBuilder()
  .setCPU("Intel i7")
  .setRAM("32GB")
  .setStorage("1TB SSD")
  .setGPU("RTX 4070")
  .build();

console.log("Office computer:", officeComputer);
console.log("Gaming computer:", gamingComputer);
