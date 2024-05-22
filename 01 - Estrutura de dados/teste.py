# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(plano_recomendado):
   
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
    
        return plano_recomendado
# TODO: Retorne o plano de internet adequado:
def main():
# Solicita ao usuário que insira o consumo médio mensal de dados:
  consumo = float(input("informe"))
  plano_recomendado=[]
  if consumo <= 10:
    plano_recomendado=("Plano Essencial Fibra - 50Mbps")
        
    
  elif consumo<=20 and consumo>10:
        plano_recomendado="Plano_Prata_Fibra_100Mbp"
       
    
  elif consumo>20:
        plano_recomendado="Plano_Premium_Fibra_300Mbps"
        
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
  recomendar_plano(plano_recomendado)
  #print(plano_recomendado)
  print(recomendar_plano(plano_recomendado))
main()