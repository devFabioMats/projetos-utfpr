// Produto final
class Aluno {
  nome!: string;
  idade!: number;
  matricula?: string;
  curso?: string;
  email?: string;
  telefone?: string;
  endereco?: string;
  historicoEscolar: Record<string, string> = {};

  mostrar(): void {
    console.log({
      nome: this.nome,
      idade: this.idade,
      matricula: this.matricula || '',
      curso: this.curso || '',
      email: this.email || '',
      telefone: this.telefone || '',
      endereco: this.endereco || '',
      historicoEscolar: Object.entries(this.historicoEscolar)
        .map(([tipo, descricao]) => `${tipo}: ${descricao}`)
        .join(", "),
    });
  }
}

interface IAlunoBuilder {
  setDadosPessoais(nome: string, idade: number): IAlunoBuilder;
  setMatricula(matricula: string, curso: string): IAlunoBuilder;
  setContato(telefone: string, email: string): IAlunoBuilder;
  setEndereco(endereco: string): IAlunoBuilder;
  addHistorico(tipo: string, descricao: string): IAlunoBuilder;
  build(): Aluno;
}

// Builder 1
class AlunoBuilder implements IAlunoBuilder {
  private aluno: Aluno;

  constructor() {
    this.aluno = new Aluno();
  }

  reset():AlunoBuilder {
    this.aluno = new Aluno();
    return this
  }

  setDadosPessoais(nome: string, idade: number): AlunoBuilder {
    this.aluno.nome = nome;
    this.aluno.idade = idade;
    return this;
  }

  setMatricula(matricula: string, curso: string): AlunoBuilder {
    this.aluno.matricula = matricula;
    this.aluno.curso = curso;
    return this;
  }

  setContato(telefone: string, email: string): AlunoBuilder {
    this.aluno.telefone = telefone;
    this.aluno.email = email;
    return this;
  }

  setEndereco(endereco: string): AlunoBuilder {
    this.aluno.endereco = endereco;
    return this;
  }

  addHistorico(tipo: string, descricao: string): AlunoBuilder {
    this.aluno.historicoEscolar[tipo] = descricao;
    return this;
  }

  build(): Aluno {
    return this.aluno;
  }
}

// Builder 2 - com validacao
class AlunoValidacaoBuilder implements IAlunoBuilder {
  private aluno: Aluno;

  constructor() {
    this.aluno = new Aluno();
  }

  setDadosPessoais(nome: string, idade: number): IAlunoBuilder {
    if (!nome || nome.trim().length < 2) {
      throw new Error("Nome inválido");
    }
    if (idade <= 0 || idade > 100) {
      throw new Error("Idade inválida");
    }
    this.aluno.nome = nome.trim();
    this.aluno.idade = idade;
    return this;
  }

  setMatricula(matricula: string, curso: string): IAlunoBuilder {
    if (!matricula || matricula.trim().length === 0) {
      throw new Error("Matrícula inválida");
    }
    if (!curso || curso.trim().length === 0) {
      throw new Error("Curso inválido");
    }
    this.aluno.matricula = matricula.trim();
    this.aluno.curso = curso.trim();
    return this;
  }

  setContato(telefone: string, email: string): IAlunoBuilder {
    const telefoneRegex = /^\d{4}\d?-?\d{4}$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (telefone && !telefoneRegex.test(telefone)) {
      throw new Error("Telefone inválido");
    }
    if (email && !emailRegex.test(email)) {
      throw new Error("Email inválido");
    }
    this.aluno.telefone = telefone;
    this.aluno.email = email;
    return this;
  }

  setEndereco(endereco: string): IAlunoBuilder {
    if (!endereco || endereco.trim().length === 0) {
      throw new Error("Endereço inválido");
    }
    this.aluno.endereco = endereco.trim();
    return this;
  }

  addHistorico(tipo: string, descricao: string): IAlunoBuilder {
    if (!tipo || tipo.trim().length === 0) {
      throw new Error("Tipo de histórico inválido");
    }
    if (!descricao || descricao.trim().length === 0) {
      throw new Error("Descrição de histórico inválida");
    }
    this.aluno.historicoEscolar[tipo.trim()] = descricao.trim();
    return this;
  }

  build(): Aluno {
    // Verifica campos obrigatórios antes de construir
    if (!this.aluno.nome || !this.aluno.idade || !this.aluno.matricula) {
      throw new Error("Dados incompletos do aluno");
    }
    return this.aluno;
  }
}

class DiretorAlunoBuilder {
    private  builder: IAlunoBuilder;

    public constructor(builder: IAlunoBuilder) {
        this.builder = builder;
    }

    public makeAlunoSimples(nome:string, email:string): Aluno {
        this.builder.setDadosPessoais(nome, 18)
                     .setMatricula("NOVA_MATRICULA", "Computação")
                     .setContato("", email);
        return this.builder.build();
    }

    public makeAlunoCompleto(nome:string, idade:number, matricula:string, curso:string, email:string, telefone:string, endereco:string): IAlunoBuilder {
        this.builder.setDadosPessoais(nome, idade)
                     .setMatricula(matricula, curso)
                     .setContato(telefone, email)
                     .setEndereco(endereco);
        return this.builder;
    }

}

// ---------- Uso ----------

const aluno1 = new AlunoValidacaoBuilder()
  .setDadosPessoais("Alice", 20)
  .setMatricula("12345", "Engenharia de Software")
  .setContato("91234-5678", "alice@email.com")
  .setEndereco("Rua A, 123")
  .addHistorico("Matemática", "A")
  .addHistorico("Física", "B")
  .build();

aluno1.mostrar();

const aluno2 = new AlunoBuilder()
  .setDadosPessoais("Bob", 22)
  .setContato("99876-5432", "bob@email.com")
  .setEndereco("Rua B, 456")
  .build();

aluno2.mostrar();

const diretor = new DiretorAlunoBuilder(new AlunoValidacaoBuilder())
const aluno3 = diretor.makeAlunoSimples("Joao", "joao@email.com");
aluno3.mostrar()