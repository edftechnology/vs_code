#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `VS Code` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/usae the `VS Code` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `VS Code (VS Code)`
# 
# O `VS Code`, comumente conhecido como `VS Code`, é um editor de código-fonte altamente popular e amplamente utilizado por desenvolvedores de software em todo o mundo. Desenvolvido pela Microsoft, o `VS Code` é uma ferramenta altamente personalizável e extensível, que oferece suporte a uma ampla variedade de linguagens de programação e _frameworks_. Sua interface simples e intuitiva, juntamente com recursos poderosos, como realce de sintaxe, depuração integrada, controle de versão e uma vasta coleção de extensões disponíveis na sua loja, tornam-no uma escolha preferida para muitos programadores que buscam eficiência e produtividade em seus projetos de desenvolvimento de _software_.
# 
# ### `Linting`
# 
# O `Linting` é o processo de análise estática de código-fonte para identificar problemas, erros de sintaxe, e más práticas de programação antes da execução do programa. Ferramentas de linting, conhecidas como _linters_, verificam o código em busca de inconsistências, padrões de estilo e potenciais _bugs_, ajudando os desenvolvedores a manterem a qualidade e legibilidade do código. Esse recurso é especialmente valioso em equipes de desenvolvimento, pois promove a conformidade com diretrizes de codificação e reduz a probabilidade de erros em produção, resultando em um código mais robusto e fácil de manter.
# 
# ### `PyLance`
# 
# O `PyLance` é uma extensão para o `VS Code` que oferece suporte avançado ao `Python`, proporcionando uma experiência de codificação mais eficiente. Baseado no `Pyright`, um servidor de linguagem desenvolvido pela `Microsoft`, o `PyLance` fornece recursos como autocompletar (_IntelliSense_), verificação de tipos estática, navegação de código e documentação _inline_, ajudando os desenvolvedores a escrever código mais preciso e sem erros. Ele é amplamente utilizado para melhorar a produtividade ao trabalhar com projetos `Python`, oferecendo ferramentas poderosas de análise e sugestões em tempo real.
# 

# ## 1. Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que **NÃO** podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que **NÃO** são mais necessários. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
#     
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
#     
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     
#     ```bash
#     sudo apt full-upgrade -y
#     ```

# 3. **Navegue até o diretório onde o arquivo `.deb` está localizado:** Use o comando cd para navegar até o diretório onde o arquivo `.deb` está localizado. Por exemplo, se o arquivo `.deb` estiver na sua pasta `Downloads`, você pode usar o seguinte comando:
# 
#     ```bash
#     cd ~/Downloads
#     ```
# 
# 4. Instale o arquivo `.deb`: Use o comando `dpkg` para instalar o arquivo `.deb`. Substitua "`<nome_do_arquivo>.deb`" pelo nome real do arquivo `.deb` que você deseja instalar:
#     
#     ```bash
#     sudo dpkg -i code_1.82.2-1694671812_amd64.deb
#     ```
# 
#     Você precisará fornecer sua senha de administrador (`sudo`) para continuar.
# 
# 5. Resolva as dependências (se necessário): Às vezes, a instalação do arquivo `.deb` pode gerar erros devido a dependências ausentes. Se isso acontecer, você pode usar o seguinte comando para tentar resolver as dependências:
# 
#     ```bash
#     sudo apt install -f
#     ```
# 
# O comando acima tentará instalar automaticamente as dependências necessárias para o pacote `.deb` que você está instalando.
# 
# 6. **Verifique a instalação:** Após a conclusão do processo, verifique se o programa ou pacote foi instalado corretamente. Você pode fazer isso procurando o aplicativo no menu de aplicativos ou executando-o a partir do terminal com o comando:
# 
#     ```bash
#     code
#     ```
# 
# Isso deve permitir que você instale um arquivo `.deb` no seu sistema `Linux Ubuntu`. Lembre-se de que os arquivos .deb são pacotes de software específicos para distribuições baseadas no Debian, como o `Linux Ubuntu`, e geralmente são seguros de usar, especialmente se você os obtiver de fontes confiáveis. No entanto, sempre esteja ciente da origem dos arquivos .deb que você baixa e evite fontes **NÃO** confiáveis para garantir a segurança do seu sistema.
# 

