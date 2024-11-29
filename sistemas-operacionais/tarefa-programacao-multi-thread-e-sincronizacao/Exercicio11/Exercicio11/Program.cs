/*
 * Aluno: FABIO EIZO RODRIGUEZ MATSUMOTO
 * RA: 2475413
 * Disciplina: ES42D - ES21
 * Enunciado: Exercício 11
*/

namespace Exercicio11
{
    using System;
    using System.Collections.Generic;
    using System.Threading;

    class DadosCompartilhados
    {
        private readonly ReaderWriterLockSlim rwLock = new ReaderWriterLockSlim();
        private string dado = "Valor inicial";

        public void Ler(int idLeitor)
        {
            rwLock.EnterReadLock();
            try
            {
                Console.WriteLine($"Leitor {idLeitor} leu: {dado}");
            }
            finally
            {
                rwLock.ExitReadLock();
            }

            Thread.Sleep(500);
        }

        public void Escrever(int idEscritor, string novoDado)
        {
            rwLock.EnterWriteLock();
            try
            {
                Console.WriteLine($"Escritor {idEscritor} está atualizando o dado...");
                dado = novoDado;
                Console.WriteLine($"Escritor {idEscritor} atualizou o dado para: {dado}");
            }
            finally
            {
                rwLock.ExitWriteLock();
            }

            Thread.Sleep(1000);
        }
    }

    class Programa
    {
        static void Main()
        {
            DadosCompartilhados dados = new DadosCompartilhados();
            List<Thread> threads = new List<Thread>();

            for (int i = 1; i <= 5; i++)
            {
                int idLeitor = i;
                threads.Add(new Thread(() =>
                {
                    while (true)
                    {
                        dados.Ler(idLeitor);
                        Thread.Sleep(200);
                    }
                }));
            }


            for (int i = 1; i <= 3; i++)
            {
                int idEscritor = i;
                threads.Add(new Thread(() =>
                {
                    while (true)
                    {
                        dados.Escrever(idEscritor, $"Atualizado pelo escritor {idEscritor} em {DateTime.Now:HH:mm:ss}");
                        Thread.Sleep(2000);
                    }
                }));
            }

            threads.ForEach(thread => thread.Start());

            threads.ForEach(thread => thread.Join());
        }
    }
}