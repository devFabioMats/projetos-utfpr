/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 2
*/

using System;
using System.Collections.Generic;
using System.Threading;

namespace Exercicio2
{
    class JantarDosFilosofosComSemaforo
    {
        private readonly SemaphoreSlim semaforo = new SemaphoreSlim(2);
        private readonly object trava = new object();
        private readonly HashSet<int> filaDeEspera = new HashSet<int>();
        private int ultimoQueComeu = -1;

        private readonly int numeroDeFilosofos;

        public JantarDosFilosofosComSemaforo(int numeroDeFilosofos)
        {
            this.numeroDeFilosofos = numeroDeFilosofos;
        }

        public void Filosofo(int id)
        {
            while (true)
            {
                Pensar(id);
                SolicitarParaComer(id);
                Comer(id);
                TerminarDeComer(id);
            }
        }

        private void SolicitarParaComer(int id)
        {
            lock (trava)
            {
                filaDeEspera.Add(id);

                while (id == ultimoQueComeu || !PodeComer(id))
                {
                    Monitor.Wait(trava);
                }

                filaDeEspera.Remove(id);
                ultimoQueComeu = id;
            }

            semaforo.Wait();
        }

        private void TerminarDeComer(int id)
        {
            semaforo.Release();
            lock (trava)
            {
                Monitor.PulseAll(trava);
            }
        }

        private bool PodeComer(int id)
        {
            return filaDeEspera.Contains(id) && semaforo.CurrentCount > 0;
        }

        private void Pensar(int id)
        {
            Console.WriteLine($"Filósofo {id} está pensando.");
            Thread.Sleep(new Random().Next(100, 300)); // Simula pensar
        }

        private void Comer(int id)
        {
            Console.WriteLine($"Filósofo {id} está comendo.");
            Thread.Sleep(new Random().Next(200, 500)); // Simula comer
        }
    }

    class Programa
    {
        static void Main()
        {
            const int numeroDeFilosofos = 5;
            JantarDosFilosofosComSemaforo jantar = new JantarDosFilosofosComSemaforo(numeroDeFilosofos);

            List<Thread> filosofos = new List<Thread>();
            for (int i = 0; i < numeroDeFilosofos; i++)
            {
                int id = i;
                filosofos.Add(new Thread(() => jantar.Filosofo(id)));
            }

            foreach (var filosofo in filosofos)
            {
                filosofo.Start();
            }

            foreach (var filosofo in filosofos)
            {
                filosofo.Join();
            }
        }
    }
}