import yfinance as yf

acoes = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'MXRF11.SA']  # .SA para indicar ações da B3

for acao in acoes:
    ticker = yf.Ticker(acao)
    preco_atual = ticker.history(period='1d')['Close'][0]
    print(f"Ação: {acao} - Preço atual: R$ {preco_atual:.2f}")
