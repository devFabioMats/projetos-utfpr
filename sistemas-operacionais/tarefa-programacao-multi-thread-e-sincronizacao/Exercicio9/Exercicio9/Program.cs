/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 9
*/

namespace Exercicio9
{
    using System;
    using System.Collections.Generic;
    using System.Threading;

    class LeitoresEscritoresComPrioridade
    {
        private int leitoresAtivos = 0;
        private int escritoresEsperando = 0;
        private readonly object lockObj = new object();
        private readonly SemaphoreSlim semaforoEscritores = new SemaphoreSlim(1, 1);

        public void Ler(int id)
        {
            lock (lockObj)
            {
                while (escritoresEsperando > 0)
                {
                    Monitor.Wait(lockObj);
                }

                leitoresAtivos++;
                Console.WriteLine($"Leitor {id} iniciou a leitura.");

            }

            Thread.Sleep(1000);

            lock (lockObj)
            {
                leitoresAtivos--;
                Console.WriteLine($"Leitor {id} terminou a leitura.");

                if (leitoresAtivos == 0)
                {
                    Monitor.PulseAll(lockObj);
                }
            }
        }

        public void Escrever(int id)
        {
            lock (lockObj)
            {
                escritoresEsperando++;

                while (leitoresAtivos > 0 || escritoresEsperando > 1)
                {
                    Monitor.Wait(lockObj);
                }

                escritoresEsperando--;
                semaforoEscritores.Wait();
                Console.WriteLine($"Escritor {id} iniciou a escrita.");
            }

            Thread.Sleep(2000);

            lock (lockObj)
            {
                semaforoEscritores.Release();
                Console.WriteLine($"Escritor {id} terminou a escrita.");
                Monitor.PulseAll(lockObj);
            }
        }
    }

    class Programa
    {
        static void Main()
        {
            LeitoresEscritoresComPrioridade sistema = new LeitoresEscritoresComPrioridade();
            List<Thread> threads = new List<Thread>();

            for (int i = 1; i <= 5; i++)
            {
                int id = i;
                threads.Add(new Thread(() => sistema.Ler(id)));
            }

            for (int i = 1; i <= 3; i++)
            {
                int id = i;
                threads.Add(new Thread(() => sistema.Escrever(id)));
            }

            threads.ForEach(thread => thread.Start());

            threads.ForEach(thread => thread.Join());
        }
    }
}