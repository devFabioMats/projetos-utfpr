/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 5
*/

namespace Exercicio5
{
    using System;
    using System.Collections.Generic;
    using System.Threading;

    class TrabalhadorESupervisor
    {
        private readonly object trava = new object();
        private bool turnoLiberado = false;

        public void Supervisor(int rodadas)
        {
            for (int i = 1; i <= rodadas; i++)
            {
                Console.WriteLine($"Supervisor: Sinalizando início da rodada {i}.");
                LiberarTurno();

                Thread.Sleep(1000);

                Console.WriteLine($"Supervisor: Finalizando rodada {i}.");
            }

            Console.WriteLine("Supervisor: Trabalho concluído. Encerrando.");
        }

        public void Trabalhador(int id)
        {
            while (true)
            {
                AguardarTurno(id);
                RealizarTrabalho(id);
            }
        }

        private void LiberarTurno()
        {
            lock (trava)
            {
                turnoLiberado = true;
                Monitor.PulseAll(trava);
            }
        }

        private void AguardarTurno(int id)
        {
            lock (trava)
            {
                while (!turnoLiberado)
                {
                    Monitor.Wait(trava);
                }
            }
        }

        private void RealizarTrabalho(int id)
        {
            lock (trava)
            {
                Console.WriteLine($"Trabalhador {id}: Começando o trabalho.");
                Thread.Sleep(new Random().Next(500, 1000));
                Console.WriteLine($"Trabalhador {id}: Finalizou o trabalho.");
                turnoLiberado = false;
            }
        }
    }

    class Programa
    {
        static void Main()
        {
            const int numeroDeTrabalhadores = 5;
            const int rodadas = 3;

            TrabalhadorESupervisor sistema = new TrabalhadorESupervisor();

            List<Thread> trabalhadores = new List<Thread>();
            for (int i = 0; i < numeroDeTrabalhadores; i++)
            {
                int id = i + 1;
                trabalhadores.Add(new Thread(() => sistema.Trabalhador(id)));
            }

            foreach (var trabalhador in trabalhadores)
            {
                trabalhador.Start();
            }

            sistema.Supervisor(rodadas);

            foreach (var trabalhador in trabalhadores)
            {
                trabalhador.Abort();
            }
        }
    }
}