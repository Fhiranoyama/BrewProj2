#  **BrewProj2** 



#1 Conceito do Aplicativo.
    - Esse api tem utilizaçao perfeita para viagens e podem verificar melhores e mais proximos cervejarias, podendo ter sua localizaçao em qualquer parte do mundo, caso tambem goste de alguma cervejaria nao endereçado e possivel cadastrlo e salvar seus favoritos e caso deseje ate mesmo remove-los.

#2 Setup do ambiente virtual

    - Inserindo ambiente virtual: python -m venv venv   
    - Ativando e ambiente virtual: .\venv\Scripts\activate
    - Instalando Django: pip install django
    - Instalando Django Rest: pip install djangorestframework
    - Instalando Requests: pip install requests

#2  Documentaçao Relevantes
    
    - https://stackabuse.com/creating-a-rest-api-in-python-with-django/
    - https://mazer.dev/pt-br/git/boas-praticas/commits-semanticos/

#2 Api

    - https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao=Frango

#2 Testes do Insomnia

    - Testes do Get estao funcionando conforme o esperado trazendo sempre as localizaçoes cadastradas das cervejarias por varias partes do mundo utilizando http://127.0.0.1:8000/brew e colocando nome e a cidade ele dara as informaçoes tabeladas caso nao coloque nem uma info ele buscara as mais relevantes e utilizadas.

    - Teste do post esta funcionando como esperado 

    - Testes no patch indicam que as atualizaçoes estao funcionando que funcionam atualizaçoes do sistema

    - Teste do delete permite usuarios usando comando remover os itens indesejados feitos no banco de dados armazenados.

    - Teste de Post esta salvando normalmente novos dados no banco.
    

*