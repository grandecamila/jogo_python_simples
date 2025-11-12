import pgzrun  
import math, random  
  
TITLE = "Mila Jogo TESTE"  
WIDTH = 800  
HEIGHT = 400  


# ESTADOS DO JOGO  
estado = "menu"  
som_ativo = True  
  

# VARIÁVEIS DO PLAYER  
player = {  
    "x": 100,  
    "y": 300,  
    "vel_y": 0,  
    "no_chao": True  
}  

  
# INIMIGOS  
inimigos = []  
for i in range(3):  
    inimigos.append({  
        "x": random.randint(400, 800),  
        "y": 300,  
        "vel": random.randint(2, 4)  
    })  

  
# FUNÇÕES AUXILIARES  
def resetar_jogo():  
    global estado, player, inimigos  
    estado = "menu"  
    player["x"], player["y"], player["vel_y"], player["no_chao"] = 100, 300, 0, True  
    for i in range(3):  
        inimigos[i]["x"] = random.randint(400, 800)  
        inimigos[i]["vel"] = random.randint(2, 4)  
  
def desenhar_texto_menu():  
    screen.draw.text("MINI PLATFORMER", center=(WIDTH/2, 80), fontsize=60, color="white")  
    screen.draw.text("1 - Iniciar Jogo", center=(WIDTH/2, 160), fontsize=40, color="yellow")  
    screen.draw.text(f"2 - Som: {'Ligado' if som_ativo else 'Desligado'}", center=(WIDTH/2, 210), fontsize=40, color="yellow")  
    screen.draw.text("3 - Sair", center=(WIDTH/2, 260), fontsize=40, color="yellow")  
  
def desenhar_texto_gameover():  
    screen.draw.text("VOCÊ PERDEU!", center=(WIDTH/2, 120), fontsize=70, color="red")  
    screen.draw.text("Pressione R para reiniciar", center=(WIDTH/2, 220), fontsize=40, color="yellow")  
  

# DRAW  
def draw():  
    screen.clear()  
    if estado == "menu":  
        desenhar_texto_menu()  
    elif estado == "jogando":  
        screen.draw.filled_rect(Rect((0, 350), (WIDTH, 50)), (80, 50, 30))  
        screen.draw.filled_rect(Rect((player["x"], player["y"]), (30, 40)), (50, 200, 255))  
        for e in inimigos:  
            screen.draw.filled_rect(Rect((e["x"], e["y"]), (30, 30)), (255, 60, 60))  
    elif estado == "gameover":  
        desenhar_texto_gameover()  

  
# UPDATE LOOP  
def update():  
    global estado  
  
    if estado == "menu":  
        return  
  
    if estado == "jogando":  
        atualizar_player()  
        atualizar_inimigos()  
        checar_colisoes()  
  

# PLAYER  
def atualizar_player():  
    if keyboard.left:  
        player["x"] -= 4  
    if keyboard.right:  
        player["x"] += 4  
  
    # gravidade  
    player["vel_y"] += 0.4  
    player["y"] += player["vel_y"]  
  
    # chão  
    if player["y"] >= 300:  
        player["y"] = 300  
        player["vel_y"] = 0  
        player["no_chao"] = True  
  
def checar_colisoes():  
    global estado  
    for e in inimigos:  
        if abs(player["x"] - e["x"]) < 25 and abs(player["y"] - e["y"]) < 30:  
            estado = "gameover"  
  
def atualizar_inimigos():  
    for e in inimigos:  
        e["x"] -= e["vel"]  
        if e["x"] < -30:  
            e["x"] = random.randint(WIDTH, WIDTH+200)  
            e["vel"] = random.randint(2, 4)  
  

# TECLAS  
def on_key_down(key):  
    global estado, som_ativo  
    if estado == "menu":  
        if key == keys.K_1:  
            estado = "jogando"  
        elif key == keys.K_2:  
            som_ativo = not som_ativo  
        elif key == keys.K_3:  
            exit()  
  
    elif estado == "jogando":  
        if key == keys.SPACE or key == keys.W:  
            if player["no_chao"]:  
                player["vel_y"] = -8  
                player["no_chao"] = False  
                if som_ativo and hasattr(sounds, "jump"):  
                    sounds.jump.play()  
  
    elif estado == "gameover":  
        if key == keys.R:  
            resetar_jogo()  
  

# EXECUÇÃO DO JOGO  
pgzrun.go()  
