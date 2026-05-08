interface Prototype<T> {
  clone(): T;
}

class MeuPrototipo implements Prototype<MeuPrototipo> {
    public primitive: any;
    public component: object;
    public circularReference: ComponentWithBackReference;

    public constructor(primitive: any, component: object) {
        this.primitive = primitive;
        this.component = component;
        this.circularReference = new ComponentWithBackReference(this);
    }

    public clone(): this {
        const clone = Object.create(this);
        clone.component = Object.create(this.component);
        clone.circularReference = new ComponentWithBackReference(clone);
        return clone;
    }
}

class ComponentWithBackReference {
    public prototype;

    constructor(prototype: Prototype<any>) {
        this.prototype = prototype;
    }
}

function clientCode() {
    const p1 = new MeuPrototipo(245, new Date());
    
    const p2 = p1.clone();
    if (p1.primitive === p2.primitive) {
        console.log('Os valores primitivos foram copiados corretamente. Yay!');
    } else {
        console.log('Os valores primitivos não foram copiados. Booo!');
    }
    if (p1.component === p2.component) {
        console.log('O componente simples não foi clonado. Booo!');
    } else {
        console.log('O componente simples foi clonado. Yay!');
    }

    if (p1.circularReference === p2.circularReference) {
        console.log('O componente com referência circular não foi clonado. Booo!');
    } else {
        console.log('O componente com referência circular foi clonado. Yay!');
    }

    if (p1.circularReference.prototype === p2.circularReference.prototype) {
        console.log('O componente com referência circular está vinculado ao objeto original. Booo!');
    } else {
        console.log('O componente com referência circular está vinculado ao clone. Yay!');
    }
}

clientCode();
