#include <stdio.h>
#include <stdlib.h>

// Estrutura do nodo da árvore AVL
typedef struct Nodo {
  int chave;              // Valor armazenado no nodo
  int bal;                // Fator de balanceamento do nodo
  struct Nodo *esq, *dir; // Ponteiros para os filhos esquerdo e direito
} Nodo;

// Função para criar um novo nodo
Nodo *criaNodo(int x) {
  Nodo *novo = (Nodo *)malloc(sizeof(Nodo)); // Aloca memória para um novo nodo
  if (!novo) { // Verifica se a alocação foi bem-sucedida
    printf("Erro de alocação de memória!\n");
    exit(1); // Sai do programa em caso de erro
  }
  novo->chave = x;              // Define o valor do nodo
  novo->bal = 0;                // Inicializa o fator de balanceamento como 0
  novo->esq = novo->dir = NULL; // Inicializa os filhos como NULL
  return novo;                  // Retorna o nodo criado
}

// Caso 1: Rotação para balancear o lado esquerdo
void caso1(Nodo **pt, int *h) {
  Nodo *ptu = (*pt)->esq; // Ponteiro para o filho esquerdo do nodo
  if (ptu->bal ==
      -1) { // Verifica se é necessário uma rotação simples à direita
    printf("RSD %d\n", (*pt)->chave); // Indica a rotação
    (*pt)->esq = ptu->dir;            // Ajusta o filho direito do nodo esquerdo
    ptu->dir = *pt; // Move o nodo atual para a direita do nodo esquerdo
    (*pt)->bal = 0; // Atualiza o fator de balanceamento
    *pt = ptu;      // Atualiza o ponteiro raiz
  } else {          // Caso contrário, faz uma rotação dupla à direita
    printf("RDD %d\n", (*pt)->chave);
    Nodo *ptv = ptu->dir;  // Ponteiro para o filho direito do nodo esquerdo
    ptu->dir = ptv->esq;   // Ajusta o filho esquerdo do nodo do meio
    ptv->esq = ptu;        // Ajusta o nodo esquerdo para baixo
    (*pt)->esq = ptv->dir; // Ajusta o filho direito do nodo do meio
    ptv->dir = *pt;        // Ajusta o nodo atual para baixo
    (*pt)->bal =
        (ptv->bal == -1) ? 1 : 0; // Atualiza os fatores de balanceamento
    ptu->bal = (ptv->bal == 1) ? -1 : 0;
    *pt = ptv; // Atualiza o ponteiro raiz
  }
  (*pt)->bal = 0; // Após a rotação, o nodo raiz fica balanceado
  *h = 0;         // Ajusta a altura da árvore
}

// Caso 2: Rotação para balancear o lado direito
void caso2(Nodo **pt, int *h) {
  Nodo *ptu = (*pt)->dir; // Ponteiro para o filho direito do nodo
  if (ptu->bal ==
      1) { // Verifica se é necessário uma rotação simples à esquerda
    printf("RSE %d\n", (*pt)->chave);
    (*pt)->dir = ptu->esq; // Ajusta o filho esquerdo do nodo direito
    ptu->esq = *pt;        // Move o nodo atual para a esquerda do nodo direito
    (*pt)->bal = 0;        // Atualiza o fator de balanceamento
    *pt = ptu;             // Atualiza o ponteiro raiz
  } else { // Caso contrário, faz uma rotação dupla à esquerda
    printf("RDE %d\n", (*pt)->chave);
    Nodo *ptv = ptu->esq;  // Ponteiro para o filho esquerdo do nodo direito
    ptu->esq = ptv->dir;   // Ajusta o filho direito do nodo do meio
    ptv->dir = ptu;        // Ajusta o nodo direito para baixo
    (*pt)->dir = ptv->esq; // Ajusta o filho esquerdo do nodo do meio
    ptv->esq = *pt;        // Ajusta o nodo atual para baixo
    (*pt)->bal =
        (ptv->bal == 1) ? -1 : 0; // Atualiza os fatores de balanceamento
    ptu->bal = (ptv->bal == -1) ? 1 : 0;
    *pt = ptv; // Atualiza o ponteiro raiz
  }
  (*pt)->bal = 0; // Após a rotação, o nodo raiz fica balanceado
  *h = 0;         // Ajusta a altura da árvore
}

// Inserção em uma árvore AVL
void insereAVL(int x, Nodo **pt, int *h) {
  if (*pt == NULL) { // Se o nodo atual for NULL, insere um novo nodo
    *pt = criaNodo(x);
    *h = 1;                       // A altura da árvore aumenta
  } else if (x == (*pt)->chave) { // Se o valor já existe, não faz nada
    return;
  } else if (x < (*pt)->chave) { // Insere no lado esquerdo se o valor for menor
    insereAVL(x, &(*pt)->esq, h);
    if (*h) {               // Verifica se houve alteração na altura
      switch ((*pt)->bal) { // Ajusta o fator de balanceamento
      case 1:
        (*pt)->bal = 0;
        *h = 0;
        break;
      case 0:
        (*pt)->bal = -1;
        break;
      case -1:
        caso1(pt, h); // Faz uma rotação se necessário
        break;
      }
    }
  } else { // Insere no lado direito se o valor for maior
    insereAVL(x, &(*pt)->dir, h);
    if (*h) {               // Verifica se houve alteração na altura
      switch ((*pt)->bal) { // Ajusta o fator de balanceamento
      case -1:
        (*pt)->bal = 0;
        *h = 0;
        break;
      case 0:
        (*pt)->bal = 1;
        break;
      case 1:
        caso2(pt, h); // Faz uma rotação se necessário
        break;
      }
    }
  }
}

// Função para liberar a árvore
void liberaArvore(Nodo *pt) {
  if (pt != NULL) { // Percorre todos os nodos e libera memória
    liberaArvore(pt->esq);
    liberaArvore(pt->dir);
    free(pt);
  }
}

int main() {
  Nodo *raiz = NULL; // Ponteiro inicial para a raiz da árvore
  int h = 0, entrada;

  while (1) {              // Loop para receber entradas do usuário
    scanf("%d", &entrada); // Lê o valor inserido
    if (entrada == -1) {   // -1 encerra o programa
      printf("fim\n");
      break;
    } else if (entrada == 0) { // 0 reinicia a árvore
      if (raiz != NULL) {
        printf("Bal= %d\n",
               raiz->bal);  // Mostra o fator de balanceamento da raiz
        liberaArvore(raiz); // Libera memória da árvore
        raiz = NULL;        // Reinicia a raiz
      }
    } else if (entrada > 0) { // Valores positivos são inseridos na árvore
      insereAVL(entrada, &raiz, &h);
    }
  }

  return 0; // Fim do programa
}