# ### 1.1 Código completo para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` 
# 
# Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```bash
#     NÂO há.
#     ```

# ### 1.2 Sincronizar suas configurações do `VS Code`
# 
# #### 1.2.1 **Opção recomendada: conta `Microsoft`**
# 
# 1. Abra o `VS Code`
# 
# 2. Clique no ícone de `perfil` no canto inferior esquerdo
# (normalmente aparece sua inicial ou um ícone de usuário).
# 
# 3. No menu que abrir, clique em:
# 
# ```bash
# Sign in to Sync Settings…
# ```
# 
# 4. Escolha Sign `in with Microsoft`
# 
# 5. Uma janela do navegador vai abrir, faça _login_ com sua conta `Microsoft`.
# 
# 6. Após autenticar, o `VS Code` perguntará o que você deseja sincronizar. Geralmente é seguro deixar tudo marcado:
# 
# - Settings (configurações)
# 
# - Keybindings (atalhos)
# 
# - Extensions (extensões)
# 
# - Snippets
# 
# - UI State
# 
# 6.1 Clique em `OK` para confirmar.
# 
# 

# #### 1.2.2 Como confirmar que a sincronização está ativa
# 
# No canto inferior esquerdo, você deve ver algo como:
# 
# ```bash
# Settings Sync: On
# ```
# 
# Se quiser verificar manualmente:
# 
# 1. Clique novamente no ícone do perfil
# 
# 2. Se aparecer `Turn off Settings Sync`, significa que já está funcionando.

# ## 2. Configurar a variável de ambiente no `VS Code`
# 
# Para configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável de ambiente `DEBUG_MODE`, você pode seguir os seguintes passos:
# 
# ### 2.1 Configurar a variável de ambiente no `VS Code`
# 
# 1. **Abra seu projeto no `VS Code`**: Certifique-se de que seu projeto esteja aberto no `VS Code`.
# 
# 2. **Crie ou edite o arquivo `launch.json`**:
# 
#     2.1 O arquivo `launch.json` é usado para configurar o comportamento da depuração no `VS Code`. Se você **NÃO** tiver um arquivo `launch.json`, você pode criar um.
# 
#     2.2 Para criar ou abrir o `launch.json`, vá para a aba `Run and Debug` (`Ctrl+Shift+D`) e clique no _link_ `create a launch.json file` ou `add configuration`.
# 
# 3. **Adicione a configuração da variável de ambiente**: No arquivo `launch.json`, adicione uma configuração para a variável de ambiente `DEBUG_MODE`. Aqui está um exemplo de configuração que define a variável de ambiente `DEBUG_MODE` para `True` durante a depuração:
# 
#     ```json
#     {
#         "version": "0.2.0",
#         "configurations": [
#             {
#                 "name": "Python: Current File",
#                 "type": "debugpy",
#                 "request": "launch",
#                 "program": "${file}",
#                 "console": "integratedTerminal",
#                 "env": {
#                     "DEBUG_MODE": "True"
#                 }
#             }
#         ]
#     }
#     ```
# 
# 4. **Salvar e iniciar a depuração**: Salve as alterações no arquivo `launch.json`. Inicie a depuração clicando no botão de execução de depuração (ícone de triângulo verde) na aba `Run and Debug` ou pressionando `F5`.
# 

# ### 2.2 Localização do arquivo `launch.json`
# 
# o arquivo `launch.json` é armazenado em uma pasta específica dentro do seu projeto no `VS Code`. Ele faz parte da configuração do seu ambiente de depuração. Aqui estão detalhes sobre onde você pode encontrar e como ele é organizado:
# 
# 1. **Localização**:
# 
#     1.1 O arquivo `launch.json` é armazenado na pasta `.vscode` no diretório raiz do seu projeto. Esta pasta é criada automaticamente pelo `VS Code` quando você adiciona configurações de depuração pela primeira vez.
# 
#     1.2 O caminho completo seria algo como: `/caminho/para/seu/projeto/.vscode/launch.json`
# 
#     1.2 Você pode copiar o arquivo para a pasta do seu projeto, execute o comando:
#     
#     ```bash
#     sudo cp /home/edenedfsls/Documents/Downloads/unix/ubuntu/ide/vs_code/vs_code/docs/.vscode/launch.json /caminho/para/seu/projeto/.vscode/
#     ``` 

