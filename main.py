import time
import random
from datetime import datetime


class CarroEletrico:
    def __init__(self, modelo, bateria_atual, capacidade_max):
        self.modelo = modelo
        self.bateria_atual = bateria_atual
        self.capacidade_max = capacidade_max
        self.potencia_recarga_atual = 0.0

    @property
    def porcentagem_bateria(self):
        return (self.bateria_atual / self.capacidade_max) * 100


class ChargeGridIntelligence:
    def __init__(self, limite_max_rede):
        self.limite_max_rede = limite_max_rede
        self.carros_conectados = []

    def adicionar_carro(self, carro):
        self.carros_conectados = [c for c in self.carros_conectados if c.porcentagem_bateria < 100]
        self.carros_conectados.append(carro)

    def calcular_tarifa_ia(self, demanda_total_rede):
        proporcao_uso = demanda_total_rede / self.limite_max_rede
        if proporcao_uso > 0.85:
            return 2.50
        elif proporcao_uso > 0.50:
            return 1.20
        else:
            return 0.65

    def gerenciar_demanda(self):
        print("\n" + "=" * 60)
        print(f" LOGS CHARGEGRID INTELLIGENCE - {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 60)

        consumo_predio_geral = random.uniform(30.0, 65.0)
        print(f" Consumo Geral da Instalação (Sem Carros): {consumo_predio_geral:.2f} kW")

        energia_disponivel_carros = self.limite_max_rede - consumo_predio_geral
        print(
            f"Energia Restante Disponível para os Carregadores: {energia_disponivel_carros:.2f} kW / Limite: {self.limite_max_rede} kW")

        tarifa_atual = self.calcular_tarifa_ia(consumo_predio_geral)
        print(f"[IA] Tarifa Dinâmica Calculada: R$ {tarifa_atual:.2f} por kWh")

        carros_ativos = [c for c in self.carros_conectados if c.porcentagem_bateria < 100]

        if not list(carros_ativos):
            print("Todos os veículos estão 100% carregados!")
            return

        potencia_por_carro = energia_disponivel_carros / len(carros_ativos)

        if potencia_por_carro > 11.0:
            potencia_por_carro = 11.0

        if potencia_por_carro < 2.0:
            print("EMERGÊNCIA: Demanda crítica na rede! Carregamento suspenso temporariamente.")
            potencia_por_carro = 0.0

        print(f"Potência Balanceada Alocada por Veículo: {potencia_por_carro:.2f} kW\n")

        print(" STATUS DOS VEÍCULOS ")
        for carro in carros_ativos:
            carro.potencia_recarga_atual = potencia_por_carro

            if potencia_por_carro > 0:
                carro.bateria_atual += (potencia_por_carro * 0.1)
                if carro.bateria_atual > carro.capacidade_max:
                    carro.bateria_atual = carro.capacidade_max

            print(f" {carro.modelo}: [{carro.porcentagem_bateria:.1f}%] - "
                  f"Recebendo {carro.potencia_recarga_atual:.2f} kW "
                  f"({'CARREGANDO' if potencia_por_carro > 0 else 'AGUARDANDO LIBERAÇÃO DE FLUXO'})")



if __name__ == "__main__":
    central_chargegrid = ChargeGridIntelligence(limite_max_rede=80.0)

    carro1 = CarroEletrico("BYD Dolphin", bateria_atual=15.0, capacidade_max=45.0)
    carro2 = CarroEletrico("GWM Ora 03", bateria_atual=38.0, capacidade_max=48.0)
    carro3 = CarroEletrico("Volvo EX30", bateria_atual=42.0, capacidade_max=51.0)

    # Note que o nome do método corrigido agora casa com a chamada aqui embaixo
    central_chargegrid.adicionar_carro(carro1)
    central_chargegrid.adicionar_carro(carro2)
    central_chargegrid.adicionar_carro(carro3)

    print("Iniciando Prova de Conceito do ChargeGrid Intelligence (GoodWe Challenge)...")
    for i in range(5):
        central_chargegrid.gerenciar_demanda()
        time.sleep(3)