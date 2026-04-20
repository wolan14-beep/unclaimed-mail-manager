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


