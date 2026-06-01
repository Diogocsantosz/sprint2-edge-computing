# ChargeGrid Intelligence – Prova de Conceito (Sprint 2)

##  Integrantes do Grupo
RM: 561975 Rafael laprega gontijo magalhaes 
RM: 570083 Pedro Ribeiro Lopes 
RM: 572952 Gustavo Torres de Oliveira 
RM: 568690 Lucas Furquim Lima 
RM: 570246 Diogo Chiaradia Santos

## Descrição da Solução
O **ChargeGrid Intelligence** é uma solução de software desenvolvida para o **GoodWe Challenge**. O foco principal é otimizar o carregamento de veículos elétricos (EVs) em ambientes de alta demanda (como condomínios ou frotas comerciais), garantindo a estabilidade da rede elétrica e oferecendo preços inteligentes.

### Evolução em Relação à Sprint 1
Deixamos a camada puramente teórica da Sprint 1 e construímos uma **Prova de Conceito (PoC) funcional em Python**. O protótipo valida os algoritmos de distribuição de carga e precificação dinâmica em tempo real.

---

## Pilares Técnicos Demonstrados na PoC

1. **Gerenciamento Inteligente de Demanda:** O software monitora o consumo geral do prédio. A energia que sobra é dividida de forma **equitativa** entre os carros conectados. Se o consumo do prédio atingir um nível crítico, o sistema pausa as recargas automaticamente para evitar a queda do disjuntor.
2. **IA e Tarifação Dinâmica:** O algoritmo analisa o estresse da rede elétrica. Em horários de pico (uso acima de 85%), a tarifa por kWh aumenta para desencorajar o uso abusivo. Em momentos de baixo consumo, o preço cai (Tarifa Econômica), incentivando o carregamento consciente.

---