# ### 2.3 Código `Python` para verificar a variável de ambiente
# 
# Dentro do seu código `Python`, você pode verificar se a variável `DEBUG_MODE` está definida corretamente assim:
# 
# ```python
# import os
# 
# # Verificar a variável de ambiente DEBUG_MODE
# debug_mode = os.getenv("DEBUG_MODE") == "True"
# 
# if debug_mode:
#     print("Modo de depuração ativado.")
# else:
#     print("Modo de depuração **NÃO** ativado.")
# ```
# 
# **Dicas adicionais**
# 
# - **Ambientes de desenvolvimento e testes**: Certifique-se de que o `VS Code` e o seu ambiente `Python` estejam configurados corretamente para usar o ambiente virtual ou a configuração desejada.
# 
# - **Recarregar o `VS Code`**: Às vezes, é útil reiniciar o `VS Code` para garantir que todas as configurações e variáveis de ambiente sejam aplicadas corretamente.
# 
# Seguindo esses passos, você deverá ser capaz de configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável `DEBUG_MODE` conforme necessário.

# ## 3. Configurar o `PEP 8` no `VS Code`
# 
# Antes de configurar o `PEP 8` no `VS Code` é recomendável conhecer as opções de arquivo `settings.json`, como segue:
# 

# ### 3.1 Opções de arquivo `settings.json`
# 
# Há três opções para editar o `settings.json`. Vou explicar quando usar cada uma delas:
# 
# * **Preferences: `Open User Settings (JSON)`**:
# 
#     * **Uso**: Essa opção é usada para definir configurações globais que serão aplicadas a todas as instâncias e projetos do `VS Code` no seu ambiente de usuário.
# 
#     * **Quando usar**: Se você quer que o `PEP 8` seja aplicado em todos os projetos `Python` que você abrir no `VS Code`, faça a alteração aqui.
# 
# * **Preferences: `Open Default Settings (JSON)`**:
# 
#     * **Uso**: Este arquivo contém as configurações padrão do `VS Code`, mas **NÃO** é recomendável fazer alterações diretamente neste arquivo. Ele serve mais como referência para ver as configurações padrão.
# 
#     * **Quando usar**: Não faça modificações aqui.
# 
# * **Preferences: `Open Workspace Settings (JSON)`**:
# 
#     * **Uso**: Este arquivo armazena configurações específicas para o _workspace_ ou pasta de projeto atual. As configurações que você fizer aqui só serão aplicadas ao projeto aberto no momento.
# 
#     * **Quando usar**: Use esta opção se você quer que as configurações de `PEP 8` sejam aplicadas apenas ao projeto atual e **NÃO** a todos os projetos.
# 
# **Qual opção escolher?**
# 
# * **Se você quer aplicar as configurações do PEP 8 para todos os projetos no VS Code**: Escolha `Preferences: Open User Settings (JSON)`.
# 
# * **Se você quer aplicar as configurações apenas para o projeto atual**: Escolha `Preferences: Open Workspace Settings (JSON)`.
# 
# Normalmente, a opção mais usada é `Open User Settings (JSON)`, pois assim o comportamento será consistente em todos os projetos que você abrir.

