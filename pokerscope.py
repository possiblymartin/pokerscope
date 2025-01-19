#!/usr/bin/env python3
import screen_capture as SC
import card_recognition as CR
import hand_analysis as HA
import time

def main():
  # monitor prompt
  monitors = SC.monitor_list()
  selected_monitor = SC.monitor_prompt(monitors)
  print(f"You have seleted monitor {selected_monitor}")

  while True:
    screenshot = SC.capture_screen(monitors[selected_monitor])
    player_cards, cards_dealt = CR.card_recognition(screenshot)

    print("Player cards:", player_cards)
    print("Board:", cards_dealt)

    hand_analytics = HA.analyze_hand(player_cards, cards_dealt)

    for stage, analysis in hand_analytics.items():
      print(f"{stage.capitalize()} Analysis:")
      if 'error' in analysis:
        print(f"Error: {analysis['error']}")
      else:
        print(f"Hand: {analysis['hand']}")
        print(f"Strength: {analysis['strength']}")
        if 'rank' in analysis:
          print(f"Rank: {analysis['rank']}")
        print()
    
    time.sleep(1)


if __name__ == "__main__":
  main()