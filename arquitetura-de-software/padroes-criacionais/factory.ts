// Produto abstrato
interface Parser {
  parse(content: string): any;
}

// Produtos concretos
class JSONParser implements Parser {
  parse(content: string): any {
    console.log("Usando JSONParser");
    return JSON.parse(content);
  }
}

class CSVParser implements Parser {
  parse(content: string): any {
    console.log("Usando CSVParser");
    // Exemplo simples: quebra em linhas e depois em colunas
    return content.split("\n").map(line => line.split(","));
  }
}

class HTMLParser implements Parser {
  parse(content: string): any {
    console.log("Usando HTMLParser");
    // Apenas simulação: retorna tags encontradas
    return content.match(/<\w+>/g) || [];
  }
}

abstract class ParserFactory {
  abstract createParser(): Parser;

  process(content: string): any {
    const parser = this.createParser();
    return parser.parse(content);
  }
}

// Fábricas concretas
class JSONParserFactory extends ParserFactory {
  createParser(): Parser {
    return new JSONParser();
  }
}

class CSVParserFactory extends ParserFactory {
  createParser(): Parser {
    return new CSVParser();
  }
}

class HTMLParserFactory extends ParserFactory {
  createParser(): Parser {
    return new HTMLParser();
  }
}

// -------------------------
// Cliente
function main(factory: ParserFactory, content: string) {
  const tipo = "csv"; // poderia vir de config ou extensão do arquivo

  console.log("Resultado:", factory.process(content));
}

main(new JSONParserFactory(), '{"nome":"Ana","idade":25}');
main(new CSVParserFactory(), "nome,idade\nAna,25\nJoão,30");
main(new HTMLParserFactory(), "<html><body><h1>Título</h1></body></html>");