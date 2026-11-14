import pygame
import os
import wave
import random
# pygame setup
pygame.init()
size=[1280, 720]
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
background=None
color=pygame.Color("green")
print(color.hsla)
# what galaxy are we in right now :P samsung galaxy s5 :samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji::samsung galaxy s5 emoji:
# lets go try the dubai chocolate ube matcha golden 24 karat labubu crumbl coookie panera lemonade shake :DDDDDD
# hey me from the future uh hows pokemon winds and waves (response: idfk it didnt release)
songs = [f"songs\\{i}" for i in os.listdir("songs")]
random.shuffle(songs)
#print (songs)

if pygame.mixer.get_init():
    song = songs[0]
    next_song= songs[1]
    pygame.mixer.music.load(song)
    pygame.mixer.music.queue(next_song)
    pygame.mixer.music.play()

def toggle():
    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
    else:
                        pygame.mixer.music.unpause()

def nextsong():
    global song
    global next_song
    songs.append(songs.pop(0))
    song, next_song=next_song, songs[1]
    pygame.mixer.music.load(song)
    pygame.mixer.music.queue(next_song)
    pygame.mixer.music.play()


logo=pygame.image.load("images/International_Pokémon_logo.svg.png")
rewind=pygame.image.load("images/rewindorsmth.png")
rewind=pygame.transform.scale(rewind, (90,90))
ff=pygame.image.load("images/fastforward-removebg-preview.png")
#ff = ff.subsurface(ff.get_bounding_rect())
ff=pygame.transform.scale(ff, (159,159))
loop=pygame.image.load("images/loop.png")
loop=pygame.transform.scale(loop, (110,110))
looptrack=pygame.image.load("images/looptrack-removebg-preview.png")
looptrack=pygame.transform.scale(looptrack, (150,110))
pause=pygame.image.load("images/pause.png")
pause=pygame.transform.scale(pause, [90,90])
play=pygame.image.load("images/play-removebg-preview.png")
play=pygame.transform.scale(play, (85,85))
playlist=pygame.image.load("images/6398977.png")
search=pygame.image.load("images/search.png")
file=pygame.image.load("images/4807934.png")
file=pygame.transform.smoothscale_by(file, 0.25)
file.set_alpha(100) #67



buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self,color = "red",text = "button",rect = pygame.Rect(0,0,100,20)):
        super().__init__(buttons)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(color)
        self.text=text
        
r1 =pygame.Rect(250,500,145,100)

for i in range(4):
    Button(rect=r1.move(i*200,0))       


Brewind, Bplay, Bff, Bloop = buttons.sprites()
looping=False
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if file.get_rect().collidepoint(pos):
                      window1 = pygame.Window(position = [1000,0])
                if Brewind.rect.collidepoint(event.pos):
                    if pygame.mixer.music.get_pos()<=3000:
                        print("boo")
                    else:
                        print(f"{pygame.mixer.music.get_pos() = }")
                        pygame.mixer.music.stop()
                        pygame.mixer.music.rewind()
                        if looping:
                            
                            pygame.mixer.music.play(-1)
                        else:
                              pygame.mixer.music.play()
                    

                if Bff.rect.collidepoint(event.pos):
                    #pygame.mixer.music.set_pos(1000)
                    nextsong()


                if Bplay.rect.collidepoint(event.pos):
                    print ("hi")
                    toggle()
                if Bloop.rect.collidepoint(event.pos):
                      print("loop")
                      looping=not looping
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("play,pause")
                toggle()
            elif event.key== pygame.K_RIGHT:
                pygame.mixer.music.set_pos(-1)
                pygame.mixer.music.queue(songs.pop(0))
        if event.type == pygame.DROPFILE:
              print(event)
              if event.file.endswith(".mp3")or event.file.endswith(".wav") or event.file.endswith(".ogg"):
                    s=pygame.mixer.Sound(event.file)
                    data = s.get_raw()
                    with open("temp.txt", "w") as f:
                          f.write(str(data))
                    with wave.open("imports/temp.wav","wb") as file:
                          freq, _, channels = pygame.mixer.get_init()
                          file.setframerate(freq)
                          file.setnchannels(channels)
                          file.setsampwidth(2)
                          file.writeframes(data)

                    next_song=event.file
                    nextsong()

                
    screen.fill("purple")
    
    buttons.update()
    buttons.draw(screen)
    if pygame.mixer.music.get_busy():
        screen.blit(pause, r1.move(230,5))
    else:
        screen.blit(play,r1.move(230,5))
    screen.blit(rewind,r1.move(27,3))
    screen.blit(ff, r1.move(395,-25))
    if looping:
        screen.blit(loop, r1.move(615,-5))
    else:
        screen.blit(looptrack, r1.move(595,-5))
    if file.get_rect().collidepoint(pos):
                          file.set_alpha(255)
    else:
         file.set_alpha(100) 
    screen.blit(file,[0,0])
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
# how to make a rejection scene: "i like you :3" "well i dont" (gets depression)