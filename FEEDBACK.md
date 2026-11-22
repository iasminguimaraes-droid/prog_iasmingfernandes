# Feedback do 3º trimestre

Fala, Iasmin.

Suas notas do trimestre ficaram assim: aulas parte 1 0,5 de 0,5, Lista A 1,1 de 1,5 e aulas parte 2 0,4 de 0,5. A Lista B você tem até 04 de dezembro, então ela ainda não entrou.

A Lista A chegou depois do prazo (18/10 ao meio-dia), então a nota teve desconto por atraso. Na aula 03 passaram 3 de 19 testes (erradas: `busca_linear_contando`, `mais_frequente_contando`; sem fazer: `busca_binaria_contando`, `tem_repetido_contando`, `quantas_divisoes`). Na aula 04, `buscas_para_compensar` tem erro de recuo e usa `custo_binaria = custo_binaria(n)`, que dá `UnboundLocalError` porque a variável tem o mesmo nome da função. As outras quatro funções estão certas. Na aula 05, o código foi colado sem nenhum recuo, então o Python não entende os blocos. `bubble_sort` não devolve a lista, e `selection_sort`, `insertion_sort` e `quicksort` usam `copiar` sem definir. A lógica está certa. Na aula 06, o código foi colado sem recuo nenhum. As quatro funções estão com a lógica correta, mas o arquivo não roda. Tem também código solto (`print`) no meio do arquivo. Onde o arquivo não rodava (erro de sintaxe ou recuo), eu testei numa cópia com o problema contornado e descontei 10%. Seu código original ficou como estava.

Parabéns pelas aulas 01 e 02 e pela Lista A, passou tudo.

Uma coisa que reparei, e fica só como dica: apareceu compreensão de lista (aula 02), `sum()` (aula 06 e Lista A) e `max()` (aula 06 e Lista A) no seu código, e a gente ainda não viu isso em aula. Se você pesquisou ou usou uma IA como apoio, tudo bem, mas vale tomar cuidado para entender cada linha e conseguir explicar sozinho, porque no mini-hackathon da prova você vai estar sem ela. Se tiver dúvida, me chama que a gente resolve com o que já foi visto.
