import random


def Player():
    return {
        "hp": 100,
        "ouro": 50,
        "attack": 10,
        "xp": 0,
        "inventory": []
    }


def Enemy(nome, hp, ataque, recompensa_ouro, recompensa_xp):
    return {
        "nome": nome,
        "hp": hp,
        "attack": ataque,
        "ouro": recompensa_ouro,
        "xp": recompensa_xp
    }


def Status(jogador):
    print(f"\nHP: {jogador['hp']} | Gold: {jogador['ouro']} | Attack: {jogador['attack']} | XP: {jogador['xp']}")
    print(f"Inventory: {', '.join(jogador['inventory']) if jogador['inventory'] else 'Empty'}")


def lutar(jogador, inimigo):
    print(f"\n Você encontrou um {inimigo['nome']}!")

    while jogador["hp"] > 0 and inimigo["hp"] > 0:
        acao = input("Você quer atacar (a) ou fugir (f)? ").lower()

        if acao == "a":
            dano = random.randint(jogador["attack"] - 2, jogador["attack"] + 2)
            inimigo["hp"] -= dano
            print(f"Você atacou e causou {dano} de dano! {inimigo['nome']} tem {inimigo['hp']} HP restante.")

            if inimigo["hp"] > 0:
                dano_inimigo = random.randint(inimigo["attack"] - 2, inimigo["attack"] + 2)
                jogador["hp"] -= dano_inimigo
                print(
                    f"{inimigo['nome']} atacou e causou {dano_inimigo} de dano! Você tem {jogador['hp']} HP restante.")

        elif acao == "f":
            print("Você fugiu da luta!")
            return

    if jogador["hp"] > 0:
        print(f"\n Você derrotou o {inimigo['nome']}!")
        jogador["ouro"] += inimigo["ouro"]
        jogador["xp"] += inimigo["xp"]
        print(f"Você ganhou {inimigo['ouro']} ouro e {inimigo['xp']} XP!")


def loja(jogador):
    print("\n Bem-vindo à loja! O que deseja comprar?")
    itens = {
        "1": ("Espada (+5 ataque)", 30, "Espada"),
        "2": ("Poção (+20 HP)", 20, "Poção"),
        "3": ("Armadura (+10 HP)", 40, "Armadura"),
        "4": ("Sair", 0, None)
    }

    for chave, (desc, preco, _) in itens.items():
        print(f"{chave} - {desc} por {preco} ouro")

    escolha = input("Escolha um item para comprar: ")
    if escolha in itens and jogador["ouro"] >= itens[escolha][1]:
        jogador["ouro"] -= itens[escolha][1]
        if itens[escolha][2] == "Espada":
            jogador["attack"] += 5
        elif itens[escolha][2] == "Poção":
            jogador["hp"] += 20
        elif itens[escolha][2] == "Armadura":
            jogador["hp"] += 10
        jogador["inventory"].append(itens[escolha][2])
        print(f" Você comprou {itens[escolha][2]}!")
    elif escolha in itens:
        print(" Ouro insuficiente.")
    else:
        print(" Opção inválida.")


def bau(jogador):
    Ob = random.randint(20, 50)
    print(f"\n Você encontrou um baú de tesouro! Ele contém {Ob} ouro!")
    jogador["ouro"] += Ob


def boss_final(jogador):
    boss = Enemy("Dragão Ancião", 100, 20, 100, 100)
    print("\n CHEGOU A HORA DA BATALHA FINAL! ")
    lutar(jogador, boss)

    if jogador["hp"] > 0:
        print("\n PARABÉNS! Você derrotou o chefe final e venceu o jogo! ")
    else:
        print("\n Você foi derrotado pelo chefe final. Fim de jogo.")


def jogo():
    jogador = Player()
    num_salas = 10

    print(" Bem-vindo ao jogo de exploração! ⚔")

    for _ in range(num_salas):
        Status(jogador)
        direcao = input("\nVocê quer ir para a esquerda (e) ou para a direita (d)? ").lower()

        evento = random.choice(["Loja", "Luta", "Tesouro"])

        if evento == "Loja":
            loja(jogador)
        elif evento == "Luta":
            inimigo = Enemy("Goblin", random.randint(20, 40), random.randint(5, 10), random.randint(10, 20),
                                    random.randint(5, 15))
            lutar(jogador, inimigo)
            if jogador["hp"] <= 0:
                print("\n Você foi derrotado. Fim de jogo.")
                return
        elif evento == "Tesouro":
            bau(jogador)

    boss_final(jogador)


jogo()
