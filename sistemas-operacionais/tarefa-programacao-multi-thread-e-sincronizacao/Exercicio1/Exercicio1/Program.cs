/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 1
*/

using System;
using System.Collections.Generic;
using System.Threading;

namespace Exercicio1
{
    class JantarDosFilosofos
    {
        private readonly object _trava = new object();
        private readonly Queue<int> _filaDeEspera = new Queue<int>();
        private int _comendo = 0;
        private readonly int _numeroDeFilosofos;

        public JantarDosFilosofos(int numeroDeFilosofos)
        {
            _numeroDeFilosofos = numeroDeFilosofos;
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
            lock (_trava)
            {
                _filaDeEspera.Enqueue(id);

                while (_filaDeEspera.Peek() != id || _comendo >= 2)
                {
                    Monitor.Wait(_trava);
                }

                // pode comer
                _comendo++;
                _filaDeEspera.Dequeue();
            }
        }

        private void TerminarDeComer(int id)
        {
            lock (_trava)
            {
                _comendo--;
                Monitor.PulseAll(_trava);
            }
        }

        private void Pensar(int id)
        {
            Console.WriteLine($"Filósofo {id} está pensando.");
            Thread.Sleep(new Random().Next(100, 300)); // tempo de pensar
        }

        private void Comer(int id)
        {
            Console.WriteLine($"Filósofo {id} está comendo.");
            Thread.Sleep(new Random().Next(200, 500)); // tempo de comer
        }
    }

    class Programa
    {
        static void Main()
        {
            const int numeroDeFilosofos = 5;
            JantarDosFilosofos jantar = new JantarDosFilosofos(numeroDeFilosofos);

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
