# ChargeGrid Intelligence - (Sprint 2)

## Integrantes do Grupo
* RM: 561975 Rafael Laprega Gontijo Magalhaes
* RM: 570083 Pedro Ribeiro Lopes
* RM: 572952 Gustavo Torres de Oliveira
* RM: 568690 Lucas Furquim Lima
* RM: 570246 Diogo Chiaradia Santos

## Descrição da Solução
O **ChargeGrid Intelligence** é uma solução de software desenvolvida para o **GoodWe Challenge**. O foco principal é otimizar o carregamento de veículos elétricos (EV).

### Evolução em Relação à Sprint 1
Deixamos a camada puramente teórica da Sprint 1 e construímos uma **Prova de Conceito (PoC) funcional em Python**. O protótipo valida os algoritmos de distribuição de carga.

---

## Pilares Técnicos Demonstrados na PoC
1. **Gerenciamento Inteligente de Demanda:** O software monitora o consumo geral do prédio. A energia que sobra é dividida de forma **equitativa** entre os carros conectados.
2. **IA e Tarifação Dinâmica:** O algoritmo analisa o estresse da rede elétrica. Em horários de pico (uso acima de 85%), a tarifa por kWh aumenta para desencorajar o uso.

---

## Fluxo Lógico do Sistema (Arquitetura)
1. **Inicialização:** O sistema carrega os parâmetros da rede elétrica (limite de potência do edifício).
2. **Conexão de Veículos:** Os veículos elétricos (EV) entram na fila de recarga informando o nível atual da bateria.
3. **Análise de Demanda (Smart Charging):** O algoritmo calcula a soma da potência necessária. Se ultrapassar o limite predial, o sistema reduz dinamicamente a potência.
4. **Tarifação Dinâmica:** Uma simulação de IA analisa o pico de consumo do horário. Se a rede estiver sobrecarregada, o valor do kWh aumenta para desincentivar recargas.