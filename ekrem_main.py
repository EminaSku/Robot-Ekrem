import subprocess
import pygame
import sys
import speech_recognition as sr
from pygame.locals import QUIT, MOUSEBUTTONDOWN

def main():
    pygame.init()
    pygame.mixer.init()
    

    screen = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Zdravo!")

    # Load your background image
    background = pygame.image.load("/home/ekrem/Pictures/Pocetna.png")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))

    # Define button properties
    # button_color = (0, 0, 0, 0)  # Yellow color
    button_rect = pygame.Rect(715, 343, 66, 66)  # Position and size of the button
    border_radius = 5
    
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    open_new_window()

        # Draw background
        screen.blit(background, (0, 0))

        # Draw button
        # pygame.draw.rect(screen, button_color, button_rect,0 )  # Draws a rounded button

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def open_new_window():
    new_window = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Glavni meni")
    
    # Set background color
    # white_color = (255, 255, 255)
    # new_window.fill(white_color)
    # Load your background image
    background = pygame.image.load("/home/ekrem/Pictures/drugiProzor2.jpeg")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))

    # Define button properties
    # button1_color = (255, 255, 255)  # Yellow color
    button1_rect = pygame.Rect(330,88, 110, 95)  # Position and size of the button
    
    # button2_color = (255, 255, 255)  # Yellow color
    button2_rect = pygame.Rect(570,88, 110, 95)  # Position and size of the button
    
    # button3_color = (255, 255, 255)  # Yellow color
    button3_rect = pygame.Rect(330,265, 110, 95)  # Position and size of the button
    
    # button4_color = (255, 255, 255)  # Yellow color
    button4_rect = pygame.Rect(570,265, 110, 95)  # Position and size of the button
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Check for button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos):
                open_new_window1()
            elif button2_rect.collidepoint(event.pos):
                open_new_window2()
            elif button3_rect.collidepoint(event.pos):
                open_new_window3()
            elif button4_rect.collidepoint(event.pos):
                open_new_window4()
        # Draw background
        new_window.blit(background, (0, 0))
        
        # Draw button
        # pygame.draw.rect(new_window, button1_color, button1_rect,0 )  # Draws a rounded button
        # pygame.draw.rect(new_window, button2_color, button2_rect,0 )  # Draws a rounded button
        # pygame.draw.rect(new_window, button3_color, button3_rect,0 )  # Draws a rounded button
        # pygame.draw.rect(new_window, button4_color, button4_rect,0 )  # Draws a rounded button
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
        

