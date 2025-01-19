from treys import Card, Evaluator

def analyze_hand(player_cards, cards_dealt):
  evaluator = Evaluator()

  player_hand = [Card.new(card) for card in player_cards]
  board = [Card.new(card) for card in cards_dealt]

  stages = {
    "preflop": [],
    "flop": board[:3] if len(board) >= 3 else [],
    "turn": board[:4] if len(board) >= 4 else [],
    "river": board
  }

  analysis = {}

  for stage, cards in stages.items():
    if stage == "preflop":
      analysis[stage] = {
        "hand": player_cards,
        "strength": "N/A (preflop)" # AI logic should probably be here
      }
    else:
      all_cards = cards + player_hand
      if len(all_cards) == 0:
        analysis[stage] = {
          "error": "No cards availabe for evaluation",
          "hand": []
        }
      elif len(all_cards) < 5:
        analysis[stage] = {
          "error": "Inssuficient cards for evaluation",
          "hand": []
        }
      else:
        try:
          hand_strength = evaluator.evaluate(cards, player_hand)
          hand_rank = evaluator.class_to_string(evaluator.get_rank_class(hand_strength))
          analysis[stage] = {
            "hand": player_cards + cards,
            "strength": hand_strength,
            "rank": hand_rank
          }
        except Exception as e:
          analysis[stage] = {
            "error": f"Evaluation error: {str(e)}",
            "hand": [str(card) for card in all_cards]
          }
  return analysis