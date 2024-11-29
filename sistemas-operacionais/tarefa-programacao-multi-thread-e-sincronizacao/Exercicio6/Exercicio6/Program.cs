/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 6
*/

namespace Exercicio6
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;

    class Buffer
    {
        private Queue<int> itens = new Queue<int>();
        private readonly int capacidadeMaxima;

        public Buffer(int capacidade)
        {
            capacidadeMaxima = capacidade;
        }

        public bool EstaCheio => itens.Count >= capacidadeMaxima;
        public bool EstaVazio => itens.Count == 0;
        public int TamanhoAtual => itens.Count;

        public void AdicionarItem(int item)
        {
            lock (itens)
            {
                while (EstaCheio)
                {
                    Monitor.Wait(itens);
                }
                itens.Enqueue(item);
                Console.WriteLine($"[Buffer {capacidadeMaxima}] Item {item} adicionado. (Tamanho Atual: {itens.Count}/{capacidadeMaxima})");
                Monitor.PulseAll(itens);
            }
        }

        public int ConsumirItem()
        {
            lock (itens)
            {
                while (EstaVazio)
                {
                    Monitor.Wait(itens);
                }
                int item = itens.Dequeue();
                Console.WriteLine($"[Buffer {capacidadeMaxima}] Item {item} consumido. (Tamanho Atual: {itens.Count}/{capacidadeMaxima})");
                Monitor.PulseAll(itens);
                return item;
            }
        }
    }

    class SistemaProdutorConsumidor
    {
        private List<Buffer> buffers;

        public SistemaProdutorConsumidor(List<int> tamanhosDosBuffers)
        {
            buffers = tamanhosDosBuffers.Select(tamanho => new Buffer(tamanho)).ToList();
        }

        public void Produtor(int id)
        {
            Random random = new Random();
            while (true)
            {
                int item = random.Next(100);
                Buffer bufferEscolhido = EscolherBufferParaProduzir();
                bufferEscolhido.AdicionarItem(item);
                Console.WriteLine($"Produtor {id} produziu item {item}.");
                Thread.Sleep(random.Next(500, 1000));
            }
        }

        public void Consumidor(int id)
        {
            Random random = new Random();
            while (true)
            {
                Buffer bufferEscolhido = EscolherBufferParaConsumir();
                if (bufferEscolhido != null)
                {
                    int item = bufferEscolhido.ConsumirItem();
                    Console.WriteLine($"Consumidor {id} consumiu item {item}.");
                }
                Thread.Sleep(random.Next(500, 1000));
            }
        }

        private Buffer EscolherBufferParaProduzir()
        {
            lock (buffers)
            {
                Random random = new Random();
                return buffers.FirstOrDefault(buffer => !buffer.EstaCheio) ?? buffers[random.Next(buffers.Count)];
            }
        }


        private Buffer EscolherBufferParaConsumir()
        {
            lock (buffers)
            {
                return buffers.OrderByDescending(buffer => buffer.TamanhoAtual).FirstOrDefault(buffer => !buffer.EstaVazio);
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

            threads.ForEach(thread => thread.Join());
        }
    }
}