# ### 3.2 Configurar o(s) _linters_ (`flake8` ou `pylint`) no `VS Code`
# 
# Para garantir que o `VS Code` considere o `PEP 8` (o guia de estilo para Python) ao editar seus códigos, você pode configurar algumas extensões e ajustes nas configurações do editor. Aqui estão os passos para configurar isso:
# 
# 1. **Instalar `pylint` e/ou `flake8`**:
# 
#     1.1 Para instalar o `pylint`, use:
# 
#     ```
#     pip install pylint
#     ```
# 
#     1.2 Você pode instalar um _linter_ específico. O `flake8` é uma boa escolha, pois é leve e fácil de usar. Você pode instalá-lo usando `pip`:
# 
#     ```
#     pip install flake8
#     ```
# 
# 2. **Configurar o(s) _linters_ (`pylint` e/ou `flake8`) no `VS Code`**: Você pode adicionar diretamente ao seu arquivo de configuração `settings.json`:
# 
#     ```json
#     {
#         "python.linting.enabled": true,
#         "python.linting.flake8Enabled": true,
#         "python.linting.pylintEnabled": false  // ou true, dependendo do que você preferir
#     }
#     ```
# 
# 3. **Configurar o Formatação de Código**:
# 
#     3.1 Para formatar seu código automaticamente de acordo com o PEP 8 ao salvar, você pode usar o `autopep8` ou `black`. Para instalar o `autopep8`, execute:
# 
#     ```bash
#     pip install autopep8
#     ```
# 
#     3.2 Para configurar a formatação automática ao salvar, adicione ao seu `settings.json`:
# 
#     ```json
#     {
#         "python.formatting.provider": "autopep8",
#         "editor.formatOnSave": true
#     }
#     ```
# 
# 4. **Verificar o Código**: Após configurar tudo, abra um arquivo `Python` e você deve ver as sugestões e avisos do _linter_ em relação ao estilo do `PEP 8`. Você também pode formatar seu código com a tecla de atalho (`Shift+Alt+F` ou `Ctrl+Shift+I`).
# 
# **Conclusão**
# 
# Com essas configurações, o `VS Code` considerará o `PEP 8` ao editar códigos `Python`, ajudando a manter um estilo de código consistente e legível. Essas ferramentas **NÃO** apenas ajudam a detectar problemas de estilo, mas também promovem boas práticas de codificação.

# ### 3.3 Comprimento Máximo da Linha
# 
# #### 3.3.1 Descrição [3]
# 
# Limite todas as linhas a no máximo **79 caracteres**.
# 
# Para blocos longos de texto com menos restrições estruturais (como *docstrings* ou comentários), o comprimento da linha deve ser limitado a **72 caracteres**.
# 
# Limitar a largura da janela do editor torna possível visualizar vários arquivos lado a lado, e funciona bem ao usar ferramentas de revisão de código que exibem as duas versões em colunas adjacentes.
# 
# A quebra de linha padrão na maioria das ferramentas prejudica a estrutura visual do código, dificultando a leitura. Os limites são definidos para evitar quebras de linha em editores com largura de janela configurada para 80 colunas, mesmo que a ferramenta coloque um marcador visual na última coluna ao quebrar a linha. Algumas ferramentas baseadas na *web* podem nem oferecer quebra dinâmica de linha.
# 
# Algumas equipes preferem um comprimento de linha maior. Para código mantido exclusivamente — ou principalmente — por uma equipe que entrou em acordo sobre isso, é aceitável aumentar o limite para até **99 caracteres**, desde que os comentários e *docstrings* ainda sejam limitados a **72 caracteres**.
# 

# #### 3.3.2 Como configurar o limite visual de caracteres no `VS Code`
# 
# 1. **Abra a Paleta de Comandos (`Ctrl+Shift+P`), digite **“Reload Window”** e pressione `Enter`**.
# 
# 2. Digite: `settings.json`
# 
# 3. Clique com o botão esquerdo do mouse em `Preferences: Open User Settings (JSON)`
# 
# 4. **Editar o `settings.json`**: Você pode adicionar a seguinte configuração:
# 
#     ```json
#     {
#         // outras configurações...
#         "editor.rulers": [79],
#         "editor.wordWrap": "on"  // opcional: quebra de linha automática
#     }
#     ```
# 
#     Se quiser usar `72` em vez de `79`, basta trocar `"editor.rulers": [79]` por `"editor.rulers":
#      [72]`.
#      
#     Se quiser os dois, use:
# 
#     ```json
#     "editor.rulers": [72, 79, 99]
#     ```
# 
# O `VS Code` mostrará uma linha vertical cinza (ou da cor do seu tema) na coluna especificada. Isso 
# **NÃO** bloqueia a digitação além do limite, mas ajuda visualmente a manter o padrão.
# 

