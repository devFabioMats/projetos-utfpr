// --- Interfaces (produtos abstratos) ---
interface Parser {
  parse(content: string): any;
}

interface Sanitizer {
  sanitize(content: string): string;
}

interface Serializer {
  serialize(data: any): string;
}

// --- JSON ---
class JSONParser implements Parser {
  parse(content: string): any {
    console.log("JSON Parser em uso");
    return JSON.parse(content);
  }
}

class JSONSanitizer implements Sanitizer {
  sanitize(content: string): string {
    console.log("JSON Sanitizer em uso");
    // Exemplo simples: remove espaços extras
    return content.trim();
  }
}

class JSONSerializer implements Serializer {
  serialize(data: any): string {
    console.log("JSON Serializer em uso");
    return JSON.stringify(data);
  }
}

// --- CSV ---
class CSVParser implements Parser {
  parse(content: string): any {
    console.log("CSV Parser em uso");
    return content.split("\n").map(line => line.split(","));
  }
}

class CSVSanitizer implements Sanitizer {
  sanitize(content: string): string {
    console.log("CSV Sanitizer em uso");
    // Remove linhas em branco
    return content.split("\n").filter(line => line.trim() !== "").join("\n");
  }
}

class CSVSerializer implements Serializer {
  serialize(data: any): string {
    console.log("CSV Serializer em uso");
    return data.map((row: string[]) => row.join(",")).join("\n");
  }
}


// --- HTML ---
class HTMLParser implements Parser {
  parse(content: string): any {
    console.log("HTML Parser em uso");
    return content.match(/<\w+>/g) || [];
  }
}

class HTMLSanitizer implements Sanitizer {
  sanitize(content: string): string {
    console.log("HTML Sanitizer em uso");
    // Remove scripts inseguros (exemplo simples)
    return content.replace(/<script.*?>.*?<\/script>/g, "");
  }
}

class HTMLSerializer implements Serializer {
  serialize(data: any): string {
    console.log("HTML Serializer em uso");
    return Array.isArray(data) ? data.join("") : String(data);
  }
}

// --- Abstract Factory ---
interface DataProcessingFactory {
  createParser(): Parser;
  createSanitizer(): Sanitizer;
  createSerializer(): Serializer;
}

// --- Fábricas concretas ---
class JSONFactory implements DataProcessingFactory {
  createParser(): Parser {
    return new JSONParser();
  }
  createSanitizer(): Sanitizer {
    return new JSONSanitizer();
  }
  createSerializer(): Serializer {
    return new JSONSerializer();
  }
}

class CSVFactory implements DataProcessingFactory {
  createParser(): Parser {
    return new CSVParser();
  }
  createSanitizer(): Sanitizer {
    return new CSVSanitizer();
  }
  createSerializer(): Serializer {
    return new CSVSerializer();
  }
}

class HTMLFactory implements DataProcessingFactory {
  createParser(): Parser {
    return new HTMLParser();
  }
  createSanitizer(): Sanitizer {
    return new HTMLSanitizer();
  }
  createSerializer(): Serializer {
    return new HTMLSerializer();
  }
}

// --- Cliente ---
function processFile(factory: DataProcessingFactory, content: string) {
  const sanitizer = factory.createSanitizer();
  const parser = factory.createParser();
  const serializer = factory.createSerializer();

  const cleanContent = sanitizer.sanitize(content);
  const data = parser.parse(cleanContent);
  const output = serializer.serialize(data);

  console.log("Resultado final:", output);
}

// ----------------------------
// Demonstração
const jsonContent = '{"nome":"Ana","idade":25}';
const csvContent = "nome,idade\nAna,25\nJoão,30\n";
const htmlContent = "<html><body><h1>Oi</h1><script>alert('xss')</script></body></html>";

console.log("\n--- JSON ---");
processFile(new JSONFactory(), jsonContent);

console.log("\n--- CSV ---");
processFile(new CSVFactory(), csvContent);

console.log("\n--- HTML ---");
processFile(new HTMLFactory(), htmlContent);
