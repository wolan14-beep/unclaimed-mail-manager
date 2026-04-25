 ## Passos para enviar ao GitHub
 

Para "commitar": 
 - **`git add .`** → Seleciona os arquivos modificados
 - **`git commit -m "definição do que foi atualizado/criado"`** → Registra o estado
     - Ambiente enviado ao github pela *primeira vez*: (`git push -u origin main     
To https://github.com/wolan14-beep/unclaimed-mail-manager.git`)

 - **`git push`** → Aqui sim envia para o GitHub

Se houver divergência entre os arquivos no GitHub com os commitados no pc, vai gerar um erro ao tentar o push.

Para isso, precisa primeiro recuperar os arquivos do repositório na nuvem com:
`git pull origin main --allow-unrelated-histories`
Será aberta uma janela no vscode. Depois é só fechar e tentar novamente o push. Assim os arquivos de nuvem serão os mesmos que estão no diretório local e ao dar o push, não terá divergências.

### Parando rastreamento de itens:
Para parar o rastreamento de algum item, como no caso onde eu criei o banco de dados vazio para poder exibir no repositório mas manter para o projeto real,  se usa o comando remover:
`git rm -r --cached "diretorio/arquivo"`

---------------------------------------
## Tabelas para criar:

- Tabela `users`
  
|Campo|Tipo|Observação|
|-----|----|----------|
|`registration`|Text| Chave primária e login (matrícula)|
|`name`|Text|Nome do funcionário|
|`password`|Text|Hash do CPF ou data de nascimento|
|`profile`|Text|`admin` ou `attendant`|

<br>

- Tabela `parcels`

|Campo|Tipo|Observação|
|----|----|----|
|`order_number`|Integer|Chave primária, gerado automaticamente|
|`tracking`|Text|Número de Rastreio S10 Standard|
|`sender`|Text|Nome do Remetente|
|`entry_date`|Date|Gerado automaticamente (data atual)|
|`exit_date`|Date|Calculado (entrada + 90)|
|`status`|Text|Padrão: `waiting`|
|`changed_by`|Text|login de quem fez a última alteração|
|`change_date`|Date|Data da última alteração|

## Tuplas nas funções de manipulação do Banco de Dados

O SQL espera receber os valor de acordo com a ordem de escrita. E o elemento que garante listagem ordenada no Python são as __tuplas__

- Nas funções de cadastro foram usadas tuplas para definir a ordem dos valores que serão recebidos pelas instruções do SQLite.
  - exemplo:
    `cursor.execute('UPDATE users SET name = ?, cpf = ?, profile = ? WHERE registration = ?', (name, cpf, profile, registration))`

A tupla `(name, cpf, profile, registration)` nesse exemplo recebeu 4 valores. Todos separados por vírgula e está na ordem de acordo com a expressão SQL.

##### Tuplas de um único valor:
Quando houver apenas um valor dentro da tupla, inserir uma vírgula no final do valor declarado:
- Exemplo:
  - `(connectio,)`





