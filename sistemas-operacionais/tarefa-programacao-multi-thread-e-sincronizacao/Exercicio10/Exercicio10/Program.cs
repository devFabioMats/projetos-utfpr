/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 10
*/

namespace Exercicio10
{
    using System;
    using System.Collections.Generic;
    using System.Threading;

    class LeitoresEscritoresComContagem
    {
        private int leitoresAtivos = 0;
        private int escritoresEsperando = 0;
        private int escritorAtivo = 0;
        private readonly object lockObj = new object();

        private int maxLeiturasConsecutivas = 3;
        private Dictionary<int, int> leiturasPorLeitor = new Dictionary<int, int>();

        public void Ler(int id)
        {
            lock (lockObj)
            {
                if (!leiturasPorLeitor.ContainsKey(id))
                {
                    leiturasPorLeitor[id] = 0;
                }

                while (leiturasPorLeitor[id] >= maxLeiturasConsecutivas || escritorAtivo > 0 || escritoresEsperando > 0)
                {
                    Monitor.Wait(lockObj);
                }

                leitoresAtivos++;
                leiturasPorLeitor[id]++;
                Console.WriteLine($"Leitor {id} iniciou a leitura (Leituras consecutivas: {leiturasPorLeitor[id]}).");
            }

            Thread.Sleep(1000);

            lock (lockObj)
            {
                leitoresAtivos--;
                Console.WriteLine($"Leitor {id} terminou a leitura.");

                if (leitoresAtivos == 0 && leiturasPorLeitor[id] >= maxLeiturasConsecutivas)
                {
                    leiturasPorLeitor[id] = 0;
                }

                Monitor.PulseAll(lockObj);
            }
        }

        public void Escrever(int id)
        {
            lock (lockObj)
            {
                escritoresEsperando++;

                while (leitoresAtivos > 0 || escritorAtivo > 0)
                {
                    Monitor.Wait(lockObj);
                }

                escritoresEsperando--;
                escritorAtivo++;
                Console.WriteLine($"Escritor {id} iniciou a escrita.");
            }

            Thread.Sleep(2000);

            lock (lockObj)
            {
                escritorAtivo--;
                Console.WriteLine($"Escritor {id} terminou a escrita.");
                Monitor.PulseAll(lockObj);
            }
        }
    }

    class Programa
    {
        static void Main()
        {
            LeitoresEscritoresComContagem sistema = new LeitoresEscritoresComContagem();
            List<Thread> threads = new List<Thread>();

            for (int i = 1; i <= 5; i++)
            {
                int id = i;
                threads.Add(new Thread(() => sistema.Ler(id)));
            }

            for (int i = 1; i <= 2; i++)
            {
                int id = i;
                threads.Add(new Thread(() => sistema.Escrever(id)));
            }

            threads.ForEach(thread => thread.Start());

            threads.ForEach(thread => thread.Join());
        }
    }
}