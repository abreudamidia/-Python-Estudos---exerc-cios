from rich import print
from rich.panel import Panel
from rich.table import Table

# 1. Exemplo de Print Colorido (Estilização)
print("\n[bold cyan]1. EXEMPLO DE PRINT COLORIDO[/]")
print("O Python é [bold green]incrível[/], o terminal é [bold red]colorido[/] e o Danilo é [u]Engenheiro[/]!")

print("\n" + "="*50)

# 2. Exemplo de Painel (Moldura)
print("[bold cyan]2. EXEMPLO DE PAINEL (PANEL)[/]")
meu_painel = Panel(
    "Este é um texto dentro de um [bold yellow]Painel[/].\nIdeal para avisos ou títulos importantes.",
    title="[bold]SISTEMA TELEFLIX[/]",
    subtitle="Versão 1.0",
    border_style="magenta",
    expand=False
)
print(meu_painel)

print("\n" + "="*50)

# 3. Exemplo de Tabela (Dados Organizados)
print("[bold cyan]3. EXEMPLO DE TABELA (TABLE)[/]")
tabela = Table(title="[bold white]PLANOS TELEFLIX CANAIS[/]", border_style="blue")

# Criando as colunas
tabela.add_column("Plano", style="cyan", no_wrap=True)
tabela.add_column("Duração", style="magenta")
tabela.add_column("Preço", justify="right", style="green")

# Adicionando as linhas (seus dados)
tabela.add_row("Bronze", "30 Dias", "R$ 35,00")
tabela.add_row("Prata", "90 Dias", "R$ 90,00")
tabela.add_row("Ouro (VIP)", "365 Dias", "R$ 320,00")

# Mostrando a tabela
print(tabela)

print("\n[bold green]>>> TUDO FUNCIONANDO! PRR PRR PATAPIMBA! <<<[/]\n")