/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 3
*/

namespace Exercicio3
{
    using System;
    using System.Collections.Generic;
    using System.Threading;

    class JantarDosFilosofosComTempo
    {
        private readonly SemaphoreSlim semaforo = new SemaphoreSlim(2); // Permite dois filósofos comendo simultaneamente
        private readonly object trava = new object(); // Protege o acesso compartilhado
        private readonly int tempoMaximoParaComer = 1000; // Tempo máximo para adquirir os recursos em milissegundos

        public void Filosofo(int id)
        {
            while (true)
            {
                Pensar(id);

                if (TentarComer(id))
                {
                    Comer(id);
                    TerminarDeComer(id);
                }
                else
                {
                    Console.WriteLine($"Filósofo {id} desistiu de comer e vai pensar novamente.");
                }
            }
        }

        private bool TentarComer(int id)
        {
            Console.WriteLine($"Filósofo {id} está tentando comer.");

            // Tenta adquirir o semáforo dentro do tempo limite
            if (semaforo.Wait(tempoMaximoParaComer))
            {
                lock (trava)
                {
                    // Simula pegar os "garfos" (recursos compartilhados)
                    Console.WriteLine($"Filósofo {id} conseguiu os recursos para comer.");
                }
                return true;
            }

            return false; // Não conseguiu comer dentro do tempo
        }

        private void TerminarDeComer(int id)
        {
            lock (trava)
            {
                // Simula liberar os "garfos"
                Console.WriteLine($"Filósofo {id} terminou de comer e liberou os recursos.");
            }

            semaforo.Release(); // Libera o semáforo
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
            JantarDosFilosofosComTempo jantar = new JantarDosFilosofosComTempo();

            List<Thread> filosofos = new List<Thread>();
            for (int i = 0; i < numeroDeFilosofos; i++)
            {
                int id = i; // Captura o valor de i
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