# ## 4. Extensões
# 
# ### 4.1 Extensões recomendadas
# 
# | Extensão                                      | Descrição |
# |-----------------------------------------------|-----------|
# | `github.copilot`                              | Assistente de IA da GitHub que sugere trechos de código para aumentar a produtividade. |
# | `github.copilot-chat`                         | Extensão do GitHub Copilot que permite a interação por chat para sugestões de código. |
# | `gitlab.gitlab-workflow`                      | Ferramentas para integração com GitLab e fluxo de trabalho direto no VS Code. |
# | `james-yu.latex-workshop`                     | Extensão para facilitar a edição de documentos LaTeX no VS Code, com visualização de PDF. |
# | `mechatroner.rainbow-csv`                     | Ferramenta para visualizar e editar arquivos CSV com formatação colorida no VS Code. |
# | `ms-ceintl.vscode-language-pack-pt-br`        | Pacote de idioma para o VS Code em português do Brasil. |
# | `ms-python.debugpy`                           | Ferramenta para depuração de código Python no VS Code. |
# | `ms-python.isort`                             | Extensão para organizar automaticamente importações em código Python. |
# | `ms-python.python`                            | Extensão oficial do Python para o VS Code, oferecendo recursos como execução, depuração e linting. |
# | `ms-python.vscode-pylance`                    | Extensão para autocompletar e análise de tipo no Python, baseada no PyLance. |
# | `ms-toolsai.datawrangler`                    | Ferramenta para manipulação e análise de dados diretamente no VS Code. |
# | `ms-toolsai.jupyter`                          | Suporte ao Jupyter Notebooks no VS Code, para trabalhar com notebooks interativos de Python. |
# | `ms-toolsai.jupyter-keymap`                   | Mapeamento de teclas específico para trabalhar com Jupyter Notebooks no VS Code. |
# | `ms-toolsai.jupyter-renderers`                | Extensão para renderizar saídas de células em Jupyter Notebooks no VS Code. |
# | `ms-toolsai.vscode-jupyter-cell-tags`         | Permite adicionar tags às células de Jupyter Notebooks no VS Code para melhorar a organização. |
# | `ms-toolsai.vscode-jupyter-slideshow`         | Ferramenta para criar apresentações interativas com Jupyter Notebooks no VS Code. |
# | `ms-vscode.cmake-tools`                       | Ferramenta para suporte ao CMake, permitindo configurar e compilar projetos no VS Code. |
# | `ms-vscode.makefile-tools`                    | Ferramenta para suportar projetos que utilizam Makefiles, permitindo compilação e execução de tarefas. |
# | `ms-vsliveshare.vsliveshare`                  | Permite a colaboração em tempo real com outros desenvolvedores dentro do VS Code, compartilhando o ambiente de trabalho. |
# | `redhat.vscode-xml`                           | Extensão para trabalhar com arquivos XML no VS Code, oferecendo validação e formatação. |
# | `twxs.cmake`                                  | Extensão para facilitar o uso de CMake no VS Code, permitindo criar e configurar projetos C++ facilmente. |
# | `visualstudioexptteam.intellicode-api-usage-examples` | Exemplos de uso da API IntelliCode, proporcionando sugestões de código baseadas em inteligência artificial. |
# | `visualstudioexptteam.vscodeintellicode`      | Extensão que oferece sugestões inteligentes de código, melhorando a produtividade com IA. |
# | `vscjava.vscode-gradle`                       | Suporte completo para projetos Gradle em Java no VS Code, com construção e depuração. |
# | `vscjava.vscode-maven`                        | Suporte ao Apache Maven para gerenciamento de dependências e construção de projetos Java no VS Code. |
# 

# ### 4.2 Instalar uma extensão
# 
# Para instalar uma extensão no `VS Code`, siga os passos abaixo:
# 
# 1. **Abrir o VS Code**:
# 
#     1.1 Inicie o `VS Code` no seu computador.
# 
# 2. **Acessar a Visualização de Extensões**:
# 
#     2.1 Clique no ícone de Extensões na barra lateral esquerda ou pressione `Ctrl+Shift+X` para abrir a visualização de extensões.
# 
# 3. **Pesquisar a Extensão**:
# 
#     2.2 No campo de pesquisa que aparece no topo da barra lateral de extensões, digite o nome da extensão que você deseja instalar (por exemplo, `Python`, `C++`, `GitLab` etc.).
# 
# 4. **Selecionar e Instalar a Extensão**:
# 
#     4.1 Após encontrar a extensão desejada na lista de resultados, clique nela para abrir a página de detalhes.
# 
#     4.2 Clique no botão `Instalar` para adicionar a extensão ao seu ambiente de desenvolvimento.
# 
# 5. **Configurar a Extensão (se necessário)**:
# 
#     5.1 Algumas extensões podem exigir configurações adicionais. Para fazer isso, você pode acessar as configurações do `VS Code` (`File > Preferences > Settings ou Ctrl+,`) e procurar pela extensão instalada para ajustar suas opções conforme necessário.
# 
# 6. **Reiniciar o `VS Code` (se necessário)**:
# 
#     6.1 Embora a maioria das extensões seja ativada automaticamente, em alguns casos, pode ser necessário reiniciar o `VS Code` para que todas as funcionalidades da extensão sejam corretamente carregadas.
# 
# Após esses passos, a extensão estará pronta para uso no seu `VS Code`!

