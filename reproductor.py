from pygame import mixer
class Reproductor:
    archivo = None
    def __init__(self):
        self.archivo = "CANCION DE LA INTRO DE WEFERE  LoFi, Estudiar, Relajarse, Dormir, Ambiente  - Ignacio _ Fe en Cristo.mp3"
        mixer.init()
        mixer.music.load(self.archivo)

    def reproducir(self):
        mixer.music.play()
        print("🎵 Reproduciendo...")

    def pausar(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            print("⏸️ Canción pausada.")
        else:
            mixer.music.unpause()
            print("▶️ Canción reanudada.")
    def subirVolumen():
        

if __name__ == "__main__":
    player = Reproductor()
    player.reproducir()

   