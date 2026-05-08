class AppSettings {
  static instance = null;

  constructor() {
    if (AppSettings.instance) {
      return AppSettings.instance;
    }
    this.values = { language: "en", theme: "dark" };
    AppSettings.instance = this;
  }

  setValue(key, value) {
    this.values[key] = value;
  }

  getValue(key) {
    return this.values[key];
  }
}

const settingsA = new AppSettings();
const settingsB = new AppSettings();

settingsA.setValue("theme", "light");

console.log("Theme from A:", settingsA.getValue("theme"));
console.log("Theme from B:", settingsB.getValue("theme"));
console.log("Same instance:", settingsA === settingsB);