# ### 4.3 Consultar extensões instaladas através de linha de comando
# 
# 1. Você pode verificar as extensões instaladas no `VS Code` através da linha de comando. Para isso, use o seguinte comando no `Terminal Emulator` do `VS Code`:
# 
#     ```bash
#     code --list-extensions
#     ```
# 
#     Esse comando vai listar todas as extensões instaladas no seu `VS Code`. Caso queira obter mais detalhes sobre uma extensão específica, como sua versão, você pode adicionar o parâmetro `--show-versions`:
# 
#     ```bash
#     code --list-extensions --show-versions
#     ```
#     
#     Isso mostrará todas as extensões junto com suas versões atuais.
# 

# ### 4.3 Desinstalar uma extensão
# 
# Para desinstalar uma extensão no `VS Code`, siga os passos abaixo:
# 
# 1. **Abrir o `VS Code`**:
# 
#    1.1 Inicie o `VS Code` no seu computador.
# 
# 2. **Acessar a Visualização de Extensões**  
#    
#    2.1 Clique no ícone de **Extensões** na barra lateral esquerda ou pressione `Ctrl+Shift+X`.
# 
# 3. **Localizar a Extensão**  
#    
#    3.1 No campo de pesquisa, digite o nome da extensão que deseja remover (por exemplo, `Python`, `C++`, `GitLab` etc.).
# 
# 4. **Selecionar e Desinstalar**  
#    
#    4.1 Clique na extensão para abrir sua página de detalhes.  
#    
#    4.2 Clique no botão **Desinstalar**.
# 
# 5. **Reiniciar o VS Code (se necessário)**  
#    
#    5.1 Em alguns casos, é preciso recarregar a janela do editor para encerrar o servidor de linguagem (LSP) da extensão.  
#    
#    5.2 Abra a Paleta de Comandos (`Ctrl+Shift+P`), digite **“Reload Window”** e pressione `Enter`.
# 
# 6. **Limpe caches (opcional)**  
#    
#    Algumas LSPs armazenam arquivos em cache em:  
#    
#    ```bash
#    ~/.vscode/extensions/
#    ```
#    

# #### 4.3.1 Verificar se existe versões antigas do `jupyter` instaladas em paralelo
# 
# Você ainda tem várias versões antigas do extension host do Jupyter instaladas em paralelo e **NÃO** removidas, por isso aparecem tantos diretórios `ms-toolsai.jupyter-*`. O `VS Code` **NÃO** apaga automaticamente versões antigas quando você atualiza uma extensão, ele cria um novo diretório a cada versão.
# 
# Para liberar espaço e parar de carregar instâncias órfãs, você pode:
# 
# **ATENÇÃO**: Possivelmente, se você apagar alguma versão do `jupyter` antiga, porém, compatível com versões de `Python` mais antigos, pode ser que as teclas de atalho se alterem. Poirtanto, sugiro usar esse passo a passo como um tutorial real para excluir outras extensões que não esteja utilizando e que estejam em duplicidade.
# 
# 1. **Manter apenas a última versão**: Digamos que a versão mais recente seja, por exemplo, `ms-toolsai.jupyter-2025.4.1-linux-x64`. Você pode remover todas as outras com algo como:
# 
#     ```bash
#     cd ~/.vscode/extensions
#     ls -d ms-toolsai.jupyter-* | grep -v 2025.4.1 | xargs rm -rf
#     ```
# 
# 2. **Fazer o mesmo para outras extensões **NÃO** usadas
# 
#     * `github.copilot-chat` se **NÃO** usa o _chat_ do `Copilot`
# 
#     * `mechatroner.rainbow-csv` se **NÃO** trabalha com CSV colorido
# 
#     * `ms-vscode-remote.remote-wsl` se **NÃO** desenvolve no WSL
# 
#     * `ms-vsliveshare.vsliveshare` se **NÃO** usa Live Share
# 
#     * `redhat.vscode-xml` se **NÃO** edita XML
# 
# 3. **Recarregar o `VS Code`**
# 
#     Após remover os diretórios antigos, abra o Command Palette (`Ctrl+Shift+P`) e execute `Reload Window` para reiniciar o Extension Host e efetivamente encerrar os servidores LSP órfãos.
# 
# Dessa forma você mantém apenas o que realmente usa e reduz significativamente o consumo de memória.

