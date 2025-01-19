import cv2
import numpy as np

def card_recognition(table_image):
  gray = cv2.cvtColor(table_image, cv2.COLOR_BGR2GRAY)

  # Thresholding to isolate cards
  _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  player_cards = []
  cards_dealt = []

  for contour in contours:
    area=cv2.contourArea(contour)

    if 1000 < area < 5000: # might have to be readjusted based on the table size
      x, y, w, h = cv2.boundingRect(contour)
      aspect_ratio = w / h
      if 0.5 < aspect_ratio < 0.8:
        card_img=table_image[y:y+h, x:x+w]

        # assuming cards_dealt are in the middle / upper half of the table
        if y < table_image.shape[0] // 2:
          cards_dealt.append("Ah") # Placeholder for Ace of Hearts
        else:
         player_cards.append("Kh") # Placeholder for King of Hearts

  return player_cards, cards_dealt
