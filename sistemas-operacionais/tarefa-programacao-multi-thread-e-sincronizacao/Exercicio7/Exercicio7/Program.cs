/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 7
*/

namespace Exercicio7
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;

    class Item
    {
        public int Prioridade { get; set; }
        public int Valor { get; set; }

        public Item(int prioridade, int valor)
        {
            Prioridade = prioridade;
            Valor = valor;
        }
    }

    class Buffer
    {
        private SortedList<int, Queue<Item>> itens = new SortedList<int, Queue<Item>>();
        private readonly int capacidadeMaxima;
        private readonly object lockObj = new object();

        public Buffer(int capacidade)
        {
            capacidadeMaxima = capacidade;
        }

        public bool EstaCheio => itens.Values.Sum(q => q.Count) >= capacidadeMaxima;
        public bool EstaVazio => itens.Count == 0 || itens.Values.Sum(q => q.Count) == 0;

        public void AdicionarItem(Item item)
        {
            lock (lockObj)
            {
                while (EstaCheio)
                {
                    Monitor.Wait(lockObj);
                }

                if (!itens.ContainsKey(item.Prioridade))
                {
                    itens[item.Prioridade] = new Queue<Item>();
                }

                itens[item.Prioridade].Enqueue(item);
                Console.WriteLine($"Item {item.Valor} (Prioridade: {item.Prioridade}) adicionado.");
                Monitor.PulseAll(lockObj);
            }
        }

        public Item ConsumirItem()
        {
            lock (lockObj)
            {
                while (EstaVazio)
                {
                    Monitor.Wait(lockObj);
                }

                int prioridadeMaisAlta = itens.Keys[itens.Keys.Count - 1];
                Queue<Item> itensComMaiorPrioridade = itens[prioridadeMaisAlta];
                Item item = itensComMaiorPrioridade.Dequeue();
                if (itensComMaiorPrioridade.Count == 0)
                {
                    itens.Remove(prioridadeMaisAlta);
                }

                Console.WriteLine($"Item {item.Valor} (Prioridade: {item.Prioridade}) consumido.");
                Monitor.PulseAll(lockObj);
                return item;
            }
        }
    }

    class SistemaProdutorConsumidor
    {
        private List<Buffer> buffers;
        private Random random = new Random();

        public SistemaProdutorConsumidor(List<int> tamanhosDosBuffers)
        {
            buffers = tamanhosDosBuffers.ConvertAll(tamanho => new Buffer(tamanho));
        }

        public void Produtor(int id)
        {
            while (true)
            {
                int valor = random.Next(100);
                int prioridade = random.Next(1, 11);
                Item item = new Item(prioridade, valor);
                Buffer bufferEscolhido = EscolherBufferParaProduzir();
                bufferEscolhido.AdicionarItem(item);
                Console.WriteLine($"Produtor {id} produziu item {item.Valor} (Prioridade: {item.Prioridade}).");
                Thread.Sleep(random.Next(500, 1000));
            }
        }

        public void Consumidor(int id)
        {
            while (true)
            {
                Buffer bufferEscolhido = EscolherBufferParaConsumir();
                if (bufferEscolhido != null)
                {
                    Item item = bufferEscolhido.ConsumirItem();
                    Console.WriteLine($"Consumidor {id} consumiu item {item.Valor} (Prioridade: {item.Prioridade}).");
                }
                Thread.Sleep(random.Next(500, 1000));
            }
        }

        private Buffer EscolherBufferParaProduzir()
        {
            lock (buffers)
            {
                return buffers.Find(buffer => !buffer.EstaCheio);
            }
        }

        private Buffer EscolherBufferParaConsumir()
        {
            lock (buffers)
            {
                return buffers.Find(buffer => !buffer.EstaVazio);
            }
        }
    }

    class Programa
    {
        static void Main()
        {
            List<int> tamanhosDosBuffers = new List<int> { 5, 10, 15 };
            SistemaProdutorConsumidor sistema = new SistemaProdutorConsumidor(tamanhosDosBuffers);

            List<Thread> threads = new List<Thread>();
            for (int i = 0; i < 3; i++)
            {
                int id = i + 1;
                threads.Add(new Thread(() => sistema.Produtor(id)));
            }
            for (int i = 0; i < 2; i++)
            {
                int id = i + 1;
                threads.Add(new Thread(() => sistema.Consumidor(id)));
            }

            threads.ForEach(thread => thread.Start());
        }
    }
}