# ### 5. Habilitar o `PyLance`
# 
# Para habilitar o `PyLance` no `VS Code`, siga os passos abaixo:
# 
# 1. **Instalar a Extensão `PyLance`**:
# 
#     1.1 Abra o `VS Code`.
# 
#     1.2 Vá até a visualização de extensões clicando no ícone de quadrado no menu lateral esquerdo ou pressione: `Ctrl+Shift+X`.
# 
#     1.3 No campo de pesquisa, digite `PyLance`.
# 
#     1.4 Clique na extensão `PyLance` da `Microsoft` e depois clique em Instalar.
# 
# 2. **Configurar o `PyLance` como o servidor de linguagem `Python`**:
# 
#     2.1 Após a instalação, `PyLance` será ativado automaticamente, mas você pode verificar ou alterar a configuração manualmente.
# 
#     2.2 Abra a configuração do `VS Code` clicando em `File > Preferences > Settings` ou pressionando `Ctrl+,`.
# 
#     2.3 Na barra de pesquisa de configurações, digite `python.languageServer`.
# 
#     2.4 No campo de configuração que aparecer, altere o valor para `Pylance` (se **NÃO** estiver configurado automaticamente).
# 
# 3. **Reinicie o `VS Code`**:
# 
#     3.1 Para garantir que as configurações sejam aplicadas corretamente, reinicie o `VS Code`.
# 
# Com isso, o `PyLance` estará ativado e você poderá aproveitar os recursos avançados como autocompletar, análise de tipos estática, navegação de código e outros recursos de produtividade no seu projeto `Python`.
# 

# ## 6. Atalhos para visualizar objetos
# 
# Essa funcionalidade é separada em algumas ferramentas, e depende da linguagem que você está usando (ex: `Python`, `C#`, `JavaScript` etc.). Para `Python`, por exemplo, e para outras linguagens também, você tem:
# 
# | Recurso                        | O que faz                                                                 | Como acessar                                              |
# |-------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------|
# | **Ir para Definição**         | Vai para onde a função/objeto/classe está definido                        | `F12`, `Ctrl+Clique` ou clique com o botão direito do mouse e escolha a opção `"Go to Definition"`              |
# | **Procurar Simbologia**       | Lista todas funções, classes, variáveis do projeto                        | `Ctrl+T`                                                  |
# | **Exibir Esquema do Arquivo** | Mostra todas funções/classe/variáveis dentro do arquivo atual             | `Ctrl+Shift+O`                                            |
# | **Pesquisar na Árvore de Símbolos** | Pesquisa em todo o projeto                                          | `Ctrl+P`, depois digite `#nome`                           |
# | **IntelliSense**              | Autocompleta e sugere funções, propriedades, métodos                      | `Ctrl+Espaço` (ou automático conforme digita)             |
# | **Extensões específicas**     | Instalar extensões como *Python*, *Pylance*, *IntelliCode* etc.          | Pela aba de extensões no `VS Code` (`Ctrl+Shift+X`)         |
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar o `vs code` no `linux ubuntu` pelo `terminal emulator`.*** Disponível em: <https://chat.openai.com/c/073320a8-7cc5-4590-9da0-d2bcc7093c88> (texto adaptado). Acessado em: 17/10/2023 16:05.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
# [3] PYTHON TEAM. ***Pep 8 – style guide for python code***. Disponível em: <https://peps.python.org/pep-0008/> (texto adaptado). Acessado em: 06/06/2025 10:02.
# 
