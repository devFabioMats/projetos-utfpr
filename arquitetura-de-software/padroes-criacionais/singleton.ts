class Singleton {
    private static instance: Singleton;

    private constructor() { }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }

        return Singleton.instance;
    }

    public fazAlgumaCoisa() {
        // TODO ...
    }
}


function clientCode() {
    const s1 = Singleton.getInstance();
    const s2 = Singleton.getInstance();

    if (s1 === s2) {
        console.log('Singleton funcionou, ambas as variáveis contêm a mesma instância.');
    } else {
        console.log('Singleton falhou, as variáveis contêm instâncias diferentes.');
    }
}

clientCode();