def open_new_window1():
    new_window = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Caskajmo")
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    
    audio_text = None  # Declare the variable outside the with block
    sound1 = pygame.mixer.Sound('/home/ekrem/Music/IamEkrem.wav')
    sound2 = pygame.mixer.Sound('/home/ekrem/Music/months.wav')
    sound3 = pygame.mixer.Sound('/home/ekrem/Music/days.wav')
    sound4 = pygame.mixer.Sound('/home/ekrem/Music/counting.wav')
    sound5 = pygame.mixer.Sound('/home/ekrem/Music/designers.wav')
    sound6 = pygame.mixer.Sound('/home/ekrem/Music/China.wav')
    sound7 = pygame.mixer.Sound('/home/ekrem/Music/YouAreCute.wav')
    sound8 = pygame.mixer.Sound('/home/ekrem/Music/Thanks.wav')
    sound9 = pygame.mixer.Sound('/home/ekrem/Music/Inspiration.wav')
    sound10 = pygame.mixer.Sound('/home/ekrem/Music/IUS.wav')
    sound11 = pygame.mixer.Sound('/home/ekrem/Music/message.wav')
    sound12 = pygame.mixer.Sound('/home/ekrem/Music/else.wav')
    sound13 = pygame.mixer.Sound('/home/ekrem/Music/counting.wav')
    
    background = pygame.image.load("/home/ekrem/Pictures/caskajmo.jpeg")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))
    
    
    # Define button properties
    button_color = (255, 255, 0)  # Yellow color
    button_rect = pygame.Rect(40, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    # Define button properties
    button1_color = (255, 255, 0)  # Yellow color
    button1_rect = pygame.Rect(705, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    font = pygame.font.Font(None, 36)
    text = font.render("<", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    open_new_window()
                if button1_rect.collidepoint(event.pos):
                    # listening to the speech and store in audio_text variable
                    with sr.Microphone() as source:
                        print("Talk")
                        try:
                            # Adjust timeout and phrase_time_limit as needed
                            audio_text = r.listen(source, timeout=3, phrase_time_limit=7
                                                  )
                            print("Time over, thanks")
                        except sr.WaitTimeoutError:
                            print("Listening timed out while waiting for phrase to start")
                            if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                            sound13.play()

                    # Using exception handling for the recognize_() method
                    if audio_text:  # Check if audio_text is not None
                        try:
                            # Using Google's speech recognition
                            print("Text: " + r.recognize_google(audio_text))
                            text = r.recognize_google(audio_text)
                            
                            if "tell me something about yourself" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound1.play()
                                
                            elif "can you name all months in a year" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound2.play()
                                
                            
                            elif "can you name all days in a week" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound3.play()
                                
                            
                            elif "who are your designers" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound5.play()
                                
                            
                            elif "are you made in china" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound6.play()
                                
                            
                            elif "can you see me" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound7.play()
                                
                            
                            elif "is there anyone you would like to say thank you to" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound8.play()
                                
                            
                            elif "who is your inspiration" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound9.play()
                                
                            
                            elif "can you tell me something about the international university of sarajevo" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound10.play()
                                
                            elif "what would be your message to future generations" in text.lower():
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound11.play()
                                
                            else:
                                if pygame.mixer.get_busy():
                                    pygame.mixer.stop()
                                sound13.play()
                                
                        except sr.UnknownValueError:
                            pygame.mixer.stop()
                            sound13.play()
                        except sr.RequestError as e:
                            pygame.mixer.stop()
                            sound13.play()
                            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                        except Exception as e:  # Use the general Exception class
                            print("An error occurred: {0}".format(e))
                    else:
                        print("No audio to process")
                        pygame.mixer.stop()
                        sound13.play()
        # Draw background
        new_window.blit(background, (0, 0))            
            
        # Draw button
        #pygame.draw.rect(new_window, button_color, button_rect,0 )  # Draws a rounded button
        #pygame.draw.rect(new_window, button1_color, button1_rect,0 )

        #new_window.blit(text, text_rect)        
        # Check for button click
        pygame.display.flip()
    pygame.quit()
    sys.exit()
        
        
        
        
def open_new_window2():

    new_window = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Note i bajke")
    
    # Load your background image
    background = pygame.image.load("/home/ekrem/Pictures/Note i bajke.png")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))
    new_window.blit(background, (0, 0))
    # Set background color
    # white_color = (255, 255, 255)
    # new_window.fill(white_color)
    # Define button properties
    button_color = (255, 255, 0)  # Yellow color
    button_rect = pygame.Rect(40, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    button5_color = (255, 255, 0)  # Yellow color
    button5_rect = pygame.Rect(705, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    font = pygame.font.Font(None, 36)
    text = font.render("", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)
    
    # Define button properties
    button1_color = (255, 255, 255)  # Yellow color
    button1_rect = pygame.Rect(43,135, 110, 110)
    # image1 = pygame.image.load('/home/raspberry/Pictures/paradajz.jpg')
    # image1 = pygame.transform.scale(image1,(110,110))
    # image1_position = (43,135)
    
    button2_color = (255, 255, 255)  # Yellow color
    button2_rect = pygame.Rect(238,135, 110, 110)  # Position and size of the button
    # image2 = pygame.image.load('/home/raspberry/Pictures/bajka.jpg')
    # image2 = pygame.transform.scale(image2,(110,110))
    # image2_position = (238,135)
    
    button3_color = (255, 255, 255)  # Yellow color
    button3_rect = pygame.Rect(432,135, 110, 110)  # Position and size of the button
    # image3 = pygame.image.load('/home/raspberry/Pictures/abcd.jpg')
    # image3 = pygame.transform.scale(image3,(110,110))
    # image3_position = (432,135)
    
    button4_color = (255, 255, 255)  # Yellow color
    button4_rect = pygame.Rect(632,135, 110, 110)  # Position and size of the button
    # image4 = pygame.image.load('/home/raspberry/Pictures/uspavanka.jpg')
    # image4 = pygame.transform.scale(image4,(110,110))
    # image4_position = (632,135)
    
    sound1 = pygame.mixer.Sound('/home/ekrem/Music/paradajz.wav')
    sound2 = pygame.mixer.Sound('/home/ekrem/Music/Uspavankica.wav')
    sound3 = pygame.mixer.Sound('/home/ekrem/Music/PetarPan.wav')
    sound4 = pygame.mixer.Sound('/home/ekrem/Music/abeceda.wav')
    

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                    # Check for button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos):
                #Here write the code to play one sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                sound1.play()
            elif button2_rect.collidepoint(event.pos):
                #Here write the code to play second sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                sound2.play()
            elif button3_rect.collidepoint(event.pos):
                #Here write the code to play third sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                sound3.play()
            elif button4_rect.collidepoint(event.pos):
                #Here write the code to play fourth sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
                sound4.play()
            elif button5_rect.collidepoint(event.pos):
                #Here write the code to play second sound
                if pygame.mixer.get_busy():
                    pygame.mixer.stop()
            elif button_rect.collidepoint(event.pos):
                    open_new_window()
            else:
                print("Hello")
        # Draw background
#         new_window.blit(background, (0, 0))
        
        # new_window.blit(image1, image1_position)
        # new_window.blit(image2, image2_position)
        # new_window.blit(image3, image3_position)
        # new_window.blit(image4, image4_position)
        
        
        # Draw button
        # pygame.draw.rect(new_window, button_color, button_rect,0 )  # Draws a rounded button
        # pygame.draw.rect(new_window, button5_color, button5_rect,0 )  # Draws a rounded button
        
#         new_window.blit(text, text_rect)
        pygame.display.flip()
    pygame.quit()
    sys.exit()
        
        

def open_new_window3():
    new_window = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Crtic kutak")
    
    # Load your background image
    background = pygame.image.load("/home/ekrem/Pictures/filmovi.png")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))

    # Set background color
    # white_color = (255, 255, 255)
    # new_window.fill(white_color)
    
    # Define button properties
    button_color = (255, 255, 0)  # Yellow color
    button_rect = pygame.Rect(40, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    font = pygame.font.Font(None, 36)
    text = font.render("<", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)

     # Define button properties
    button1_color = (255, 255, 255)  # Yellow color
    button1_rect = pygame.Rect(43, 143, 110, 100)
    # image1 = pygame.image.load('/home/raspberry/Pictures/fif.jpg')
    # image1 = pygame.transform.scale(image1,(110,100))
    # image1_position = (43,143)
    
    button2_color = (255, 255, 255)  # Yellow color
    button2_rect = pygame.Rect(238,165, 110, 100)  # Position and size of the button
    # image2 = pygame.image.load('/home/raspberry/Pictures/mumijevi.jpg')
    # image2 = pygame.transform.scale(image2,(110,100))
    # image2_position = (238,143)
    
    button3_color = (255, 255, 255)  # Yellow color
    button3_rect = pygame.Rect(432, 143, 110, 100)
    # image3 = pygame.image.load('/home/raspberry/Pictures/fif.jpg')
    # image3 = pygame.transform.scale(image3,(110,100))
    # image3_position = (432,143)
    
    button4_color = (255, 255, 255)  # Yellow color
    button4_rect = pygame.Rect(632,165, 110, 100)  # Position and size of the button
    # image4 = pygame.image.load('/home/raspberry/Pictures/mumijevi.jpg')
    # image4 = pygame.transform.scale(image4,(110,100))
    # image4_position = (632,143)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):
                    #Here write the code to play one sound
                    video_path = "/home/ekrem/Videos/Teletabisi.mp4"
                    subprocess.run(["vlc", video_path])

                elif button2_rect.collidepoint(event.pos):
                    video_path = "/home/ekrem/Videos/Fifi i cvjetno drustvo.mp4"
                    subprocess.run(["vlc", video_path])
                
                elif button3_rect.collidepoint(event.pos):
                    video_path = "/home/ekrem/Videos/Jagodica bobica.mp4"
                    subprocess.run(["vlc", video_path])
                    
                elif button4_rect.collidepoint(event.pos):
                    video_path = "/home/ekrem/Videos/Mumijevi.mp4"
                    subprocess.run(["vlc", video_path])
               # Check for button click
                elif button_rect.collidepoint(event.pos):
                    open_new_window()         

        # Draw background
        new_window.blit(background, (0, 0))
        
        # new_window.blit(image1, image1_position)
        # new_window.blit(image2, image2_position)
        # new_window.blit(image3, image3_position)
        # new_window.blit(image4, image4_position)
        
        # Draw button
        # pygame.draw.rect(new_window, button_color, button_rect,0 )  # Draws a rounded button

        # new_window.blit(text, text_rect)

        pygame.display.flip()
    pygame.quit()
    sys.exit()
        
        
def open_new_window4():
    new_window = pygame.display.set_mode((800, 430))
    screen = pygame.display.set_mode((800, 430))
    pygame.display.set_caption("Igroland")
    
    # Load your background image
    background = pygame.image.load("/home/ekrem/Pictures/Igroland.png")  # Replace with your image path
    background = pygame.transform.scale(background, (800, 430))
 
    # Set background color
    # white_color = (255, 255, 255)
    # new_window.fill(white_color)
    
    # Define button properties
    button_color = (255, 255, 0)  # Yellow color
    button_rect = pygame.Rect(40, 350, 60, 60)  # Position and size of the button
    border_radius = 5
    
    font = pygame.font.Font(None, 36)
    text = font.render("", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)
    
    # Define button properties
    button1_color = (255, 255, 255)  # Yellow color
    button1_rect = pygame.Rect(43, 143, 110, 100)
    # image1 = pygame.image.load('/home/raspberry/Pictures/fif.jpg')
    # image1 = pygame.transform.scale(image1,(110,100))
    # image1_position = (43,143)
    
    button2_color = (255, 255, 255)  # Yellow color
    button2_rect = pygame.Rect(238,165, 110, 100)  # Position and size of the button
    # image2 = pygame.image.load('/home/raspberry/Pictures/mumijevi.jpg')
    # image2 = pygame.transform.scale(image2,(110,100))
    # image2_position = (238,143)
    
    button3_color = (255, 255, 255)  # Yellow color
    button3_rect = pygame.Rect(432, 143, 110, 100)
    # image3 = pygame.image.load('/home/raspberry/Pictures/fif.jpg')
    # image3 = pygame.transform.scale(image3,(110,100))
    # image3_position = (432,143)
    
    button4_color = (255, 255, 255)  # Yellow color
    button4_rect = pygame.Rect(632,165, 110, 100)  # Position and size of the button
    # image4 = pygame.image.load('/home/raspberry/Pictures/mumijevi.jpg')
    # image4 = pygame.transform.scale(image4,(110,100))
    # image4_position = (632,143)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
               # Check for button click
                if button_rect.collidepoint(event.pos):
                    open_new_window()
                elif button1_rect.collidepoint(event.pos):
                    path = '/home/ekrem/Desktop/jaje2.py'
                    subprocess.run(['python3',path])
                    
                elif button2_rect.collidepoint(event.pos):
                    path = '/home/ekrem/Desktop/paint.py'
                    subprocess.run(['python3',path])
                    
                elif button3_rect.collidepoint(event.pos):
                    path = '/home/ekrem/Desktop/snake3.py'
                    subprocess.run(['python3',path])
                    
                elif button4_rect.collidepoint(event.pos):
                    path = '/home/ekrem/Desktop/igrica_x0x.py'
                    subprocess.run(['python3',path])
                    
                    
                    
        # Draw background
        new_window.blit(background, (0, 0))
        
        # Draw button
        # pygame.draw.rect(new_window, button_color, button_rect,0 )  # Draws a rounded button

        # new_window.blit(text, text_rect)       
        pygame.display.flip()
    pygame.quit()
    sys.exit()
            
        

if __name__ == "__main__":
    main()

