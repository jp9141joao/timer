# **Cronômetro (Timer)**

Este é um projeto em Python que implementa um cronômetro com opções de tempo configuráveis, permitindo que o usuário defina a duração e o formato (horas, minutos, segundos ou centésimos). O cronômetro conta regressivamente até zerar e oferece a opção de retornar ao menu principal.

---

## **Funcionalidades**

- **Configuração de Tempo:** O usuário pode definir a duração do cronômetro em horas, minutos, segundos ou centésimos.
- **Contagem Regressiva:** O cronômetro conta regressivamente e exibe o tempo restante de forma clara no terminal.
- **Opções de Menu:**
  - Iniciar o cronômetro.
  - Sair do programa.

---

## **Como Usar**

1. Execute o programa no terminal.
2. O menu principal será exibido, permitindo que você escolha entre:
   - **1** para iniciar o cronômetro.
   - **2** para sair do programa.
3. Ao iniciar o cronômetro:
   - Informe o tempo desejado.
   - Escolha a unidade de tempo (horas, minutos, segundos ou centésimos).
4. O cronômetro começará a contagem regressiva.
5. Após o tempo acabar, o programa pedirá para você voltar ao menu principal.

---

## **Exemplo de Execução**

Quando o programa for iniciado, o menu será exibido assim:

```
* Menu *
1- Começar
2- Sair
R: 
```

Após escolher a opção 1, o programa solicitará o tempo e a unidade:

```
Digite quanto tempo o temporizador vai ter: 5
Esse valor será em
H- Horas
M- Minutos
S- Segundos
CS- Centesimos
R: m
```

O cronômetro então começará a contagem regressiva e será exibido da seguinte forma:

```
hh:mm:ss:m
00:01:00:9
```

O cronômetro continuará a contagem até zerar.

---

## **Requisitos**

- **Python 3.x**: O código foi desenvolvido para funcionar com versões mais recentes do Python.

---

## **Como Executar**

1. Certifique-se de ter o Python 3 instalado no seu sistema.
2. Baixe o código-fonte e salve-o em um arquivo chamado `cronometro.py`.
3. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
4. Execute o comando:
   ```bash
   python cronometro.py
   ```

---

## **Observações**

- O comando `os.system('cls')` é utilizado para limpar a tela do terminal e funciona apenas no Windows. Se você estiver utilizando um sistema Linux ou macOS, substitua esse comando por `os.system('clear')` para garantir que a tela seja limpa corretamente.
- O programa aceita entradas apenas numéricas e respeita as condições de tempo configuráveis, validando as opções inseridas pelo usuário.

---

Divirta-se e bom uso! 😊
```