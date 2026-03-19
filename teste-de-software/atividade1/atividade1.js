// Função para encontrar o índice do último zero em um vetor

function lastZeroIndex(vetor) {
	for (let i = vetor.length - 1; i >= 0; i--) {
		if (vetor[i] === 0) return i;
	}

	return -1;
}

const testVectors = [
	[4, 2, 0, 7, 0, 9],
	[1, 2, 3, 4],
	[0, 5, 8],
	[0, 0, 0, 0],
	[],
];

for (const vetor of testVectors) {
	console.log("vetor:", vetor, "-> ultimo indice de zero:", lastZeroIndex(vetor));
}